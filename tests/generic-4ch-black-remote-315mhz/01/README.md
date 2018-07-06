# Generic Black 4-Button 315MHz Remote

IC: SCT2260 (SOP-16) similar to PT2260
PCB: AK-HD-4 REV:F05 2013.09.02
Battery: 12V

The remote does not come with DIP switches. The jumper pads on the back must be soldered to change the address.

The same PCB is used by the generic black 4-button 433MHz remote, with a different encoder IC and a few different passives.

![photo](photo.jpg)

### Captures:

```
$ rtl_433 -f 315000000 -a -t
```

File               | Button
------------------ | ------
g001_315M_250k.cu8 | A
g002_315M_250k.cu8 | A
g003_315M_250k.cu8 | B
g004_315M_250k.cu8 | B
g005_315M_250k.cu8 | C
g006_315M_250k.cu8 | C
g007_315M_250k.cu8 | D
g008_315M_250k.cu8 | D

### Analyze mode:

```
$ rtl_433 -r g001_315M_250k.cu8 -a

*** signal_start = 14629, signal_end = 65537
signal_len = 50908,  pulses = 56
Iteration 1. t: 234    min: 122 (33)    max: 346 (23)    delta 5
Iteration 2. t: 234    min: 122 (33)    max: 346 (23)    delta 0
Pulse coding: Short pulse length 122 - Long pulse length 346

Short distance: 99, long distance: 319, packet distance: 3401

p_limit: 234
bitbuffer:: Number of rows: 3 
[00] {25} 55 55 0c 00 : 01010101 01010101 00001100 0
[01] {25} 55 55 0c 00 : 01010101 01010101 00001100 0
[02] {6} 54 : 010101
Test mode file issued 1 packets
```

```
$ rtl_433 -r g002_315M_250k.cu8 -a

*** signal_start = 11956, signal_end = 65537
signal_len = 53581,  pulses = 62
Iteration 1. t: 235    min: 123 (35)    max: 347 (27)    delta 5
Iteration 2. t: 235    min: 123 (35)    max: 347 (27)    delta 0
Pulse coding: Short pulse length 123 - Long pulse length 347

Short distance: 98, long distance: 318, packet distance: 3401

p_limit: 235
bitbuffer:: Number of rows: 3 
[00] {19} 55 70 00 : 01010101 01110000 000
[01] {25} 55 55 c0 00 : 01010101 01010101 11000000 0
[02] {18} 55 55 c0 : 01010101 01010101 11
Test mode file issued 1 packets
```

```
$ rtl_433 -r g003_315M_250k.cu8 -a

*** signal_start = 220, signal_end = 65537
signal_len = 65317,  pulses = 82
Iteration 1. t: 235    min: 123 (49)    max: 347 (33)    delta 2
Iteration 2. t: 235    min: 123 (49)    max: 347 (33)    delta 0
Pulse coding: Short pulse length 123 - Long pulse length 347

Short distance: 98, long distance: 318, packet distance: 3403

p_limit: 235
bitbuffer:: Number of rows: 4 
[00] {25} 55 55 03 00 : 01010101 01010101 00000011 0
[01] {25} 55 55 03 00 : 01010101 01010101 00000011 0
[02] {25} 55 55 03 00 : 01010101 01010101 00000011 0
[03] {7} 54 : 0101010
Test mode file issued 1 packets
```

```
$ rtl_433 -r g004_315M_250k.cu8 -a

*** signal_start = 12655, signal_end = 65537
signal_len = 52882,  pulses = 61
Iteration 1. t: 234    min: 122 (36)    max: 346 (25)    delta 1373
Iteration 2. t: 234    min: 122 (36)    max: 346 (25)    delta 0
Pulse coding: Short pulse length 122 - Long pulse length 346

Short distance: 98, long distance: 319, packet distance: 3404

p_limit: 234
bitbuffer:: Number of rows: 3 
[00] {25} 55 55 30 00 : 01010101 01010101 00110000 0
[01] {25} 55 55 30 00 : 01010101 01010101 00110000 0
[02] {11} 55 40 : 01010101 010
Test mode file issued 1 packets
```


### Pulse Analyzer:

```
$ rtl_433 -r g001_315M_250k.cu8 -A

Test mode active. Reading samples from file: g001_315M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 12
	Tri-State:	 FFFFFFFF0010
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 12
	Tri-State:	 FFFFFFFF0010
Analyzing pulses...
Total count:   56,  width: 30909		(123.6 ms)
Pulse width distribution:
 [ 0] count:   33,  width:   121 [120;125]	( 484 us)
 [ 1] count:   23,  width:   345 [344;346]	(1380 us)
Gap width distribution:
 [ 0] count:   31,  width:   320 [319;322]	(1280 us)
 [ 1] count:   22,  width:   100 [99;102]	( 400 us)
 [ 2] count:    2,  width:  3402 [3402;3403]	(13608 us)
Pulse period distribution:
 [ 0] count:   53,  width:   443 [441;447]	(1772 us)
 [ 1] count:    2,  width:  3524 [3523;3525]	(14096 us)
Level estimates [high, low]:  16006,    392
Frequency offsets [F1, F2]:    2656,      0	(+10.1 kHz, +0.0 kHz)
Guessing modulation: Pulse Width Modulation with multiple packets
Attempting demodulation... short_limit: 233, long_limit: 323, reset_limit: 3404, sync_width: 0
pulse_demod_pwm(): Analyzer Device
bitbuffer:: Number of rows: 3 
[00] {25} aa aa f3 80 : 10101010 10101010 11110011 1
[01] {25} aa aa f3 80 : 10101010 10101010 11110011 1
[02] {6} a8 : 101010

Test mode file issued 1 packets
```

