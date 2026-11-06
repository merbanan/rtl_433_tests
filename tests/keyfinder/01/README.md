# Key finder tag samples

Flipper Zero RAW transmissions of the key finder format with made-up serials, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB. Six messages per file.

24 bits (20 bit serial, 4 bit button), then 4 short pulses and a 4 ms gap.
PWM, 1 = 400 us pulse + 1200 us gap, 0 = 1200 us pulse + 400 us gap.

| File | id | Button |
|---|---|---|
| `keyfinder_1a2b3_b1_433.92M_250k.cu8` | `1a2b3` | 1 |
| `keyfinder_1a2b3_b2_433.92M_250k.cu8` | `1a2b3` | 2 |
| `keyfinder_c0ffe_b4_433.92M_250k.cu8` | `c0ffe` | 4 |

Flex decoder `conf/KeyFinder.conf`, the `protocol` file loads it.
