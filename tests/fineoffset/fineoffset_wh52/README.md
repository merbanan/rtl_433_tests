# Fine Offset / Ecowitt WH52 3-in-1 Soil Moisture / Temperature / EC sensor

Captured live off-air at 915 MHz (250 kHz sample rate) alongside the manufacturer
gateway/app for ground truth. Decoder: merbanan/rtl_433#3602 (model "Fineoffset-WH52").

Each gfile concatenates two physical units so a single capture exercises several codes:
- gfile001: id 0058ac (44 %, 106.8 uS/cm, 20.4 C, 1.56 V) + id 005995 (36 %, 5.5 uS/cm, 18.4 C, 1.62 V)
- gfile002: id 005cb5 (25 %, 56.2 uS/cm, 20.7 C, 1.58 V) + id 005b45 (34 %, 25.5 uS/cm, 21.0 C, 1.58 V)

The four units span moisture 25-44 %, EC 5.5-107 uS/cm, temperature 18.4-21.0 C.
Verify: rtl_433 -r gfile001.cu8   (and gfile002.cu8)
