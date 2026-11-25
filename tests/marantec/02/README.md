# Marantec, 433.92 MHz

Flipper Zero transmissions with made-up codes, recorded with an RTL-SDR at 433.92 MHz, 250 kHz,
RSSI about -12 dB, SNR about 24 dB.

`ends_00` is a message ending in binary 00: the last short pulse runs into the gap and the
message slices as 48 bits, the missing last bit is 0.

| File | Key | id | button |
|---|---|---|---|
| `button_2_433.92M_250k.cu8` | `13091F0A28666` | 91F0A86 | 2 |
| `ends_00_433.92M_250k.cu8` | `1302B7E4401D8` | 2B7E401 | 4 |
