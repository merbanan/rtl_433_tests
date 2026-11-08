# Microchip HCS200 decoder: KeeLoq subtypes

Flipper Zero transmissions with made-up serials, recorded with an RTL-SDR at 433.92 MHz, 250 kHz,
RSSI about -2.5 to -7 dB, SNR 30-40 dB. The HCS101 and AN-Motors samples were sent by the
Flipper Zero encoder from key files (made-up serials), the others as RAW messages.

| File | subtype | Hopping code | Notes |
|---|---|---|---|
| `hcs101_29d4b03_433.92M_250k.cu8` | HCS101 | `CCCC B 000` | unencrypted, 16 bit counter |
| `anmotors_5c3a1e7_433.92M_250k.cu8` | AN-Motors | `CC CC B 404` | unencrypted, 8 bit counter sent twice |
| `aprimatic_prog_0a3c5e1_433.92M_250k.cu8` | Aprimatic | `1A2B3C4D` | programming mode (all button bits set) |
| `deamio_prog_3e6a0c4_433.92M_250k.cu8` | DEA-Mio | `00000000` | programming mode (all button bits set) |
