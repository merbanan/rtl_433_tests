# Ambient Weather TX-8300/8339 Wireless Thermometer

Data for Ambient Weather TX-8300/8339 Wireless Thermometer

URL: https://www.ambientweather.com/amtx8300.html
FCC: https://fccid.io/OQH-000000-13-01

Output is temperature and (I think) battery status and it supports one of three different 433 MHz channels.

## Decoded output

Seems to decodeable like this:

```
rtl_433 -q -F json -R 0 -X 'tx8365:OOK_PPM_RAW:3000:5000:6000' -r g001_433.92M_250k.cu8
```

Giving outputs like this:

```
CH1_77.7F_433.92M_250k.cu8 -> {74}63a40c953c5bf36ae80
CH1_78.2F_433.92M_250k.cu8 -> {74}63a40c95fc5bf36a1fc
CH1_80.2F_433.92M_250k.cu8 -> {74}23a40c9a3c5bf365d54
CH1_82.4F_433.92M_250k.cu8 -> {74}63a40ca03c5bf35fee4
CH2_84.5F_433.92M_250k.cu8 -> {74}23a93ca47c56c35ba00
CH2_85.2F_433.92M_250k.cu8 -> {74}23893ca5bc76c35a6f4
CH2_85.6F_433.92M_250k.cu8 -> {74}23893ca63c76c359e44
CH2_86.1F_433.92M_250k.cu8 -> {74}23893cc07c76c33fa00
CH2_82.2F_433.92M_250k.cu8 -> {74}23a93c9e7c56c3618b0
CH3_83.3F_433.92M_250k.cu8 -> {74}23ad84a17c527b5e800
```

Note that there's a bit that seems to toggle between messages (like a rolling count), so the leading nibble is always either `2` or `6`.


Data files have channel number and temperature from receiver in file name. (temperature *may* disagree slightly for the CH1 files as there's a delay until the temperature on the receiver gets updated that wasn't account for).
