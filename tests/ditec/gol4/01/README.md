# Ditec GOL4 samples

Flipper Zero RAW transmissions (Ditec GOL4 message format, scrambled from made-up serials, buttons
and counters), recorded with an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -8 dB, SNR 27-33 dB.
Four messages per file. `protocol` enables the Ditec GOL4 decoder (disabled by default).

| File | Serial (id) | Button | Learn | Counter |
|---|---|---|---|---|
| `gol4_1a2b3c4d_btn1_433.92M_250k.cu8` | `1A2B3C4D` | 1 | 0 | 258 |
| `gol4_0badf00d_btn8_433.92M_250k.cu8` | `0BADF00D` | 8 | 0 | 0 |
| `gol4_55aa1234_prog_433.92M_250k.cu8` | `55AA1234` | 0 | 1 (programming mode) | 4660 |
