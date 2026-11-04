Esperanza EWS-103 sensor on 433.92Mhz

No frame description was available on the internet therefore it was required
to reverse engineer it.
AAAABBBB ????CCTT TTTTTTTT TTHHHHHH HH?????? ??

A - Preamble
B - Rolling device ID
C - Channel (1-3)
T - Temperature (Little-endian!)
H - Humidity (Little-endian!)
? - Unknown

Sample Data:
Esperanze EWS: TemperatureF=55.5 TemperatureC=13.1 Humidity=74 Device_id=0 Channel=1

*** signal_start = 16189, signal_end = 262145
signal_len = 245956,  pulses = 266
Iteration 1. t: 142    min: 141 (37)    max: 143 (229)    delta 4
Iteration 2. t: 142    min: 141 (2)    max: 143 (264)    delta 0
Distance coding: Pulse length 142

Short distance: 487, long distance: 964, packet distance: 1920

p_limit: 142
bitbuffer:: Number of rows: 14 
[00] {0} : 
[01] {0} : 
[02] {42} 00 53 e5 69 02 00 : 00000000 01010011 11100101 01101001 00000010 00
[03] {0} : 
[04] {42} 00 53 e5 69 02 00 : 00000000 01010011 11100101 01101001 00000010 00
[05] {0} : 
[06] {42} 00 53 e5 69 02 00 : 00000000 01010011 11100101 01101001 00000010 00
[07] {0} : 
[08] {42} 00 53 e5 69 02 00 : 00000000 01010011 11100101 01101001 00000010 00
[09] {0} : 
[10] {42} 00 53 e5 69 02 00 : 00000000 01010011 11100101 01101001 00000010 00
[11] {0} : 
[12] {42} 00 53 e5 69 02 00 : 00000000 01010011 11100101 01101001 00000010 00
[13] {0} : 
Test mode file issued 4 packets

