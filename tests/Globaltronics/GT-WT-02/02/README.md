# Globaltronics (GT) WT-01

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
 [ 1] count:  176,  width:  500 us  <- PPM
Gap width distribution:
 [ 1] count:   80,  width: 2136 us  <- Short
 [ 2] count:   86,  width: 4180 us  <- Long
 [ 3] count:    9,  width: 9104 us  <- Sync

__GT-WT01, Battery-Low, Channel 1, 3,8 °C, 63%:__

<pre><code>
bitbuffer:: Number of rows: 10
[00] {14} 3f d4          : 00111111 110101
[01] { 1} 00             : 0
[02] {37} d3 80 26 7f a8 : 11010011 10000000 00100110 01111111 10101
[03] { 1} 00             : 0
[04] {37} d3 80 26 7f a8 : 11010011 10000000 00100110 01111111 10101
[05] { 1} 00             : 0
[06] {37} d3 80 26 7f a8 : 11010011 10000000 00100110 01111111 10101
[07] { 1} 00             : 0
[08] {37} d3 80 26 7f a8 : 11010011 10000000 00100110 01111111 10101
[09] { 0}                :
*** Saving signal to file g170_433.92M_250k.cu8 (212062 samples, 524288 bytes)
</code></pre>


__Battery-Low, Channel 1, 3,3 °C, 66%:__

<pre><code>
bitbuffer:: Number of rows: 13
[00] { 0}                :
[01] {37} d3 80 21 85 38 : 11010011 10000000 00100001 10000101 00111
[02] { 1} 00             : 0
[03] {37} d3 80 21 85 38 : 11010011 10000000 00100001 10000101 00111
[04] { 1} 00             : 0
[05] {37} d3 80 21 85 38 : 11010011 10000000 00100001 10000101 00111
[06] { 1} 00             : 0
[07] {37} d3 80 21 85 38 : 11010011 10000000 00100001 10000101 00111
[08] { 1} 00             : 0
[09] {37} d3 80 21 85 38 : 11010011 10000000 00100001 10000101 00111
[10] { 1} 00             : 0
[11] {37} d3 80 21 85 38 : 11010011 10000000 00100001 10000101 00111
[12] { 0}                :
*** Saving signal to file g269_433.92M_250k.cu8 (387410 samples, 786432 bytes)
</code></pre>

__Battery-Low, Channel 1, 3,1 °C, 66%:__

<pre><code>
bitbuffer:: Number of rows: 13
[00] { 0}                :
[01] {37} d3 80 1f 85 a0 : 11010011 10000000 00011111 10000101 10100
[02] { 1} 00             : 0
[03] {37} d3 80 1f 85 a0 : 11010011 10000000 00011111 10000101 10100
[04] { 1} 00             : 0
[05] {37} d3 80 1f 85 a0 : 11010011 10000000 00011111 10000101 10100
[06] { 1} 00             : 0
[07] {37} d3 80 1f 85 a0 : 11010011 10000000 00011111 10000101 10100
[08] { 1} 00             : 0
[09] {37} d3 80 1f 85 a0 : 11010011 10000000 00011111 10000101 10100
[10] { 1} 00             : 0
[11] {37} d3 80 1f 85 a0 : 11010011 10000000 00011111 10000101 10100
[12] { 0}                :
*** Saving signal to file g299_433.92M_250k.cu8 (262975 samples, 655360 bytes)
</code></pre>
