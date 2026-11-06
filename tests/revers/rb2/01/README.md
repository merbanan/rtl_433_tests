# Revers RB2 samples

Flipper Zero RAW transmissions (Revers RB2 message format) with made-up ids, recorded with an
RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -7 dB, SNR 31-35 dB. Eight messages per file, sent
back to back. `protocol` loads `conf/Revers-RB2.conf`.

| File | Message | id |
|---|---|---|
| `revers_rb2_012345_433.92M_250k.cu8` | `FFFFFFFF048D1600` | `012345` |
| `revers_rb2_3abcde_433.92M_250k.cu8` | `FFFFFFFFEAF37A00` | `3abcde` |
