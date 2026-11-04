# Globaltronics (GT) WT-02

decoding:
<pre><code>
SENSOR: GT-WT-02 (ALDI Globaltronics..)
TYP AAAAAAAA BCDDEFFF FFFFFFFF GGGGGGG xxxxxx
BIT 00000000 01111111 11122222 2222233 333333
BIT 12345678 90123456 78901234 5678901 234567

TYPE Description
A = Rolling Device Code, Change after battarie
B = Batt 0=OK 1=LOW
C = Manual Send Button Pressed 0=not pressed 1=pressed
D = Channel 00=CH1, 01=CH2, 10=CH3
E = Temp 0=positiv 1=negativ
F = PositivTemp = 12 Bit bin2dez Temp, 
F = negativ Temp = 4095+1- F (12Bit bin2dez) , Factor Divid F / 10 (1Dezimal)
G = Humidity = 7Bit bin2dez 00-99, Display LL=10%, Display HH=110% (Range 20-90%)
x = 6 bit checksum (sum width carry over all nibbles)
</code></pre>

Pulse width distribution:
 [ 0] count:  240,  width:  556 us  <- PPM
Gap width distribution:
 [ 0] count:   12,  width: 9020 us  <- Sync / Packet separation
 [ 1] count:   78,  width: 4104 us  <- Long
 [ 2] count:  149,  width: 2068 us  <- Short

__GT-WT02 - Battery-OK, No-Button, Channel 2, 21,1 °C, 31%__

<pre><code>
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
*** Saving signal to file g368_433.92M_250k.cu8 (1620127 samples, 3145728 bytes)
</code></pre>

And finally some sample from inside the __fridge__ ;-). Humidity is lower than the supported range (code 10=="LL")...

__GT-WT02 - Battery-OK, No-Button, Channel 3, -12,7 °C, 10%-???-Display shows "LL"__

<pre><code>
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
