# TS-8082 refrigerator/freezer thermometer (TS-808x family, Nexus 36 bit variant)

Wireless sensors of the TS-8082 refrigerator/freezer thermometer (2 channels, temperature only),
see discussion #3431 in rtl_433. The family also has the TS-8081 (1 channel) and the TS-8083
(3 channels, with humidity). Also sold as Brifit (ASIN B0FMXX5LLG) and Oria (ASIN B0FGPXYNW1).

Samples provided by @zuckschwerdt in rtl_433 PR #3722.

* 433.92 MHz, OOK PPM like the Nexus sensors: pulse ~490 us, gap ~1000 us = 0, ~2000 us = 1, sync gap ~3900 us
* 36 bits, 3 repeats
* The Nexus decoder rejects it (constant nibble 0x5 instead of 0xF).

Data layout (Nexus layout with a different constant, same as the 40 bit VOCOO 6202 in `../04/` without the trailing nibble):

    [id0] [id1] [flags] [temp0] [temp1] [temp2] [const] [humi0] [humi1]

- id: 8 bit, changes when the batteries are changed
- flags: B T C C – B battery OK, T test (unconfirmed), CC channel - 1
- temp: 12 bit signed, scale 10, °C
- const: always 0x5 (Nexus: 0xF)
- humi: always 0x00 (no humidity)

Format string:

    ID:8d BATT:b TEST:b CH:2d TEMP:12d CONST:4h HUMI:8d

Samples (250 kHz), battery OK:

| File | Code | Id | Channel | Temperature |
|---|---|---|---|---|
| g001_433.92M_250k.cu8 | `{36}da8f45500` | 218 | 1 | -18.7 °C |
| g002_433.92M_250k.cu8 | `{36}c19059500` | 193 | 2 | 8.9 °C |
| g004_433.92M_250k.cu8 | `{36}da8f46500` | 218 | 1 | -18.6 °C |
| g007_433.92M_250k.cu8 | `{36}da8f42500` | 218 | 1 | -19.0 °C |

The `.json` files are the output of the proposed decoder (rtl_433 PR #3722, model `TS-808x`).
