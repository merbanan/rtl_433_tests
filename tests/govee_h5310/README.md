# Govee Pool/Spa Thermometer H5310

https://www.govee.com/products/h5310-wifi-pool-thermometer

Battery-powered floating pool/spa thermometer. The sensor communicates via
sub-GHz RF (~912.36 MHz) to a separate Govee gateway hub (the gateway handles
the Wi-Fi/cloud side). It shares its RF sync word, CRC, and XOR-key envelope
with the Govee H5059 water leak detector (see `../govee_h5059`) and other
devices in the same Govee sensor family.

See https://github.com/merbanan/rtl_433/pull/3564 (decoder by Paul Antaki)
and https://github.com/merbanan/rtl_433_tests/pull/503 (these captures, same
author).

Capture notes:
- Tuned frequency: 912.275 MHz (~100 kHz below the 912.375 MHz FCC nominal,
  chosen to avoid the RTL2832U's center/DC spike).
- Sample rate: >=1 MS/s is required in general for this family (FSK deviation
  is too wide for 250k to reliably lock), but these specific captures were
  recorded at 250k and decode reliably.
- Modulation: FSK_PULSE_PCM, short/long width 100us, reset_limit 2000us.

## Two physical units captured

- **g001-g003**: id_wire `0x71b09cb2` (`id` `0x9cb271b0`)
- **g004-g007**: id_wire `0xf8a79cb2` (`id` `0x9cb2f8a7`)

The on-wire ID is 32 bits; the low 16 bits (`9cb2`) are shared material common
to this entire Govee sensor family, and the high 16 bits distinguish the
physical unit. `id` is the same 32-bit value with its two 16-bit halves
swapped (the app-facing form), matching the convention used by
`govee_h5059.c`.

## Frame types

Only 2 of the 7 original captures are kept here as raw `.cu8` (one per
physical unit, chosen to cover the two frame types not otherwise duplicated):

| File | Event            | Notes |
| ---- | ---------------- | ----- |
| g002 | Temperature Update | LL=0x10, marker 0x11. Triggered by a forced report / unit-change action. |
| g006 | Periodic Update  | LL=0x3d, marker 0x1b. The sensor's autonomous ~10-minute broadcast -- the production-critical message. |

3 of the other 5 captures (g003, g005, g007 -- Status from both units, plus
the second unit's Temperature Update) are represented as extracted codes in
`codes_test.txt`/`codes_test.json` instead of raw `.cu8`:

| Code | Event            | Notes |
| ---- | ---------------- | ----- |
| g003 | Status           | LL=0x1f, marker 0x71. Sent in reply to a gateway poll. |
| g005 | Temperature Update | Same as g002, second physical unit. |
| g007 | Status           | Same as g003, second physical unit. |

The remaining 2 original captures (g001, g004 -- Ping, LL=0x1c/marker 0x70)
are not represented at all: rtl_433#3568 removed ping-frame decoding from
this decoder entirely, after discovering the marker/length combination is
shared with other Govee gateway devices (confirmed on the H5112 dual-probe
thermometer) with no way to disambiguate by frame structure alone -- see the
decoder's own doc-comment. Ping frames from these captures no longer produce
any Govee-H5310 output.

All temperature values use `T_C = (raw - 33168) / 10.0` and were confirmed
against each sensor's own on-device display at capture time.

Expected decodes are in the matching `.json` files (one JSON object per
decoded frame, as produced by `rtl_433 -r <file> -F json`, or `rtl_433 -y
<code> -F json` for the extracted codes). All originals verified against the
actual decoder before being added.
