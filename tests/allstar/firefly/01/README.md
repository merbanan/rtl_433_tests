# Allstar Firefly gate remote samples

Flipper Zero RAW transmissions of the Allstar Firefly format (318ALD31K, Supertex ED-9 encoder) with
made-up DIP settings. Real remotes use 318 MHz; these were sent and recorded at 433.92 MHz
(250 kHz, RSSI about -10 dB, SNR about 29 dB), the timing is the same. Five messages per file.

9 trinary switches as 18 bits, 2 bits per switch: 11 = +, 10 = 0, 00 = -.
PWM, 1 = 4000 us pulse + 600 us gap, 0 = 600 us pulse + 4000 us gap, 30 ms between messages.

| File | Switches | code |
|---|---|---|
| `firefly_pmm000ppm_433.92M_250k.cu8` | `+--000++-` | `30abc` |
| `firefly_0pm0pm0pm_433.92M_250k.cu8` | `0+-0+-0+-` | `2cb2c` |
| `firefly_00000000m_433.92M_250k.cu8` | `00000000-` | `2aaa8` |

Flex decoder `conf/Allstar-Firefly.conf`, the `protocol` file loads it.
