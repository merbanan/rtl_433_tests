# Nero Radio samples

Flipper Zero RAW transmissions (Nero Radio message format, 56 bit) with made-up codes, recorded
with an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -7 dB. Three messages per file. `protocol`
enables the Nero Radio decoder (disabled by default).

| File | id | Button | Check byte |
|---|---|---|---|
| `radio_1a2b3c40abc_btn1_433.92M_250k.cu8` | `1a2b3c40abc` | 1 | `5a` |
| `radio_1a2b3c40abc_btn3_433.92M_250k.cu8` | `1a2b3c40abc` | 3 | `a5` |

The check byte of real remotes depends on the button; its rule is not known, made-up values are used.
