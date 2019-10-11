# Cheep 433MHz TempSensor from AURIOL Weather Station 4-LD4437-1

https://www.lidl.de/de/auriol-funk-wetterstation/p242905?searchTrackingQuery=AURIOL&reg;%20Funk-Wetterstatio&searchTrackingId=Product.242905&searchTrackingPos=1&searchTrackingOrigPos=1&searchTrackingRelevancy=98.5&searchTrackingPage=1&searchTrackingPageSize=36&searchTrackingOrigPageSize=36

frequency: 433907500 Hz
call:      rtl_433 -f 433907500 -a -g 1
set:       channel-1/-2/-3 [a/b/c]
	   °C/°F [C/F] val [XX.X/-XX.X]
	   batter low indicator

                           01234567 89abcdef ghijklmn opqrstuv w
[01] {33} f0 a0 dc 85 00 : 11110000 10100000 11011100 10000101 0
'--' '--' '------------'   '------' ||'''--' '------' '------' |
 |    |     |_HEX values      |     || |  |     |        |     |_always zero (although missing in the last row)
 |    |_bit count             |     || |  |     |        |_this byte is related to the first 3bytes (but don't know how) some sort of checksum maybe
 |_row count                  |     || |  |     |_this byte holds the temperature values in (decimal) d°C (1/10 degree Celsius)(-256 if cdef is 1111)
                              |     || |  |_this is 0000 if the temperature is >= 0°C and 1111 if the temperature is <0°C (values in 3rd byte changing)
                              |     || |_this indicates the channel 00 ch1, 01 ch2, 10 ch3
                              |     ||_always zero
                              |     |_this is 1 as long as the battery is good and change to zero for low battery
                              |_this is some kind of ID, holds the same values until the batteries are changed (restart)


[cF71.6]__________________________________________________________
*** signal_start = 1167854, signal_end = 1387633
signal_len = 219779,  pulses = 237
Iteration 1. t: 122    min: 121 (2)    max: 124 (235)    delta 4
Iteration 2. t: 122    min: 121 (2)    max: 124 (235)    delta 0
Distance coding: Pulse length 122

Short distance: 469, long distance: 974, packet distance: 2133

p_limit: 122
bitbuffer:: Number of rows: 7 
[00] {33} f0 a0 dc 85 00 : 11110000 10100000 11011100 10000101 0
[01] {33} f0 a0 dc 85 00 : 11110000 10100000 11011100 10000101 0
[02] {33} f0 a0 dc 85 00 : 11110000 10100000 11011100 10000101 0
[03] {33} f0 a0 dc 85 00 : 11110000 10100000 11011100 10000101 0
[04] {33} f0 a0 dc 85 00 : 11110000 10100000 11011100 10000101 0
[05] {33} f0 a0 dc 85 00 : 11110000 10100000 11011100 10000101 0
[06] {32} f0 a0 dc 85 : 11110000 10100000 11011100 10000101 

[bF73.2]__________________________________________________________
*** signal_start = 670093, signal_end = 889875
signal_len = 219782,  pulses = 237
Iteration 1. t: 126    min: 125 (90)    max: 127 (147)    delta 10
Iteration 2. t: 125    min: 124 (37)    max: 127 (200)    delta 1
Iteration 3. t: 125    min: 124 (6)    max: 127 (231)    delta 0
Distance coding: Pulse length 125

Short distance: 467, long distance: 971, packet distance: 2131

p_limit: 125
bitbuffer:: Number of rows: 7 
[00] {33} f0 90 e5 29 00 : 11110000 10010000 11100101 00101001 0
[01] {33} f0 90 e5 29 00 : 11110000 10010000 11100101 00101001 0
[02] {33} f0 90 e5 29 00 : 11110000 10010000 11100101 00101001 0
[03] {33} f0 90 e5 29 00 : 11110000 10010000 11100101 00101001 0
[04] {33} f0 90 e5 29 00 : 11110000 10010000 11100101 00101001 0
[05] {33} f0 90 e5 29 00 : 11110000 10010000 11100101 00101001 0
[06] {32} f0 90 e5 29 : 11110000 10010000 11100101 00101001 

[aF74.8]___________________________________________________________
*** signal_start = 1606126, signal_end = 1832744
signal_len = 226618,  pulses = 237
Iteration 1. t: 126    min: 125 (79)    max: 128 (158)    delta 5
Iteration 2. t: 125    min: 124 (38)    max: 127 (199)    delta 2
Iteration 3. t: 125    min: 124 (7)    max: 127 (230)    delta 0
Distance coding: Pulse length 125

Short distance: 465, long distance: 971, packet distance: 2130

p_limit: 125
bitbuffer:: Number of rows: 7 
[00] {33} f0 80 ee 97 00 : 11110000 10000000 11101110 10010111 0
[01] {33} f0 80 ee 97 00 : 11110000 10000000 11101110 10010111 0
[02] {33} f0 80 ee 97 00 : 11110000 10000000 11101110 10010111 0
[03] {33} f0 80 ee 97 00 : 11110000 10000000 11101110 10010111 0
[04] {33} f0 80 ee 97 00 : 11110000 10000000 11101110 10010111 0
[05] {33} f0 80 ee 97 00 : 11110000 10000000 11101110 10010111 0
[06] {32} f0 80 ee 97 : 11110000 10000000 11101110 10010111 

[aC24.3]____________________________________________________________
*** signal_start = 5199093, signal_end = 5425711
signal_len = 226618,  pulses = 237
Iteration 1. t: 126    min: 125 (100)    max: 127 (137)    delta 10
Iteration 2. t: 125    min: 124 (54)    max: 127 (183)    delta 1
Iteration 3. t: 125    min: 124 (13)    max: 126 (224)    delta 1
Iteration 4. t: 125    min: 124 (13)    max: 126 (224)    delta 0
Distance coding: Pulse length 125

Short distance: 465, long distance: 971, packet distance: 2130

p_limit: 125
bitbuffer:: Number of rows: 7 
[00] {33} f0 80 f3 b9 00 : 11110000 10000000 11110011 10111001 0
[01] {33} f0 80 f3 b9 00 : 11110000 10000000 11110011 10111001 0
[02] {33} f0 80 f3 b9 00 : 11110000 10000000 11110011 10111001 0
[03] {33} f0 80 f3 b9 00 : 11110000 10000000 11110011 10111001 0
[04] {33} f0 80 f3 b9 00 : 11110000 10000000 11110011 10111001 0
[05] {33} f0 80 f3 b9 00 : 11110000 10000000 11110011 10111001 0
[06] {32} f0 80 f3 b9 : 11110000 10000000 11110011 10111001 

[bC24.6]___________________________________________________________
*** signal_start = 283371, signal_end = 509989
signal_len = 226618,  pulses = 237
Iteration 1. t: 127    min: 126 (135)    max: 128 (102)    delta 10
Iteration 2. t: 126    min: 125 (84)    max: 128 (153)    delta 1
Iteration 3. t: 126    min: 125 (45)    max: 127 (192)    delta 1
Iteration 4. t: 126    min: 125 (45)    max: 127 (192)    delta 0
Distance coding: Pulse length 126

Short distance: 465, long distance: 971, packet distance: 2132

p_limit: 126
bitbuffer:: Number of rows: 7 
[00] {33} f0 90 f6 6a 00 : 11110000 10010000 11110110 01101010 0
[01] {33} f0 90 f6 6a 00 : 11110000 10010000 11110110 01101010 0
[02] {33} f0 90 f6 6a 00 : 11110000 10010000 11110110 01101010 0
[03] {33} f0 90 f6 6a 00 : 11110000 10010000 11110110 01101010 0
[04] {33} f0 90 f6 6a 00 : 11110000 10010000 11110110 01101010 0
[05] {33} f0 90 f6 6a 00 : 11110000 10010000 11110110 01101010 0
[06] {32} f0 90 f6 6a : 11110000 10010000 11110110 01101010 

[cC24.8]___________________________________________________________
*** signal_start = 3793332, signal_end = 4019949
signal_len = 226617,  pulses = 237
Iteration 1. t: 126    min: 125 (143)    max: 127 (94)    delta 4
Iteration 2. t: 125    min: 125 (40)    max: 126 (197)    delta 1
Iteration 3. t: 14971    min: 0 (0)    max: 29942 (237)    delta 889009481
Iteration 4. t: 14971    min: 29942 (237)    max: 0 (0)    delta 1793046728
Iteration 5. t: 14971    min: 29942 (237)    max: 0 (0)    delta 0
Distance coding: Pulse length 14971

Short distance: 465, long distance: 972, packet distance: 2132

p_limit: 14971
bitbuffer:: Number of rows: 7 
[00] {33} f0 a0 f8 da 00 : 11110000 10100000 11111000 11011010 0
[01] {33} f0 a0 f8 da 00 : 11110000 10100000 11111000 11011010 0
[02] {33} f0 a0 f8 da 00 : 11110000 10100000 11111000 11011010 0
[03] {33} f0 a0 f8 da 00 : 11110000 10100000 11111000 11011010 0
[04] {33} f0 a0 f8 da 00 : 11110000 10100000 11111000 11011010 0
[05] {33} f0 a0 f8 da 00 : 11110000 10100000 11111000 11011010 0
[06] {32} f0 a0 f8 da : 11110000 10100000 11111000 11011010 

[aC19.0lb]_________________________________________________________
*** signal_start = 42363, signal_end = 262145
signal_len = 219782,  pulses = 237
Iteration 1. t: 126    min: 125 (85)    max: 128 (152)    delta 5
Iteration 2. t: 125    min: 124 (47)    max: 127 (190)    delta 2
Iteration 3. t: 125    min: 124 (4)    max: 127 (233)    delta 0
Distance coding: Pulse length 125

Short distance: 467, long distance: 971, packet distance: 2131

p_limit: 125
bitbuffer:: Number of rows: 7 
[00] {33} d2 00 be d2 00 : 11010010 00000000 10111110 11010010 0
[01] {33} d2 00 be d2 00 : 11010010 00000000 10111110 11010010 0
[02] {33} d2 00 be d2 00 : 11010010 00000000 10111110 11010010 0
[03] {33} d2 00 be d2 00 : 11010010 00000000 10111110 11010010 0
[04] {33} d2 00 be d2 00 : 11010010 00000000 10111110 11010010 0
[05] {33} d2 00 be d2 00 : 11010010 00000000 10111110 11010010 0
[06] {32} d2 00 be d2 : 11010010 00000000 10111110 11010010 

[cC-5.1lb]_________________________________________________________
*** signal_start = 35522, signal_end = 262145
signal_len = 226623,  pulses = 237
Iteration 1. t: 125    min: 125 (56)    max: 126 (181)    delta 4
Iteration 2. t: 14949    min: 0 (0)    max: 29898 (237)    delta 886387609
Iteration 3. t: 14949    min: 29898 (237)    max: 0 (0)    delta 1787780808
Iteration 4. t: 14949    min: 29898 (237)    max: 0 (0)    delta 0
Distance coding: Pulse length 14949

Short distance: 466, long distance: 972, packet distance: 2132

p_limit: 14949
bitbuffer:: Number of rows: 7 
[00] {33} d6 2f cd 02 00 : 11010110 00101111 11001101 00000010 0
[01] {33} d6 2f cd 02 00 : 11010110 00101111 11001101 00000010 0
[02] {33} d6 2f cd 02 00 : 11010110 00101111 11001101 00000010 0
[03] {33} d6 2f cd 02 00 : 11010110 00101111 11001101 00000010 0
[04] {33} d6 2f cd 02 00 : 11010110 00101111 11001101 00000010 0
[05] {33} d6 2f cd 02 00 : 11010110 00101111 11001101 00000010 0
[06] {32} d6 2f cd 02 : 11010110 00101111 11001101 00000010 


Some rows copied for inspection
___________________________________________________________________
[06] {32} f0 a0 dc 85 : 11110000 10100000 11011100 10000101
[06] {32} f0 a0 f8 da : 11110000 10100000 11111000 11011010
[06] {32} f0 90 f6 6a : 11110000 10010000 11110110 01101010
[06] {32} f0 a0 d1 c5 : 11110000 10100000 11010001 11000101
[06] {32} f0 a0 d3 1c : 11110000 10100000 11010011 00011100
[06] {32} f0 80 f3 b9 : 11110000 10000000 11110011 10111001 
[06] {32} f0 80 ee 97 : 11110000 10000000 11101110 10010111
[06] {32} f0 90 e5 29 : 11110000 10010000 11100101 00101001 
[06] {32} f0 a0 c1 ab : 11110000 10100000 11000001 10101011 
[06] {32} f0 a0 cd 1f : 11110000 10100000 11001101 00011111
[06] {32} f0 80 cd 66 : 11110000 10000000 11001101 01100110 
[06] {32} d6 2f cd 02 : 11010110 00101111 11001101 00000010
[06] {32} d2 00 be d2 : 11010010 00000000 10111110 11010010

