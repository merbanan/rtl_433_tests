# Doitrand gate remote samples

Flipper Zero RAW transmissions of the Doitrand format with made-up DIP settings, recorded with an RTL-SDR
at 433.92 MHz, 250 kHz, RSSI about -12 dB. Six messages per file, 24.8 ms apart.

24.8 ms gap, 700 us start pulse, 37 bits; 1 = 1100 us gap + 400 us pulse, 0 = 400 us gap + 1100 us pulse.
10 DIP switches and a 2 bit button, shown in the order of the Flipper Zero display.

| File | DIP switches | Button | Code |
|---|---|---|---|
| `doitrand_0001001010_b2_433.92M_250k.cu8` | `0001001010` | 2 | `0a5c082f5f` |
| `doitrand_0001001010_b1_433.92M_250k.cu8` | `0001001010` | 1 | `0a5c042f5f` |
| `doitrand_1111111111_b2_433.92M_250k.cu8` | `1111111111` | 2 | `1fe208af5f` |

The decoder is disabled by default (no integrity check), the `protocol` file enables it.
