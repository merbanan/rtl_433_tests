# Forever Young RTH11 "RF433 Temp & Humidity Sensor"

Sub device of the Tuya Wi-Fi weather station (gateway WS06) by Shenzhen Forever Young Technology Co., Ltd,
label "RF433 Temp & Humidity Sensor, Model: RTH11, Batch Number A2604", 2 x AAA, IP65.
Sold as "P80-FLY RTH11" and as eMylo RTH11.

* 433.92 MHz, FSK, pulse ~416 us (F1), gap 416 us = 0, 832 us = 1 (PPM on the gap)
* 80 bits, up to 9 repeats, bytes sent LSB first, CRC-8 (poly 0x59, XOR 0xe4)

Samples (250 kHz), three different sensors (IDs 22180, 24051, 24419):

| File | Sensor ID | Temperature | Humidity | Counter | Flags | Notes |
|---|---|---|---|---|---|---|
| g001_433.92M_250k.cu8 | 22180 | 15.7 C | 78 % | 22 | 4 | normal operation |
| g002_433.92M_250k.cu8 | 22180 | 18.6 C | 72 % | 3 | 6 | a few packets after power up |
| g003_433.92M_250k.cu8 | 22180 | 20.2 C | 76 % | 7 | 4 | reset button pressed (humidity bit 7 set) |
| g004_433.92M_250k.cu8 | 24051 | -3.6 C | 30 % | 92 | 15 | negative temperature, flags nibble reads 0xf |
| g005_433.92M_250k.cu8 | 24051 | -18.2 C | 48 % | 121 | 15 | freezer |
| g006_433.92M_250k.cu8 | 24419 | 19.9 C | 55 % | 8 | 8 | nearly empty batteries, battery low |

The `.json` files are the output of the proposed decoder (model `ForeverYoung-RTH11`).
