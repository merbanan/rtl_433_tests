
GT-WT02 is not decoded too. So here are the samples for the GT-WT02:

__GT-WT02 - Battery-OK, No-Button, Channel 2, 21,1 °C, 31%__

<pre><code>
*** signal_start = 4671389, signal_end = 4921346, signal_len = 249957, pulses_found = 240
Iteration 1. t: 140    min: 139 (40)    max: 141 (200)    delta 9
Iteration 2. t: 140    min: 139 (4)    max: 141 (236)    delta 0
Distance coding: Pulse length 140

Short distance: 514, long distance: 1024, packet distance: 2254

p_limit: 140
bitbuffer:: Number of rows: 13
[00] { 0}                :
[01] {37} c5 10 d4 3f a0 : 11000101 00010000 11010100 00111111 10100
[02] { 1} 00             : 0
[03] {37} c5 10 d4 3f a0 : 11000101 00010000 11010100 00111111 10100
[04] { 1} 00             : 0
[05] {37} c5 10 d4 3f a0 : 11000101 00010000 11010100 00111111 10100
[06] { 1} 00             : 0
[07] {37} c5 10 d4 3f a0 : 11000101 00010000 11010100 00111111 10100
[08] { 1} 00             : 0
[09] {37} c5 10 d4 3f a0 : 11000101 00010000 11010100 00111111 10100
[10] { 1} 00             : 0
[11] {37} c5 10 d4 3f a0 : 11000101 00010000 11010100 00111111 10100
[12] { 0}                :
*** Saving signal to file g192_433.92M_250k.cu8 (265228 samples, 655360 bytes)
</code></pre>

__GT-WT02 - Battery-OK, No-Button, Channel 2, 21,0 °C, 32%__

<pre><code>
*** signal_start = 9597298, signal_end = 9835039, signal_len = 237741, pulses_found = 240
Iteration 1. t: 142    min: 141 (178)    max: 144 (62)    delta 20
Iteration 2. t: 141    min: 140 (103)    max: 143 (137)    delta 2
Iteration 3. t: 140    min: 139 (29)    max: 142 (211)    delta 2
Iteration 4. t: 140    min: 139 (1)    max: 142 (239)    delta 0
Distance coding: Pulse length 140

Short distance: 514, long distance: 1023, packet distance: 2252

p_limit: 140
bitbuffer:: Number of rows: 13
[00] { 0}                :
[01] {37} c5 10 d2 41 28 : 11000101 00010000 11010010 01000001 00101
[02] { 1} 00             : 0
[03] {37} c5 10 d2 41 28 : 11000101 00010000 11010010 01000001 00101
[04] { 1} 00             : 0
[05] {37} c5 10 d2 41 28 : 11000101 00010000 11010010 01000001 00101
[06] { 1} 00             : 0
[07] {37} c5 10 d2 41 28 : 11000101 00010000 11010010 01000001 00101
[08] { 1} 00             : 0
[09] {37} c5 10 d2 41 28 : 11000101 00010000 11010010 01000001 00101
[10] { 1} 00             : 0
[11] {37} c5 10 d2 41 28 : 11000101 00010000 11010010 01000001 00101
[12] { 0}                :
*** Saving signal to file g308_433.92M_250k.cu8 (351795 samples, 786432 bytes)
</code></pre>

Now some samples with the transmit button pressed on the outdoor unit...

__GT-WT02 - Battery-OK, Button-PRESSED, Channel 2, 22,1 °C, 38%___

<pre><code>
*** signal_start = 17503417, signal_end = 17751278, signal_len = 247861, pulses_found = 240
Iteration 1. t: 140    min: 139 (97)    max: 141 (143)    delta 17
Iteration 2. t: 139    min: 138 (18)    max: 141 (222)    delta 1
Iteration 3. t: 139    min: 138 (3)    max: 140 (237)    delta 1
Iteration 4. t: 139    min: 138 (3)    max: 140 (237)    delta 0
Distance coding: Pulse length 139

Short distance: 514, long distance: 1024, packet distance: 2214

