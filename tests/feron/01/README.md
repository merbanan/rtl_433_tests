# Feron samples

Flipper Zero RAW transmissions (Feron message format) with made-up ids, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB, SNR 27 dB. Four messages per file. The decoder is disabled by default, `protocol` enables it.

| File | id | Command |
|---|---|---|
| `feron_1a2b_on_433.92M_250k.cu8` | `1a2b` | `85` (on) |
| `feron_1a2b_off_433.92M_250k.cu8` | `1a2b` | `84` (off) |
| `feron_c0de_brighter_433.92M_250k.cu8` | `c0de` | `86` (brighter) |

Each message is the 16 bit id, the command and the inverted command.
