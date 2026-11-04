# Govee Water Leak Detector H5059 -- top-probe leak regression captures

https://www.govee.com/products/h5059-water-leak-detector

These two captures are regression samples for a fix to `govee_h5059.c`'s
"Water Leak" event detection. See
https://github.com/merbanan/rtl_433/pull/3564 (fix by Paul Antaki, alongside
the companion Govee-H5310 decoder addition) and
https://github.com/merbanan/rtl_433_tests/pull/503 (these captures, same
author). Original H5059 decoder from PR #3493 by Reece Neff.

Background: the leak detector has two probe pairs (top and bottom). The
original decoder only fired the "Water Leak" event when the *bottom* probe
pair was wet (`dec[15] == 1 && dec[17] == 1`); a top-probe-only leak fell
through to the generic "Telemetry" event and was never reported. The fix
checks `dec[17] != 0 && (dec[14] == 0x01 || dec[15] == 0x01)`, and adds
`leak_top` / `leak_bottom` output fields so the affected probe pair can be
identified.

## Captures

| File | Event      | leak_top | leak_bottom | Notes |
| ---- | ---------- | -------- | ----------- | ----- |
| g001 | Water Leak | 1        | 0           | Top-probe-only leak -- the previously-undetected case. |
| g002 | Post Alarm | -        | -           | Follow-up frame sent ~1s after the leak event (x2 in this capture). |

Same RF parameters as `../govee_h5310`: 912.275 MHz, 250k sample rate,
FSK_PULSE_PCM. This unit's id_wire is `0x96839cb2` (the companion PR's
README states `0xac869cb2`, which doesn't match either capture's actual
decoded value -- corrected here).

Expected decodes are in the matching `.json` files (one JSON object per
decoded frame, as produced by `rtl_433 -r <file> -F json`). Both verified
against the actual decoder before being added.
