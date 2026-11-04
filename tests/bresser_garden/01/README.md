# Bresser SmartHome Garden 7510100/7510200 (Baldr Homgar / RainPoint)

433.92 MHz FSK PCM garden-irrigation set. Decoder: `bresser_garden` (added in
rtl_433 PR #3005). Original issue: rtl_433 #2988.

The set is bidirectional (every message is acknowledged) and made of four devices,
of which two are normally on the air:

- **Gateway / weather station** HWS388WRF-V7 (Bresser 7510100), RF id `16780994` = `0x01000EC2`
- **Water timer valve** HTV103FRF (Bresser 7910100), RF id `520097180` = `0x1F000D9C`
- **Soil moisture sensor** HCS005FRF (Bresser 7910102), RF id `1191183797` = `0x470005B5`
  (relays through the valve; rarely heard directly — see below)

The top byte of the 32-bit id is the device class: `0x01` gateway, `0x1F` water timer,
`0x47` soil sensor. The decoder reports the model of the actual transmitter from this class
byte — `Bresser-Gateway`, `Bresser-WaterTimer`, or `Bresser-SoilMoisture` — so control and
ack frames are attributed to whichever device sent them, not to one generic name. An
unrecognised class falls back to the generic `Bresser-Garden`.

## Captured

RTL-SDR (Nooelec NESDR SMArt v5) indoors, ~8 m from the devices:

    rtl_433 -f 433.6M -s 1200k -w capture.cu8 -T 480

then split per frame with `rtl_433 -r capture.cu8 -R <bresser_garden> -S known`.
`433.6M / 1200k` spans both the uplink (~433.15) and downlink (~433.65) channels of the
set's frequency-division duplex. All frames are CRC-clean (CRC-16, poly 0x1021, init 0xd636).

## Samples

| file | frame | model | notes |
|---|---|---|---|
| `soil_moisture_0x09` | `0x09` soil sensor -> valve telemetry | `Bresser-SoilMoisture` | the sensor's own reading: moisture 47 %, 66.0 F, battery level 8. **Captured directly** — issue #2988 / PR #3005 never had this frame. It is ~1520 bits (long wake-up preamble), which is why it needs the raised length cap. |
| `water_timer_0x0a` | `0x0a` valve -> gateway telemetry | `Bresser-WaterTimer` | the same moisture/temperature block **relayed** by the valve (47 %, 66.0 F) — the valve has no soil probe. `device_type`/`sensor_number` are ids (both 6 here), `flag1` a per-message counter. |
| `base_ack_0x8a` | `0xa1` valve beacon + `0x8a` gateway ack | `Bresser-Gateway` | two devices: a `0xa1` `Beacon` from the valve (`Bresser-WaterTimer`, payload `02`, ack bit set) followed by the gateway's `0x8a` acknowledgement (`Bresser-Gateway`). The golden tracks the `0x8a` ack; the leading beacon is a tolerated cross-model frame. |
| `config_0x21` | `0x21` gateway -> valve heartbeat | `Bresser-Gateway` | payload `0109013c000a00`. Decoded (educated guess) as a `Heartbeat` exposing `heartbeat_interval_s` = 60 (the `0x3c`, a fixed interval, NOT the watering duration - that lives in `0x85`); the rest of the payload is kept as raw `msg`. |
| `watering_event_0x04` | `0x04` valve -> gateway watering event | `Bresser-WaterTimer` | `programme` 44462, `cycle_counter` 6628, `duration_s` 60, `trigger` 33 (`0x21`). Captured from a **manual** 1-minute run triggered in the HomGar app. `trigger` = source nibble (2 manual / 4 scheduled) × mode nibble (1 normal / 2 misting); a manual misting run reads `0x22`. `duration_s` is the *actual* elapsed seconds (a hand-stopped run at ~90 s read 91). |
| `schedule_0x86` | `0x86` gateway -> valve schedule table | `Bresser-Gateway` | one row per watering plan: Plan 1 normal 06:23 every day 180 s 2.0 L, Plan 2 **misting** 06:53 weekly (mask `0x42` = Mon+Sat, i.e. bits Mon+Sat in a Sun..Sat order) 40980 s no-limit. `more_parts` = 1 marks this as one page of a larger table (see the `schedule_0x86_split_*` fixtures). The valve stores and runs the schedule on its own clock. Leading `0xa1` beacon is a tolerated cross-model frame. |
| `schedule_config_0x85` | `0x85` gateway -> valve config | `Bresser-Gateway` | default `duration_s` 120, misting run 197 s / interval 807 s, `sensor_number` 6, `stop_moisture` 62 % (skip-when-wet threshold), `flow_rate` 20 % (litre-calc constant). All established by setting distinctive values in the app. |
| `config_counter_0x20` | `0x20` gateway config-change counter | `Bresser-Gateway` | one-byte `config_counter` (54 here) that increments on every settings change. |
| `soil_init_0x01` | `0x01` soil sensor INIT / pairing broadcast | `Bresser-SoilMoisture` | `firmware` 53, payload `0eff474700043507`. Captured 2026-07-20; the sensor emits this periodically (a *sender-only* re-announce — it never receives), so a restarted valve/base re-learns the pairing by waiting for the next one. `msg[7]` varies between broadcasts (`03` on 2026-07-17, `07` here), so it is a session/pairing nibble, not a constant. |
| `water_timer_init_0x01` | `0x01` water timer INIT / pairing broadcast | `Bresser-WaterTimer` | `firmware` 93, payload `06ff1f1f00075d`. Captured on valve power-up (battery reinsert 2026-07-20). Same `0x01` INIT as the soil sensor but **length 7** (no trailing session byte); `device_type` 6, class byte `0x1f`. Confirms INIT is a family-wide broadcast, not soil-specific. A leading gateway frame is a tolerated cross-model frame; the golden tracks the water-timer INIT. |
| `schedule_0x86_split_1of3` | `0x86` schedule table, page 1 of 3 | `Bresser-Gateway` | a 5-plan table split **2+2+1** across three `0x86` frames (consecutive `msg_counter` 18/19/20). Page 1: `more_parts=1`, plans 06:26 + 07:07 (both every-day; 07:07 = 420 s / 5.5 L, validating the LE duration + 0.1 L water-limit fields). |
| `schedule_0x86_split_2of3` | `0x86` schedule table, page 2 of 3 | `Bresser-Gateway` | `more_parts=1`, plans 08:18 **odd days** + 09:29 **even days** — confirms `day_mode` 2 = odd, 3 = even (both were decoder guesses until captured 2026-07-20). |
| `schedule_0x86_split_3of3` | `0x86` schedule table, page 3 of 3 | `Bresser-Gateway` | `more_parts=0` (last page), single plan 22:25. `more_parts` is `b[11]`: 1 = another page follows, 0 = last — reassemble the full table in `msg_counter` order until `more_parts=0`. |
| `status_request_0x02_0x82` | Water Timer `0x02` status poll **+** gateway `0x82` reply (same counter) | `Bresser-WaterTimer`, `Bresser-Gateway` | A poll/reply pair in one capture: the Water Timer polls (`0x02`, len 15, carrying its own state) and the gateway answers with `0x82` = poll type\|0x80, echoing `msg_counter` 6 — the reply-flag convention that also governs the acks. `gateway_time` = 15269896 is a monotonic u24 the base keeps cloud-synced (pulling the base's batteries on 2026-07-20 reset it to 0; it re-synced from the cloud on boot, not free-running uptime; ~1.07/s). Its exact unit is unconfirmed, so it is emitted raw and labelled `Status response`, not `time`. |

## Not yet captured

- **A disabled plan's `enabled` bit** — every captured plan has `enabled=1`; whether toggling a
  plan off in the app sends it with `enabled=0` or drops it from the table is not yet observed.

## Why the soil sensor is hard to hear

It is a small, low-power battery transmitter — only its probe prongs go into the soil; the
housing and antenna sit above ground. It transmits weakly, so even the gateway a few metres away
hears it at only about -118 dBm and relies on the valve to relay its reading onward.

But the dominant reason a nearby receiver still misses it is **co-channel FM capture**: the soil
sensor shares its channel with the much stronger gateway-side traffic (the valve's telemetry and
beacon, and the gateway's acks), and rtl_433 demodulates the band as a single FSK stream, so the
stronger signal wins whenever they overlap. This was confirmed directly by pulling the *valve's*
batteries: with the valve off-air the soil sensor decoded cleanly in every ~3-frame burst
regardless of moisture (46 % up through 93 % after watering); the instant the valve came back on
the air, reception dropped to roughly 1 of 3 frames. So an earlier guess that it was "heard better
when the soil was dry (47 %)" was a coincidence — the real driver is whether the loud gateway-side
traffic is present, not the soil moisture, and the antenna is above ground so it is not soil
attenuation. The fixtures here were captured with an SDR ~1 m from the sensor, where its signal
(SNR ~10-30 dB) dominates the co-channel traffic.
