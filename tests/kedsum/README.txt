Kedsum temperature and humidity sensor (http://amzn.to/25IXeng)
My models transmit at a bit lower freq. Around ~433.71 Mhz

Copyright (C) 2016 John Lifsey
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

Largely based on prologue, esperanza_ews, s3318p
Frame appears to be a differently-endianed version of the esperanza

Frame structure:
IIIIIIII????CC++++ttttTTTThhhhHHHH?????? PP

IIIIIIII unique id. changes on powercycle
CC channel, 00 = ch1, 10=ch3
++++ low temp nibble
tttt med temp nibble
TTTT high temp nibble
hhhh humidity low nibble
HHHH humidity high nibble


*** signal_start = 31553, signal_end = 327681
signal_len = 296128,  pulses = 279
Iteration 1. t: 105    min: 104 (13)    max: 107 (266)    delta 13
Iteration 2. t: 105    min: 103 (3)    max: 107 (276)    delta 1
Iteration 3. t: 105    min: 103 (3)    max: 107 (276)    delta 0
Distance coding: Pulse length 105

Short distance: 518, long distance: 1022, packet distance: 1997

p_limit: 105
bitbuffer:: Number of rows: 25 


Analyzing pulses...
Total count:  279,  width: 276127		(1104.5 ms)
Pulse width distribution:
 [ 0] count:  279,  width:   106 [102;109]	( 424 us)
Gap width distribution:
 [ 0] count:   26,  width:  1997 [1983;2259]	(7988 us)
 [ 1] count:  126,  width:   518 [509;571]	(2072 us)
 [ 2] count:  126,  width:  1023 [1016;1072]	(4092 us)
Pulse period distribution:
 [ 0] count:   26,  width:  2104 [2088;2366]	(8416 us)
 [ 1] count:  126,  width:   625 [615;678]	(2500 us)
 [ 2] count:  126,  width:  1130 [1121;1178]	(4520 us)
Level estimates [high, low]:  15917,     25
Frequency offsets [F1, F2]:    8348,      0	(+31.8 kHz, +0.0 kHz)
Guessing modulation: Pulse Position Modulation with fixed pulse width
Attempting demodulation... short_limit: 770, long_limit: 1073, reset_limit: 2260, demod_arg: 0
pulse_demod_ppm(): Analyzer Device 
bitbuffer:: Number of rows: 25 

[00] {0} : 
[01] {0} : 
[02] {0} : 
[03] {0} : 
[04] {0} : 
[05] {0} : 
[06] {0} : 
[07] {0} : 
[08] {0} : 
[09] {0} : 
[10] {0} : 
[11] {0} : 
[12] {0} : 
[13] {0} : 
[14] {0} : 
[15] {42} 32 52 d5 84 eb c0 : 00110010 01010010 11010101 10000100 11101011 11
[16] {0} : 
[17] {42} 32 52 d5 84 eb c0 : 00110010 01010010 11010101 10000100 11101011 11
[18] {0} : 
[19] {42} 32 52 d5 84 eb c0 : 00110010 01010010 11010101 10000100 11101011 11
[20] {0} : 
[21] {42} 32 52 d5 84 eb c0 : 00110010 01010010 11010101 10000100 11101011 11
[22] {0} : 
[23] {42} 32 52 d5 84 eb c0 : 00110010 01010010 11010101 10000100 11101011 11
[24] {42} 32 52 d5 84 eb c0 : 00110010 01010010 11010101 10000100 11101011 11
Test mode file issued 5 packets

