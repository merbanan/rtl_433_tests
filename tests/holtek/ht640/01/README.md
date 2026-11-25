# Holtek HT640 samples

Flipper Zero transmissions (Holtek HT640 protocol) with made-up codes, recorded with an RTL-SDR
at 433.92 MHz, 250 kHz, RSSI about -12 dB, SNR 20-24 dB. Four repeats per file.
`protocol` enables the Holtek HT640 decoder (disabled by default).

Pins: 0 low, 1 high, Z floating. Data nibbles: 0xa idle, 0xe on, 0xb off.

| File | A0-A9 | AD10-AD17 | id | Button | State |
|---|---|---|---|---|---|
| `ht640_b1_on_433.92M_250k.cu8` | `01Z10Z01Z1` | `ZZZZZZ1Z` | `dc4dc` | 1 | on |
| `ht640_b4_on_433.92M_250k.cu8` | `Z1100ZZ01Z` | `1ZZZZZZZ` | `7143d` | 4 | on |
