# Hormann HSM samples (44 bit)

Flipper Zero transmissions (Hormann HSM protocol) with made-up codes, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -12 dB, SNR 22 dB. Six messages per file.
`protocol` selects the flex conf (`conf/Hormann-HSM.conf`), which outputs the 24 bit code as `code`
and the full 44 bits as `data`.

| File | Data | Button |
|---|---|---|
| `hsm_btn1_433.92M_250k.cu8` | `ff5a3c9614f` | 1 |
| `hsm_btn8_433.92M_250k.cu8` | `ff13579b8a7` | 8 |
