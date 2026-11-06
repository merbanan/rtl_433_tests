# Linear MultiCode and Delta-3 samples

Flipper Zero transmissions (Linear MultiCode and Delta-3 protocols) with made-up codes, recorded with
an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -12 dB, SNR 22-23 dB. Real remotes use 300 MHz
(MultiCode) and 318 MHz (Delta-3); the Flipper Zero sent the same timing at 433.92 MHz.
Four repeats per file. `protocol` loads `conf/Linear-MultiCode.conf`.

| File | Protocol | Bits | Code |
|---|---|---|---|
| `multicode_2a5_433.92M_250k.cu8` | MultiCode | 10 | `2A5` |
| `multicode_15a_433.92M_250k.cu8` | MultiCode | 10 | `15A` |
| `delta3_5a_433.92M_250k.cu8` | Delta-3 | 8 | `5A` |
| `delta3_c3_433.92M_250k.cu8` | Delta-3 | 8 | `C3` |
