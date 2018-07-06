# Generic Black 4-Button 433MHz Remote

IC: EV1527 1500 (SOP-8)
PCB: AK-HD-4 REV:F05 2013.09.02
Battery: 12V

The remote does not come with DIP switches. The jumper pads on the back must be soldered to change the address.

The same PCB is used by the generic black 4-button 315MHz remote, with a different encoder IC and a few different passives.

![photo](photo.jpg)

### Captures:

```
$ rtl_433 -f 433920000 -a -t
```

File                  | Button
--------------------- | ------
g001_433.92M_250k.cu8 | A
g002_433.92M_250k.cu8 | A
g003_433.92M_250k.cu8 | B
g004_433.92M_250k.cu8 | B
g005_433.92M_250k.cu8 | C
g006_433.92M_250k.cu8 | C
g007_433.92M_250k.cu8 | D
g008_433.92M_250k.cu8 | D

### Analyze mode:

```
$ rtl_433 -r g001_433.92M_250k.cu8 -a

Test mode active. Reading samples from file: g001_433.92M_250k.cu8
Input format: uint8
*** signal_start = 14142, signal_end = 65537
signal_len = 51395,  pulses = 32
Iteration 1. t: 3    min: 2 (17)    max: 4 (15)    delta 4
Iteration 2. t: 2    min: 2 (7)    max: 3 (25)    delta 1
Iteration 3. t: 55    min: 0 (0)    max: 111 (32)    delta 11668
Iteration 4. t: 55    min: 111 (32)    max: 0 (0)    delta 24642
Iteration 5. t: 55    min: 111 (32)    max: 0 (0)    delta 0
Distance coding: Pulse length 55

Short distance: 450, long distance: 1252, packet distance: 3113

p_limit: 55
bitbuffer:: Number of rows: 6 
[00] {0} : 
[01] {13} 00 90 : 00000000 10010
[02] {6} 20 : 001000
[03] {1} 80 : 1
[04] {4} 20 : 0010
[05] {2} 00 : 00
Test mode file issued 1 packets
```

```
$ rtl_433 -r g002_433.92M_250k.cu8 -a

Test mode active. Reading samples from file: g002_433.92M_250k.cu8
Input format: uint8
*** signal_start = 14527, signal_end = 65537
signal_len = 51010,  pulses = 46
Iteration 1. t: 3    min: 2 (20)    max: 4 (26)    delta 4
Iteration 2. t: 3    min: 2 (9)    max: 4 (37)    delta 0
Pulse coding: Short pulse length 2 - Long pulse length 4

Short distance: 359, long distance: 1043, packet distance: 3192

p_limit: 3
bitbuffer:: Number of rows: 4 
[00] {1} 80 : 1
[01] {21} ff ff d8 : 11111111 11111111 11011
[02] {12} bb f0 : 10111011 1111
[03] {12} d7 00 : 11010111 0000
Test mode file issued 1 packets
```

```
$ rtl_433 -r g003_433.92M_250k.cu8 -a

Test mode active. Reading samples from file: g003_433.92M_250k.cu8
Input format: uint8
*** signal_start = 9651, signal_end = 65537
signal_len = 55886,  pulses = 40
Iteration 1. t: 3    min: 2 (23)    max: 4 (17)    delta 4
Iteration 2. t: 2    min: 2 (11)    max: 3 (29)    delta 1
Iteration 3. t: 68    min: 0 (0)    max: 136 (40)    delta 17693
Iteration 4. t: 68    min: 136 (40)    max: 0 (0)    delta 36992
Iteration 5. t: 68    min: 136 (40)    max: 0 (0)    delta 0
Distance coding: Pulse length 68

Short distance: 463, long distance: 1897, packet distance: 3086

p_limit: 68
bitbuffer:: Number of rows: 5 
[00] {0} : 
[01] {17} 00 00 00 : 00000000 00000000 0
[02] {10} 82 00 : 10000010 00
[03] {7} 16 : 0001011
[04] {1} 00 : 0
Test mode file issued 1 packets
```

```
$ rtl_433 -r g004_433.92M_250k.cu8 -a

Test mode active. Reading samples from file: g004_433.92M_250k.cu8
Input format: uint8
*** signal_start = 15953, signal_end = 65537
signal_len = 49584,  pulses = 29
Iteration 1. t: 2    min: 2 (7)    max: 3 (22)    delta 4
Iteration 2. t: 47    min: 0 (0)    max: 94 (29)    delta 8285
Iteration 3. t: 47    min: 94 (29)    max: 0 (0)    delta 17672
Iteration 4. t: 47    min: 94 (29)    max: 0 (0)    delta 0
Distance coding: Pulse length 47

Short distance: 535, long distance: 1891, packet distance: 3142

p_limit: 47
bitbuffer:: Number of rows: 5 
[00] {0} : 
[01] {12} 00 80 : 00000000 1000
[02] {8} 00 : 00000000 
[03] {1} 00 : 0
[04] {3} c0 : 110
Test mode file issued 1 packets
```


