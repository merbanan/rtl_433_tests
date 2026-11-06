# Phoenix V2 samples

Flipper Zero transmissions (Phoenix_V2 protocol) with made-up serials, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -3 to -7 dB, SNR 32-36 dB. Three messages per file.
`protocol` enables the Phoenix V2 decoder (disabled by default).

| File | Serial (id) | Button | Counter | Sent as |
|---|---|---|---|---|
| `phoenix_v2_1a2b3c40_btn1_433.92M_250k.cu8` | `1A2B3C40` | 1 | 256 | RAW |
| `phoenix_v2_deadbee0_btn4_433.92M_250k.cu8` | `DEADBEE0` | 4 | 32766 | RAW |
| `phoenix_v2_0c0ffee0_btn8_flipper_encoder_433.92M_250k.cu8` | `0C0FFEE0` | 8 | 19 | Flipper Zero encoder (key file) |

The counter is scrambled with the two high serial bytes; the decoder reverses it.
