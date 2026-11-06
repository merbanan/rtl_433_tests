# Clemsa and Clemsa MasterCode samples

Flipper Zero transmissions (Clemsa and Clemsa MasterCode protocols) with made-up codes, recorded with
an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -8 dB, SNR 31-35 dB. Four repeats per file.
`protocol` loads `conf/Clemsa.conf`.

DIP switches: 2 bits each, 11 is +, 10 is 0, 00 is -.

| File | Protocol | Code | DIP switches | id | Button |
|---|---|---|---|---|---|
| `clemsa_32cb1_433.92M_250k.cu8` | Clemsa | `32CB1` | `+-0+-0+-` | `CB2C` | 1 |
| `clemsa_0ce2c_433.92M_250k.cu8` | Clemsa | `0CE2C` | `-+-+0-0+` | `338B` | 0 |
| `mastercode_5a30e38e4_433.92M_250k.cu8` | MasterCode | `5A30E38E4` | `+0-+0-+0` | `E38E` | 1 |
| `mastercode_0c102cb29_433.92M_250k.cu8` | MasterCode | `0C102CB29` | `-0+-0+-0` | `2CB2` | 2 |
