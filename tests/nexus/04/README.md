# VOCOO 6202 indoor/outdoor thermometer hygrometer – outdoor sensor (Nexus 40 bit variant)

Wireless outdoor sensor of the VOCOO 6202 indoor/outdoor thermometer hygrometer
(label on the base station: "VOCOO, support@vocoovip.com, Model: 6202").
An identical looking set is sold without brand on AliExpress as
"Digital Thermometer Hygrometer with remote sensor" (same base station and sensor in the product
pictures, not yet confirmed with a recording): https://de.aliexpress.com/item/1005006781350030.html

Pictures: `front.jpg`, `back.jpg` (outdoor sensor), `station_front.jpg`, `station_back.jpg` (base station with label).
The sensor itself has no label.

* 433.92 MHz, OOK PPM like the Nexus sensors: pulse 488 us, gap 1012 us = 0, 1988 us = 1, sync gap 3992 us (measured with `-A`)
* 40 bits, 9 repeats (368 pulses) every ~57 s
* The current Nexus decoder rejects it (it expects 36 bits and the constant nibble 0xF).

Data layout (Nexus layout with a different constant and an additional constant nibble):

    [id0] [id1] [flags] [temp0] [temp1] [temp2] [const] [humi0] [humi1] [const2]

- id: 8 bit, changes when the batteries are changed
- flags: B T C C – B battery OK, T test (unconfirmed), CC channel - 1
- temp: 12 bit signed, scale 10, °C
- const: always 0x5 (Nexus: 0xF)
- humi: 8 bit %
- const2: always 0xA

Format string:

    ID:8d BATT:b TEST:b CH:2d TEMP:12d CONST:4h HUMI:8d CONST2:4h

Flex decoder:

    -X 'n=Vocoo-6202,m=OOK_PPM,s=1000,l=2000,g=3000,r=5000,bits=40,repeats>=3,unique,get=@0:{8}:id,get=@8:{1}:battery_ok,get=@10:{2}:channel,get=@12:{12}:temp_raw,get=@24:{4}:const,get=@28:{8}:humidity,get=@36:{4}:const2'

Samples (250 kHz, recorded 2026-10-07 with an RTL-SDR, FC0013 tuner), id 30, channel 1, battery OK:

| File | Temperature | Humidity |
|---|---|---|
| g003_433.92M_250k.cu8 | 8.4 °C | 99 % |
| g012_433.92M_250k.cu8 | 8.5 °C | 99 % |
| g027_433.92M_250k.cu8 | 8.6 °C | 99 % |
| g030_433.92M_250k.cu8 | 8.7 °C | 99 % |
| g042_433.92M_250k.cu8 | 8.9 °C | 98 % |

Codes, e.g. `{40}1e8054563a` (8.4 °C, 99 %), `{40}1e8057563a` (8.7 °C, 99 %).
The `.json` files are the output of the proposed decoder (rtl_433 PR, model `Vocoo-6202`).

All 16 messages received in 15 minutes had const 0x5 and const2 0xA.
Cross-check: at 12:45 the same day the decoded values (14.9 °C, 84 %) matched the display of the base station (`station_front.jpg`).
