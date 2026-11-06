# Power Smart blind remote samples

Flipper Zero RAW transmissions of the Power Smart format with made-up codes, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB. One press (8 messages without a gap) per file. The decoder is
enabled by default.

Manchester, 225 us half bits, 1 = high then low. 64 bits: `FD KCCCCCCD DDDDDDDK YY AA ~(16 bits) WW`,
with the 16 bits repeated inverted and Y = ~W - 1.

| File | id | Channel | Button |
|---|---|---|---|
| `power_smart_5a3c_ch05_up_433.92M_250k.cu8` | `55a3c` | 5 | 2 (up) |
| `power_smart_5a3c_ch05_down_433.92M_250k.cu8` | `55a3c` | 5 | 1 (down) |
| `power_smart_c381_ch2a_up_433.92M_250k.cu8` | `2ac381` | 42 | 2 (up) |
