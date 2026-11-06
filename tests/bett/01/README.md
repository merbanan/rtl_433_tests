# BETT samples

Flipper Zero transmissions (BETT protocol: Berner, Elka, Tedsen, Teletaster) with made-up codes,
recorded with an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -8 dB, SNR 31-34 dB. Four repeats
per file. `protocol` loads `conf/BETT.conf`.

DIP switches: 2 bits each, 11 is +, 10 is 0, 00 is -.

| File | Code | DIP switches |
|---|---|---|
| `bett_38e38_433.92M_250k.cu8` | `38E38` | `+0-+0-+0-` |
| `bett_0e38e_433.92M_250k.cu8` | `0E38E` | `-+0-+0-+0` |
| `bett_3ffff_433.92M_250k.cu8` | `3FFFF` | `+++++++++` |
