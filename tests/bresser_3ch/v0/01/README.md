# Bresser Thermo-/Hygro-Sensor 3CH, V0 format samples

Flipper Zero RAW transmissions of the older V0 format (sent by the sensor before the V1 format) with
made-up values, recorded with an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -10 dB. Eight messages per file.

PPM, 475 us pulses, 0 = 990 us gap, 1 = 1980 us gap, 3975 us sync gap between repeats.
52 bits: 8 bit id, 4 bit flags (channel bit 0, channel bit 1, test, battery low), 12 bit signed
temperature (C, scale 10), 0xf separator, 8 bit humidity, 16 zero bits.

| File | id | Channel | Temperature | Humidity | Battery |
|---|---|---|---|---|---|
| `bresser_3ch_v0_5a_ch1_21.5C_45H_433.92M_250k.cu8` | 90 | 1 | 21.5 C | 45 | ok |
| `bresser_3ch_v0_5a_ch2_-7.3C_88H_433.92M_250k.cu8` | 90 | 2 | -7.3 C | 88 | ok |
| `bresser_3ch_v0_c3_ch3_30.2C_61H_batlow_433.92M_250k.cu8` | 195 | 3 | 30.2 C | 61 | low |

The decoder is disabled by default (no integrity check), the `protocol` file enables it.
