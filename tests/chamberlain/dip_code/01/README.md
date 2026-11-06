# Chamberlain / LiftMaster DIP switch remote samples

Flipper Zero RAW transmissions of the Chamberlain DIP switch (fixed code) format with made-up codes,
one per code length. Real remotes use 300 to 390 MHz; these were sent and recorded at 433.92 MHz
(250 kHz, RSSI about -12 dB, SNR about 20 dB), the timing is the same. Four messages per file.

PCM with 1 ms slots, each bit a 4 slot symbol: 0 = 0111, 1 = 0011, stop = 0001.

| File | Bits | id | Dip switches (Flipper order) |
|---|---|---|---|
| `cham_9bit_1a5_433.92M_250k.cu8` | 9 | `1a5` | `110100101` |
| `cham_8bit_b3_433.92M_250k.cu8` | 8 | `b3` | `10110x11` |
| `cham_7bit_55_433.92M_250k.cu8` | 7 | `55` | `1010101` |

The decoder is disabled by default (no integrity check), the `protocol` file enables it.
