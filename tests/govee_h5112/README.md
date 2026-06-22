# Govee H5112 Dual-Probe Thermometer

https://www.govee.com/products/govee-h5112-refrigerator-thermometer

Battery-powered dual-probe thermometer that communicates via sub-GHz RF
(~912.375 MHz FCC nominal) to a separate Govee gateway hub. Shares the
RF sync word, CRC-16/AUG-CCITT, and 128-byte XOR key with the H5059 water
leak detector and H5310 pool/spa thermometer.

Probe 1 carries both temperature and humidity sensors; probe 2 is
temperature-only. The two probe connectors are physically keyed and cannot
be swapped.

## Capture notes

- Tuned frequency: 912.375 MHz (the FCC nominal; deviating by even 100 kHz
  pushes the signal to the filter edge at 250k sample rate and kills decodes).
- Sample rate: 250k is the correct value for H5112. The H5059/H5310 family
  normally needs ≥1 MS/s, but H5112 uses a narrower FSK deviation.
- Modulation: FSK_PULSE_PCM, short/long width 100 µs, reset_limit 2000 µs.

## Frame types

| File | Type     | id_wire      | Notes |
|------|----------|--------------|-------|
| g001 | Periodic | `0x04069cb2` | Autonomous 10-minute broadcast (msg_class 0x13). Includes 10-record history buffer. Both probes at room temperature; display-confirmed 23.6 °C on both probes at capture time. |
| g002 | Triggered | `0x08139cb2` | Gateway-triggered status response (msg_class 0x71). Sent in reply to a 0x70 network-test command. No history buffer. |
| g003 | Periodic | `0x0b279cb2` | Autonomous 10-minute broadcast, second physical unit (id_wire high-word 0x0b27). Probe 1 in refrigerator (~2.3 °C), probe 2 temperature shown as 1.6 °C (k=0 cold-start value; probe 2 was physically in a freezer at approximately −24 °C but rtl_433 had just started so wrap-count k was seeded to 0 rather than −1). |

## Probe 2 temperature encoding

Probe 2 uses a modular 8-bit encoding that wraps every 25.6 °C. The decoder
maintains a per-device wrap-count k and applies `T_abs = T_mod + k × 25.6`.
k is seeded on first decode using `T1 ≈ T2` (correct when both probes start
at room temperature, which is the normal setup procedure). If rtl_433 restarts
while probe 2 is already in a cold environment, k is seeded from the current
frame and may be off by ±1 until a 25.6 °C boundary crossing self-corrects it.

## Device IDs

The low 16 bits of id_wire (`0x9cb2`) are a gateway pairing token shared by
all sensors bound to the same Govee gateway. The high 16 bits identify the
individual device and change on re-pairing. `id` is id_wire with its two
16-bit halves byte-swapped (the app-facing representation).
