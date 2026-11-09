# Nero Sketch samples

Flipper Zero RAW transmissions (Nero Sketch message format) with made-up codes, recorded with an
RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -6.5 dB. Three messages per file. `protocol` selects
the flex conf (`conf/Nero-Sketch.conf`), which outputs the code as `code_hi` and `code_lo`. The first
message of a transmission is not decoded (the conf preamble starts with the stop pulse of a message).

| File | Code |
|---|---|
| `sketch_3c5a96e10f_433.92M_250k.cu8` | `3c5a96e10f` |
| `sketch_a1b2c3d4e5_433.92M_250k.cu8` | `a1b2c3d4e5` |