p_limit: 139
bitbuffer:: Number of rows: 14
[00] { 0}                :
[01] {37} 14 50 dd 4d a0 : 00010100 01010000 11011101 01001101 10100
[02] { 0}                :
[03] { 0}                :
[04] {37} 14 50 dd 4d a0 : 00010100 01010000 11011101 01001101 10100
[05] { 1} 00             : 0
[06] {37} 14 50 dd 4d a0 : 00010100 01010000 11011101 01001101 10100
[07] { 1} 00             : 0
[08] {37} 14 50 dd 4d a0 : 00010100 01010000 11011101 01001101 10100
[09] { 1} 00             : 0
[10] {37} 14 50 dd 4d a0 : 00010100 01010000 11011101 01001101 10100
[11] { 1} 00             : 0
[12] {37} 14 50 dd 4d a0 : 00010100 01010000 11011101 01001101 10100
[13] { 0}                :
*** Saving signal to file g346_433.92M_250k.cu8 (587269 samples, 1179648 bytes)
</code></pre>

Now with __channel 3__, to support the correct channel decoding (_wrong_ in the current ../01/README.md)...

__GT-WT02 - Battery-OK, Button-PRESSED, Channel 3, 23,9 °C, 33%__

<pre><code>
*** signal_start = 3539116, signal_end = 3790344, signal_len = 251228, pulses_found = 240
Iteration 1. t: 141    min: 140 (22)    max: 142 (218)    delta 4
Iteration 2. t: 141    min: 140 (2)    max: 142 (238)    delta 0
Distance coding: Pulse length 141

Short distance: 514, long distance: 1024, packet distance: 2216

p_limit: 141
bitbuffer:: Number of rows: 14
[00] { 0}                :
[01] {37} 14 60 ef 43 70 : 00010100 01100000 11101111 01000011 01110
[02] { 0}                :
[03] { 0}                :
[04] {37} 14 60 ef 43 70 : 00010100 01100000 11101111 01000011 01110
[05] { 1} 00             : 0
[06] {37} 14 60 ef 43 70 : 00010100 01100000 11101111 01000011 01110
[07] { 1} 00             : 0
[08] {37} 14 60 ef 43 70 : 00010100 01100000 11101111 01000011 01110
[09] { 1} 00             : 0
[10] {37} 14 60 ef 43 70 : 00010100 01100000 11101111 01000011 01110
[11] { 1} 00             : 0
[12] {37} 14 60 ef 43 70 : 00010100 01100000 11101111 01000011 01110
[13] { 0}                :
Signal bigger than buffer, signal = 3276800 > buffer 3145728 !!
*** Saving signal to file g368_433.92M_250k.cu8 (1620127 samples, 3145728 bytes)
</code></pre>

And finally some sample from inside the __fridge__ ;-). Humidity is lower than the supported range (code 10=="LL")...

__GT-WT02 - Battery-OK, No-Button, Channel 3, -12,7 °C, 10%-???-Display shows "LL"__

<pre><code>
*** signal_start = 230986483, signal_end = 231221803, signal_len = 235320, pulses_found = 240
Iteration 1. t: 124    min: 123 (22)    max: 126 (218)    delta 13
Iteration 2. t: 124    min: 122 (6)    max: 126 (234)    delta 1
Iteration 3. t: 124    min: 122 (6)    max: 126 (234)    delta 0
Distance coding: Pulse length 124

Short distance: 520, long distance: 1029, packet distance: 2257

p_limit: 124
bitbuffer:: Number of rows: 13
[00] { 0}                :
[01] {37} 14 2f 81 15 20 : 00010100 00101111 10000001 00010101 00100
[02] { 1} 00             : 0
[03] {37} 14 2f 81 15 20 : 00010100 00101111 10000001 00010101 00100
[04] { 1} 00             : 0
[05] {37} 14 2f 81 15 20 : 00010100 00101111 10000001 00010101 00100
[06] { 1} 00             : 0
[07] {37} 14 2f 81 15 20 : 00010100 00101111 10000001 00010101 00100
[08] { 1} 00             : 0
[09] {37} 14 2f 81 15 20 : 00010100 00101111 10000001 00010101 00100
[10] { 1} 00             : 0
[11] {37} 14 2f 81 15 20 : 00010100 00101111 10000001 00010101 00100
[12] { 0}                :
*** Saving signal to file g573_433.92M_250k.cu8 (250591 samples, 524288 bytes)
</code></pre>
