# Jarolift shutter remotes

Flipper Zero RAW transmissions with made-up serials and random hopping codes (Jarolift message
format), recorded with an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -2.5 to -7 dB, SNR 30-40 dB.

| File | Serial | Button | Group |
|---|---|---|---|
| `jarolift_0a1b2c3_group01_433.92M_250k.cu8` | 0x0A1B2C3 | 0x8 (up) | 0x01 |
| `jarolift_5f00d12_group80_433.92M_250k.cu8` | 0x5F00D12 | 0x8 (up) | 0x80 |

The frame is a 1500 us pulse and 8 short pulses as warm-up, a 3.8 ms gap, then 72 bits, LSB first:
32 bit KeeLoq hopping code, 28 bit serial, 4 bit button, 8 bit group. PWM: a 1 bit is a 400 us pulse
and an 800 us gap, a 0 bit is an 800 us pulse and a 400 us gap.

The decoder is disabled by default, so the set has a `protocol` file. JSON is
`rtl_433 -c 0 -R <n> -F json -r` output from the PR build (`<n>` from `rtl_433 -R help`).
