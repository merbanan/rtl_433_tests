# Treadmill remote (37 bit) samples

Flipper Zero RAW transmissions of the 37 bit treadmill remote format with made-up codes, recorded with
an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -10 dB. Six messages per file.

37 bits: 20 bit serial, 16 bit button code, 1 bit.
PWM, 1 = 900 us pulse + 300 us gap, 0 = 300 us pulse + 900 us gap, 6 ms between messages.

| File | id | Button |
|---|---|---|
| `treadmill37_1a2b3_00c3_433.92M_250k.cu8` | `1a2b3` | `00c3` |
| `treadmill37_1a2b3_0a50_433.92M_250k.cu8` | `1a2b3` | `0a50` |
| `treadmill37_c0ffe_f00d_433.92M_250k.cu8` | `c0ffe` | `f00d` |

The decoder is disabled by default (no integrity check), the `protocol` file enables it.