### Pulse Analyzer:

```
$ rtl_433 -r g001_433.92M_250k.cu8 -A

Test mode active. Reading samples from file: g001_433.92M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
Analyzing pulses...
Total count:    5,  width:   710		( 2.8 ms)
Pulse width distribution:
 [ 0] count:    3,  width:    18 [17;21]	(  72 us)
 [ 1] count:    2,  width:    14 [13;16]	(  56 us)
Gap width distribution:
 [ 0] count:    2,  width:   240 [239;242]	( 960 us)
 [ 1] count:    2,  width:    72 [71;73]	( 288 us)
Pulse period distribution:
 [ 0] count:    2,  width:   260 [260;260]	(1040 us)
 [ 1] count:    2,  width:    86 [86;87]	( 344 us)
Level estimates [high, low]:   2369,    132
Frequency offsets [F1, F2]:    7253,      0	(+27.7 kHz, +0.0 kHz)
Guessing modulation: No clue...

Test mode file issued 1 packets
```

```
$ rtl_433 -r g002_433.92M_250k.cu8 -A

Test mode active. Reading samples from file: g002_433.92M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
Analyzing pulses...
Total count:    3,  width:   362		( 1.4 ms)
Pulse width distribution:
 [ 0] count:    3,  width:    15 [15;16]	(  60 us)
Gap width distribution:
 [ 0] count:    1,  width:   246 [246;246]	( 984 us)
 [ 1] count:    1,  width:    70 [70;70]	( 280 us)
Pulse period distribution:
 [ 0] count:    1,  width:   261 [261;261]	(1044 us)
 [ 1] count:    1,  width:    86 [86;86]	( 344 us)
Level estimates [high, low]:   2660,    259
Frequency offsets [F1, F2]:    5934,      0	(+22.6 kHz, +0.0 kHz)
Guessing modulation: Pulse Position Modulation with fixed pulse width
Attempting demodulation... short_limit: 158, long_limit: 247, reset_limit: 247, sync_width: 0
pulse_demod_ppm(): Analyzer Device 
bitbuffer:: Number of rows: 1 
[00] {2} 80 : 10

Test mode file issued 1 packets
```

```
$ rtl_433 -r g003_433.92M_250k.cu8 -A

Test mode active. Reading samples from file: g003_433.92M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
Analyzing pulses...
Total count:    5,  width:   718		( 2.9 ms)
Pulse width distribution:
 [ 0] count:    4,  width:    17 [16;21]	(  68 us)
 [ 1] count:    1,  width:    11 [11;11]	(  44 us)
Gap width distribution:
 [ 0] count:    2,  width:   244 [238;251]	( 976 us)
 [ 1] count:    2,  width:    74 [71;77]	( 296 us)
Pulse period distribution:
 [ 0] count:    2,  width:   263 [259;267]	(1052 us)
 [ 1] count:    2,  width:    88 [88;88]	( 352 us)
Level estimates [high, low]:   2429,    145
Frequency offsets [F1, F2]:    6712,      0	(+25.6 kHz, +0.0 kHz)
Guessing modulation: No clue...

Detected OOK package	@ @0.000000s
Analyzing pulses...
Total count:    6,  width:   800		( 3.2 ms)
Pulse width distribution:
 [ 0] count:    1,  width:   179 [179;179]	( 716 us)
 [ 1] count:    5,  width:    20 [18;24]	(  80 us)
Gap width distribution:
 [ 0] count:    4,  width:    69 [61;82]	( 276 us)
 [ 1] count:    1,  width:   242 [242;242]	( 968 us)
Pulse period distribution:
 [ 0] count:    2,  width:   260 [260;261]	(1040 us)
 [ 1] count:    3,  width:    87 [85;89]	( 348 us)
Level estimates [high, low]:   2555,    193
Frequency offsets [F1, F2]:   16687,      0	(+63.7 kHz, +0.0 kHz)
Guessing modulation: No clue...

Test mode file issued 1 packets
```

```
$ rtl_433 -r g004_433.92M_250k.cu8 -A

Test mode active. Reading samples from file: g004_433.92M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
Analyzing pulses...
Total count:    9,  width:  1410		( 5.6 ms)
Pulse width distribution:
 [ 0] count:    8,  width:    16 [15;19]	(  64 us)
 [ 1] count:    1,  width:    12 [12;12]	(  48 us)
Gap width distribution:
 [ 0] count:    4,  width:   243 [242;245]	( 972 us)
 [ 1] count:    4,  width:    72 [71;75]	( 288 us)
Pulse period distribution:
 [ 0] count:    4,  width:   261 [260;262]	(1044 us)
 [ 1] count:    4,  width:    87 [87;88]	( 348 us)
Level estimates [high, low]:   2810,    113
Frequency offsets [F1, F2]:    6994,      0	(+26.7 kHz, +0.0 kHz)
Guessing modulation: No clue...

Test mode file issued 1 packets
```
