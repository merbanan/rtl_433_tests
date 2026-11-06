# Hollarm alarm system remote samples

Flipper Zero RAW transmissions of the Hollarm format with made-up serials, recorded with an RTL-SDR at
433.92 MHz, 250 kHz, RSSI about -10 dB. Eight messages per file. The decoder is enabled by default.

PPM, 200 us pulses, 0 = 1000 us gap, 1 = 1600 us gap. 42 bits: 24 bit serial, 4 bit unknown,
4 bit button, 8 bit sum of the 4 bytes before, 2 zero bits.

| File | id | Button |
|---|---|---|
| `hollarm_1a2b3c_arm_433.92M_250k.cu8` | `1a2b3c` | `2` (arm) |
| `hollarm_1a2b3c_disarm_433.92M_250k.cu8` | `1a2b3c` | `1` (disarm) |
| `hollarm_c0ffee_ring_433.92M_250k.cu8` | `c0ffee` | `8` (ring) |
