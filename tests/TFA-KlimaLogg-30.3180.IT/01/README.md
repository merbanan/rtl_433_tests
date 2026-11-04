# TFA Dostmann 30.3180.IT

Github Issue: #965 ( https://github.com/merbanan/rtl_433/issues/965 )

Sensor:

- TFA Dostmann
- Kat Nr.: 30.3180.IT
- ID:3F14
- Date:7/25/2016
- V34

https://www.conrad.de/de/tfa-303180it-thermo-hygro-funksensor-fuer-klimalogg-pro-passend-fuer-details-tfa-303039it-klimalogg-bestnr-1240367-396443.html


Data collected with:

rtl_433 -f 868.25M -s 1536000 -a -S unknown


SDR:

https://www.ebay.de/itm/Mini-Digital-USB2-0-TV-Stick-SDR-Tuner-Receiver-DVBT-DAB-FM-RTL2832U-R820T2-G2G6/113534622214?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649


Output of tfrec:

```
./tfrec -D -g 50 -T 1
Found Rafael Micro R820T tuner
Registering demod for TFA_1 KlimaLoggPro
GAIN 49.6
Frequency 868.2500MHz
Samplerate 1536000
START READ THREAD
#000 1549220248  2d d4 3f 14 85 93 29 60 70 56 a2           ID 3f14 +19.3 41%  seq 7 lowbat 0 RSSI 77
#001 1549220258  2d d4 3f 14 85 93 29 60 80 56 ba           ID 3f14 +19.3 41%  seq 8 lowbat 0 RSSI 76
#002 1549220269  2d d4 3f 14 85 93 29 60 90 56 d4           ID 3f14 +19.3 41%  seq 9 lowbat 0 RSSI 76
#003 1549220279  2d d4 3f 14 85 93 29 60 a0 56 66           ID 3f14 +19.3 41%  seq a lowbat 0 RSSI 76
#004 1549220289  2d d4 3f 14 85 92 29 60 b0 56 db           ID 3f14 +19.2 41%  seq b lowbat 0 RSSI 76
#005 1549220300  2d d4 3f 14 85 92 2a 60 c0 56 7c           ID 3f14 +19.2 42%  seq c lowbat 0 RSSI 76
#006 1549220310  2d d4 3f 14 85 92 2b 60 d0 56 89           ID 3f14 +19.2 43%  seq d lowbat 0 RSSI 76
#007 1549220321  2d d4 3f 14 85 92 2c 60 e0 56 a9           ID 3f14 +19.2 44%  seq e lowbat 0 RSSI 76
#008 1549220331  2d d4 3f 14 85 92 2c 60 f0 56 c7           ID 3f14 +19.2 44%  seq f lowbat 0 RSSI 76
```
