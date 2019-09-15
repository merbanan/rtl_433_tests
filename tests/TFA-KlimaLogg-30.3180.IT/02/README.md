# TFA Dostmann/Wertheim 30.3180.IT

Github Issue: #965 ( https://github.com/merbanan/rtl_433/issues/965 )

Sensor:

TFA Dostmann/Wertheim
Kat Nr.: 30.3180.IT
ID      DATE
==      ====
7a20    11/11/2014
7f4a    11/12/2014
7d60    11/13/2014
1d71    1/9/2015

SDR device used:

https://www.aliexpress.com/snapshot/0.html?spm=a2g0s.9042647.6.2.13754c4dfbcyf5&orderId=98844292356025&productId=32670752611


Content of folder(s):

01
rtl_433 -M newmodel -f 868.25M -s 1536000 -a -S all -g 50

7d60 - 23,2C - 37%
7f4a - 23,2C - 35%
797c - 23,0C - 37%
7a20 - 22,9C - 37%
0366 - ????? - ???

01.png -> picture of the sensors and their readings at time of capture.


Output of tfrec (although not at time of capturing the signals above - but this illustrates what comes out. I get quite a few BAD signals with tfrec - shitty receiver? (it was cheap...)):

```
$ tfrec -D -f 868250 -g 50 -T 1
Registering demod for TFA_1 KlimaLoggPro
Found Fitipower FC0012 tuner
GAIN 19.2
Frequency 868.2500MHz
Samplerate 1536000
START READ THREAD
Allocating 15 zero-copy buffers
#000 1555416767  2d d4 03 66 86 78 19 60 20 56 da           TFA1 ID 0366 +27.8 25% seq 2 lowbat 0 RSSI 80
#001 1555416768  2d d4 7d 60 86 35 23 60 c0 56 e8           TFA1 ID 7d60 +23.5 35% seq c lowbat 0 RSSI 79
#002 1555416771  2d d4 7f 4a 86 36 21 60 00 56 80           TFA1 ID 7f4a +23.6 33% seq 0 lowbat 0 RSSI 79
#003 1555416773  2d d4 79 7c 85 66 21 60 20 56 2b           TFA1 ID 797c +16.6 33% seq 2 lowbat 0 RSSI 79
#004 1555416775  2d d4 7a 20 86 30 26 60 b0 56 1a           TFA1 ID 7a20 +23.0 38% seq b lowbat 0 RSSI 78
#005 1555416776  2d d4 1d 71 86 34 21 60 f0 56 21           TFA1 ID 1d71 +23.4 33% seq f lowbat 0 RSSI 75
#006 1555416776  2d d4 03 66 86 78 19 60 30 56 b4           TFA1 ID 0366 +27.8 25% seq 3 lowbat 0 RSSI 74
#007 1555416778  2d d4 7d 60 86 34 23 60 d0 56 55           TFA1 ID 7d60 +23.4 35% seq d lowbat 0 RSSI 78
#008 1555416781  2d d4 7f 4a 86 36 21 60 10 56 ee           TFA1 ID 7f4a +23.6 33% seq 1 lowbat 0 RSSI 79
#009 1555416784  2d d4 79 7c 85 65 21 60 30 56 01           TFA1 ID 797c +16.5 33% seq 3 lowbat 0 RSSI 79
#010 1555416784  2d d4 7a 20 86 30 26 60 c0 56 21           TFA1 ID 7a20 +23.0 38% seq c lowbat 0 RSSI 78
#011 1555416786  2d d4 1d 71 86 34 21 c0 00 ac 72           TFA1 BAD 1 RSSI 71 (CRC 72 cc)
#012 1555416786  2d d4 03 66 86 78 19 60 40 56 8f           TFA1 ID 0366 +27.8 25% seq 4 lowbat 0 RSSI 74
#013 1555416789  2d d4 7d 60 86 35 23 60 e0 56 34           TFA1 ID 7d60 +23.5 35% seq e lowbat 0 RSSI 79
#014 1555416791  2d d4 7f 4a 86 35 21 60 20 56 18           TFA1 ID 7f4a +23.5 33% seq 2 lowbat 0 RSSI 79
#015 1555416794  2d d4 79 7c 85 65 22 60 40 56 a6           TFA1 ID 797c +16.5 34% seq 4 lowbat 0 RSSI 77
#016 1555416795  2d d4 7a 20 86 30 26 60 d0 56 4f           TFA1 ID 7a20 +23.0 38% seq d lowbat 0 RSSI 79
#017 1555416797  2d d4 1d 71 86 34 21 60 10 56 57           TFA1 ID 1d71 +23.4 33% seq 1 lowbat 0 RSSI 73
#018 1555416797  2d d4 03 66 86 28 03 0c 65 15 0e           TFA1 BAD 2 RSSI 72 (CRC 0e 24)
#019 1555416800  2d d4 7d 60 86 34 23 60 f0 56 89           TFA1 ID 7d60 +23.4 35% seq f lowbat 0 RSSI 79
#020 1555416801  2d d4 7f 4a 86 35 21 60 30 56 76           TFA1 ID 7f4a +23.5 33% seq 3 lowbat 0 RSSI 80
#021 1555416806  2d d4 79 78 85 64 22 60 50 56 1b           TFA1 BAD 3 RSSI 79 (CRC 1b ec)
#022 1555416808  2d d4 03 66 86 78 19 c0 c0 ac a6           TFA1 BAD 4 RSSI 73 (CRC a6 59)
#023 1555416808  2d d4 1d 71 86 34 21 60 20 56 e5           TFA1 ID 1d71 +23.4 33% seq 2 lowbat 0 RSSI 72
#024 1555416810  2d d4 7d 60 86 34 23 60 00 56 91           TFA1 ID 7d60 +23.4 35% seq 0 lowbat 0 RSSI 79
#025 1555416811  2d d4 7f 4a 86 35 21 60 40 56 4d           TFA1 ID 7f4a +23.5 33% seq 4 lowbat 0 RSSI 80
```