```
$ rtl_433 -r g002_315M_250k.cu8 -A

Test mode active. Reading samples from file: g002_315M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 192
	Tri-State:	 FFFFFFFF1000
Analyzing pulses...
Total count:   62,  width: 33581		(134.3 ms)
Pulse width distribution:
 [ 0] count:   35,  width:   123 [122;125]	( 492 us)
 [ 1] count:   27,  width:   346 [346;348]	(1384 us)
Gap width distribution:
 [ 0] count:   33,  width:   319 [318;321]	(1276 us)
 [ 1] count:   26,  width:    98 [98;101]	( 392 us)
 [ 2] count:    2,  width:  3402 [3402;3402]	(13608 us)
Pulse period distribution:
 [ 0] count:   59,  width:   443 [440;447]	(1772 us)
 [ 1] count:    2,  width:  3525 [3525;3526]	(14100 us)
Level estimates [high, low]:  15990,    375
Frequency offsets [F1, F2]:    3525,      0	(+13.4 kHz, +0.0 kHz)
Guessing modulation: Pulse Width Modulation with multiple packets
Attempting demodulation... short_limit: 234, long_limit: 322, reset_limit: 3403, sync_width: 0
pulse_demod_pwm(): Analyzer Device
bitbuffer:: Number of rows: 3 
[00] {19} aa 8f e0 : 10101010 10001111 111
[01] {25} aa aa 3f 80 : 10101010 10101010 00111111 1
[02] {18} aa aa 00 : 10101010 10101010 00

Test mode file issued 1 packets
```

```
$ rtl_433 -r g003_315M_250k.cu8 -A

Test mode active. Reading samples from file: g003_315M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 3
	Tri-State:	 FFFFFFFF0001
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 3
	Tri-State:	 FFFFFFFF0001
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 3
	Tri-State:	 FFFFFFFF0001
@0.000000s :	Smoke detector GS 558 	:	1365 	:	10 	:	0
	Raw Code:	 c0aaaa
Analyzing pulses...
Total count:   82,  width: 45319		(181.3 ms)
Pulse width distribution:
 [ 0] count:   49,  width:   122 [121;126]	( 488 us)
 [ 1] count:   33,  width:   346 [344;347]	(1384 us)
Gap width distribution:
 [ 0] count:   45,  width:   319 [318;321]	(1276 us)
 [ 1] count:   33,  width:    99 [98;101]	( 396 us)
 [ 2] count:    3,  width:  3403 [3403;3404]	(13612 us)
Pulse period distribution:
 [ 0] count:   78,  width:   443 [440;448]	(1772 us)
 [ 1] count:    3,  width:  3525 [3525;3526]	(14100 us)
Level estimates [high, low]:  15894,    265
Frequency offsets [F1, F2]:    3631,      0	(+13.9 kHz, +0.0 kHz)
Guessing modulation: Pulse Width Modulation with multiple packets
Attempting demodulation... short_limit: 234, long_limit: 322, reset_limit: 3405, sync_width: 0
pulse_demod_pwm(): Analyzer Device
bitbuffer:: Number of rows: 4 
[00] {25} aa aa fc 80 : 10101010 10101010 11111100 1
[01] {25} aa aa fc 80 : 10101010 10101010 11111100 1
[02] {25} aa aa fc 80 : 10101010 10101010 11111100 1
[03] {7} aa : 1010101

Test mode file issued 1 packets
```

```
$ rtl_433 -r g004_315M_250k.cu8 -A

Test mode active. Reading samples from file: g004_315M_250k.cu8
Input format: uint8
Detected OOK package	@ @0.000000s
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 48
	Tri-State:	 FFFFFFFF0100
@0.000000s :	Generic Remote
	House Code:	 21845
	Command:	 48
	Tri-State:	 FFFFFFFF0100
Analyzing pulses...
Total count:   61,  width: 32884		(131.5 ms)
Pulse width distribution:
 [ 0] count:   35,  width:   122 [120;125]	( 488 us)
 [ 1] count:   25,  width:   346 [345;347]	(1384 us)
 [ 2] count:    1,  width:    84 [84;84]	( 336 us)
Gap width distribution:
 [ 0] count:   33,  width:   320 [319;321]	(1280 us)
 [ 1] count:   25,  width:    99 [98;101]	( 396 us)
 [ 2] count:    2,  width:  3404 [3404;3405]	(13616 us)
Pulse period distribution:
 [ 0] count:   58,  width:   443 [440;447]	(1772 us)
 [ 1] count:    2,  width:  3527 [3527;3527]	(14108 us)
Level estimates [high, low]:  15891,    268
Frequency offsets [F1, F2]:    3251,      0	(+12.4 kHz, +0.0 kHz)
Guessing modulation: Pulse Width Modulation with sync/delimiter
Attempting demodulation... short_limit: 122, long_limit: 346, reset_limit: 3406, sync_width: 84
pulse_demod_pwm_precise(): Analyzer Device 
bitbuffer:: Number of rows: 2 
[00] {60} aa aa cf d5 55 67 ea a0 
[01] {0} : 

Test mode file issued 1 packets
```
