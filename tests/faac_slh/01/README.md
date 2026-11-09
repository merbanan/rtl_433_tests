# FAAC SLH samples

Signals generated from the FAAC SLH protocol with made-up codes and transmitted by a Flipper Zero
as RAW files, recorded with an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -9 dB, SNR 28-33 dB.
Four repeats per file. `protocol` selects the flex conf (`conf/FAAC-SLH.conf`), which outputs the encrypted part as
`encrypted_hi` and `encrypted_lo`.

| File | Serial | Button | Encrypted | Seed |
|---|---|---|---|---|
| `button_1_433.92M_250k.cu8` | `3B6E4A2` | 1 | `9C4F17D2` | |
| `button_2_433.92M_250k.cu8` | `3B6E4A2` | 2 | `51A0E38B` | |
| `programming_433.92M_250k.cu8` | | | | `1E34E7AB` (counter 83) |

The conf outputs the programming message like the others (id `520f6b3`, button 13); flex can't
compute the seed.
