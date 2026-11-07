# Gate TX gate remote samples

Flipper Zero RAW transmissions of the Gate TX format with made-up serials, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB. Six messages per file, 17 ms apart.

17 ms gap, 700 us start pulse, 24 bits; 1 = 700 us gap + 350 us pulse, 0 = 350 us gap + 700 us pulse.
Reversed (LSB first) the 24 bits hold a 20 bit serial and a 4 bit button.

| File | id | Button |
|---|---|---|
| `gate_tx_1a2b3_b1_433.92M_250k.cu8` | `1a2b3` | 1 |
| `gate_tx_1a2b3_b2_433.92M_250k.cu8` | `1a2b3` | 2 |
| `gate_tx_c0ffe_b4_433.92M_250k.cu8` | `c0ffe` | 4 |

The decoder is disabled by default (no integrity check), the `protocol` file enables it.
