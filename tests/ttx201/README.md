# Emos TTX201 Remote Temperature Sensor
https://shop.emos.cz/2603108000-bezdratovy-teplomer-ttn303 (no English site)

* Manufacturer: Ewig Industries Macao
* Model No.: TTX201
* Maybe same as Ewig TTX201M (FCC ID: N9ZTTX201M)

* Measurable range: -20 °C ~ +50 °C
* 2 x 1.5 V AAA/LR4 battery
* Transmit Interval: every ~61s
* Frequency 433.92 MHz
* 5 Channels
* LED is blinking on every TX
* button to select channel, reset button

Manchester Encoding, pulse width: 460 us, gap width 1508 us.

A complete message is 444 bits:
```
  PPPPPPPP PPPP
    KKKKKK IIIIIIII S???BCCC ?XXXTTTT TTTTTTTT MMMMMMMM JJJJJJJJ  (repeated 7 times)
    KKKKKK IIIIIIII S???BCCC ?XXXTTTT TTTTTTTT MMMMMMMM      (last packet without J)
```

20-bit initial preamble, always 0
```
  PPPPPPPP PPPP = 0x0000 0x00
```

54-bit data packet format
```
  0   1    2   3    4   5    6   7    8   9    10  11   12  13  (nibbles #, aligned to 8-bit)
  ..KKKKKK IIIIIIII S???BCCC ?XXXTTTT TTTTTTTT MMMMMMMM JJJJJJJJ

  K = 6-bit checksum, sum of nibbles 2-11
  I = 8-bit sensor ID
  S = startup (0 = normal operation, 1 = reset or battery changed)
  ? = unknown, always 0
  B = battery status (0 = OK, 1 = low)
  C = 3-bit channel, 0-4
  X = 3-bit packet index, 0-7
  T = 12-bit signed temperature10 in Celsius
  M = 8-bit postmark, always 0x14
  J = 8-bit packet separator, always 0xF8
```

Sample received raw data package:
```
  bitbuffer:: Number of rows: 1
  [00] {444} 00 00 06 f0 80 00 41 c5 3e 1c c2 00 11 07 14 f8 77 08 00 84 1c 53 e1 ec 20 03 10 71 4f 87 f0 80 10 41 c5 3e 20 c2 00 51 07 14 f8 87 08 01 84 1c 53 e2 2c 20 07 10 71 40 
```

Decoded:
```
  K   I    S    B  C    X   T    M     J
  27  194  0x0  0  0x0  0   263  0x14  0xf8
  28  194  0x0  0  0x0  1   263  0x14  0xf8
  29  194  0x0  0  0x0  2   263  0x14  0xf8
  30  194  0x0  0  0x0  3   263  0x14  0xf8
  31  194  0x0  0  0x0  4   263  0x14  0xf8
  32  194  0x0  0  0x0  5   263  0x14  0xf8
  33  194  0x0  0  0x0  6   263  0x14  0xf8
  34  194  0x0  0  0x0  7   263  0x14
```

```
Analyzing pulses...
Total count:  373,  width: 110415		(441.7 ms)
Pulse width distribution:
 [ 0] count:  302,  width:   115 [113;122]	( 460 us)
 [ 1] count:   71,  width:   237 [234;240]	( 948 us)
Gap width distribution:
 [ 0] count:  292,  width:   128 [126;133]	( 512 us)
 [ 1] count:    8,  width:   377 [376;381]	(1508 us)
 [ 2] count:   72,  width:   251 [248;253]	(1004 us)
Pulse period distribution:
 [ 0] count:  271,  width:   244 [241;252]	( 976 us)
 [ 1] count:   58,  width:   489 [485;497]	(1956 us)
 [ 2] count:   43,  width:   366 [364;368]	(1464 us)
Level estimates [high, low]:  14140,    126
Frequency offsets [F1, F2]:  -18457,      0	(-70.4 kHz, +0.0 kHz)
```

![Emos TTX201 Front](ttx201-sensor-front.jpg)
![Emos TTX201 Rear](ttx201-sensor-rear.jpg)

