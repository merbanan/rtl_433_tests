# Nord ICE gate remote samples

Flipper Zero RAW transmissions of the Nord ICE format with made-up serials, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB. Six messages per file.

33 bits: serial high 18 bits, 6 bit button, serial low 9 bits.
PWM, 1 = 800 us pulse + 300 us gap, 0 = 300 us pulse + 800 us gap, 7.5 ms between messages.

| File | id | Button |
|---|---|---|
| `nord_ice_1a2b3c4_b01_433.92M_250k.cu8` | `1a2b3c4` | `01` |
| `nord_ice_1a2b3c4_b02_433.92M_250k.cu8` | `1a2b3c4` | `02` |
| `nord_ice_5c0ffee_b10_433.92M_250k.cu8` | `5c0ffee` | `10` |

The decoder is disabled by default (no integrity check), the `protocol` file enables it.
