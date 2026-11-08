# Hay21 remote samples

Flipper Zero RAW transmissions of the Hay21 format with made-up serials, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB. Six messages per file.

21 bits: 8 bit button, 8 bit serial, 4 bit counter, 1 bit always 1.
PWM, 1 = 700 us pulse + 300 us gap, 0 = 300 us pulse + 700 us gap.

| File | id | Button | Counter |
|---|---|---|---|
| `hay21_3e_onoff_cnt1_433.92M_250k.cu8` | `3e` | `5a` (on/off) | 1 |
| `hay21_3e_mode_cnt2_433.92M_250k.cu8` | `3e` | `c3` (mode) | 2 |
| `hay21_d7_hold_cnt9_433.92M_250k.cu8` | `d7` | `88` (hold) | 9 |

The decoder is disabled by default (no integrity check), the `protocol` file enables it.
