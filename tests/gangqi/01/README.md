# GangQi alarm system remote samples

Flipper Zero RAW transmissions of the GangQi format with made-up serials, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB. Six messages per file. The decoder is enabled by default.

34 bits: 16 bit serial, 4 bit constant 0xd, 4 bit button, 8 bit checksum, 2 zero bits.
The checksum is 0xc8 minus the first three bytes (type 1, the remotes) or 0x02 plus them (type 2).

| File | id | Button | Checksum type |
|---|---|---|---|
| `gangqi_1a2b_arm_433.92M_250k.cu8` | `1a2b` | `d` (arm) | 1 |
| `gangqi_1a2b_disarm_433.92M_250k.cu8` | `1a2b` | `e` (disarm) | 1 |
| `gangqi_c0de_ring_sum2_433.92M_250k.cu8` | `c0de` | `7` (ring) | 2 |
