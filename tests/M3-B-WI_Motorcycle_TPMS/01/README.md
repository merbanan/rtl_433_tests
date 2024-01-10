# Motorcycle TPMS (Model: M3-B-WI)

## Recorded signals

rtl_433 wasn't able to record these unknown signals; Therefore, I used Universal Radio Hacker.

433.92MHz, 1MSps, 1MHz.

### File name format

```
(Front/Rear)-PSI-TempCelcius.complex16s

F-29-23.complex16s
R-10-26.complex16s
...
```


## Sensor specification

| | | |
|-|-|-|
| Pressure testing range:    | 0 ~ 8 BAR (0 ~ 116 PSI) |
| Temperature testing range: | -40°C ~ +85°C           |
| Frequency:                 | FSK433.92MHz            |

Text printed on sensors:
* 19L0038844 / F
* 19L0038854 / R


## Related links and pictures

There's no manufacturer given on the packaging but I found very similar (pretty much the same) products on Amazon:
* https://www.amazon.de/dp/B07DR9F2NY/
* https://www.amazon.de/dp/B07HJ184X3/


## Decoding

When there's a change in pressure/temperatur the sensor is sending two bursts (?). I tried to compare 11 measurements (= 22 bursts/packets) but they have absolutely nothing in common...

First column numerates all packets; second column is the decoded value with Manchester 1 in Hex; third column is just the concatenation of two packets; last columns represent the measurements.

Note: I just played around with these signals, they are not contained in this folder.

| Packet |       HEX Manchester 1      |   |                      Concatenated                     |   | Front/Rear | PSI | °C |
|:------:|:---------------------------:|:-:|:-----------------------------------------------------:|:-:|:----------:|:---:|:--:|
|    1   | 03ffc00000040001fffff800000 |   | 03ffc00000040001fffff800000f000000000000000000000000  |   |      F     |  38 | 24 |
|    2   | f000000000000000000000000   |   |                                                       |   |            |     |    |
|    3   | fffe00000fffffffffffffffff8 |   | fffe00000fffffffffffffffff8c00000000000fffffffe0fffe  |   |      F     |  36 | 25 |
|    4   | c00000000000fffffffe0fffe   |   |                                                       |   |            |     |    |
|    5   | 00e1ffffffffffffbffffffff8  |   | 00e1ffffffffffffbffffffff8000000000800000000000000    |   |      F     |  35 | 24 |
|    6   | 000000000800000000000000    |   |                                                       |   |            |     |    |
|    7   | fffffffffffffffffffffffff   |   | fffffffffffffffffffffffff003f0001fff00000fffffffffc   |   |      F     |  32 | 24 |
|    8   | 003f0001fff00000fffffffffc  |   |                                                       |   |            |     |    |
|    9   | 30000c1c07ff800000000000    |   | 30000c1c07ff80000000000000018003df007c00001ffffe      |   |      F     |  31 | 24 |
|   10   | 00018003df007c00001ffffe    |   |                                                       |   |            |     |    |
|   11   | 001ff801fc03fc01fffffffff8  |   | 001ff801fc03fc01fffffffff8ffffffc001fffffffffff80fe   |   |      F     |  29 | 25 |
|   12   | ffffffc001fffffffffff80fe   |   |                                                       |   |            |     |    |
|   13   | 000003fc0000fffffffffff800  |   | 000003fc0000fffffffffff800000007ffffffffffffffff8003c |   |      F     |  28 | 24 |
|   14   | 000007ffffffffffffffff8003c |   |                                                       |   |            |     |    |
|   15   | 3fffc00007fffffa1fffc0      |   | 3fffc00007fffffa1fffc00d000cfc04000103f00ff8          |   |      F     |  26 | 25 |
|   16   | 0d000cfc04000103f00ff8      |   |                                                       |   |            |     |    |
|   17   | 0ffff007ffffffffffffffffff  |   | 0ffff007ffffffffffffffffff000000000000000000fe0000    |   |      F     |  25 | 24 |
|   18   | 000000000000000000fe0000    |   |                                                       |   |            |     |    |
|   19   | 000000f3ffffe3f80003ffffe   |   | 000000f3ffffe3f80003ffffe01fffff1fffff001f8fffffffe   |   |      F     |  23 | 24 |
|   20   | 01fffff1fffff001f8fffffffe  |   |                                                       |   |            |     |    |
|   21   | c041801fffc7f00000000       |   | c041801fffc7f000000007f80000000f803fc0000e18          |   |      F     |  20 | 24 |
|   22   | 7f80000000f803fc0000e18     |   |                                                       |   |            |     |    |