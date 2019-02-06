GT-WT01 is not decoded by rtl_433. Is the decoder broken or not compatible with some versions of the actual hardware?
Anyhow, here are some samples to check/improve the decoder.

<pre>
Corrections:
Bit 11+12: channel-code 00=Ch1, 01==Ch2, 10=Ch3 (not 11!)
Bit 25: belongs to the humidity (7bit in total),
Bit 32: unclear (always set to "1" in my tests???)
</pre>

So likely the right (better?) decoding:
<pre><code>
/* SENSOR: GT-WT-02 (ALDI Globaltronics..)
/*                XX              X      X (X-bits to correct?)
/* TYP AAAAAAAA BCDDEFFF FFFFFFFF gGGGGGG?xxxxx
/* BIT 00000000 01111111 11122222 2222233333333
/* BIT 12345678 90123456 78901234 5678901234567
/* 
/* TYPDescriptian
/* A = Rolling Device Code, Change after battarie
/* B = Batt 0=OK 1=LOW
/* C = Manual Send Button Pressed 0=not pressed 1=pressed
/* D = Channel 00=CH1, 01=CH2, 10=CH3
/* E = Temp 0=positiv 1=negativ
/* F = PositivTemp = 12 Bit bin2dez Temp, 
/* F = negativ Temp = 4095+1- F (12Bit bin2dez) , Factor Divid F / 10 (1Dezimal)
/* G = Humidity = 7Bit bin2dez 00-99, Display LL=10%, Display HH=110% (Range 20-90%)
/* x = checksum
</code></pre>

__GT-WT01, Battery-Low, Channel 1, 3,8 °C, 63%:__

<pre><code>
*** signal_start = -7110, signal_end = 188208, signal_len = 195318, pulses_found = 176
Iteration 1. t: 142    min: 142 (4)    max: 143 (172)    delta 4
Iteration 2. t: 12650    min: 0 (0)    max: 25301 (176)    delta 632945128
Iteration 3. t: 12650    min: 25301 (176)    max: 0 (0)    delta 1280281202
Iteration 4. t: 12650    min: 25301 (176)    max: 0 (0)    delta 0
Distance coding: Pulse length 12650

Short distance: 516, long distance: 1027, packet distance: 2259

p_limit: 12650
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
*** signal_start = 34589571, signal_end = 34831207, signal_len = 241636, pulses_found = 240
Iteration 1. t: 142    min: 141 (9)    max: 143 (231)    delta 4
Iteration 2. t: 142    min: 141 (1)    max: 143 (239)    delta 0
Distance coding: Pulse length 142

Short distance: 516, long distance: 1026, packet distance: 2257

p_limit: 142
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
*** signal_start = 32475023, signal_end = 32722728, signal_len = 247705, pulses_found = 240
Iteration 1. t: 142    min: 142 (4)    max: 143 (236)    delta 4
Iteration 2. t: 17270    min: 0 (0)    max: 34540 (240)    delta 1183173773
Iteration 3. t: 17270    min: 34540 (240)    max: 0 (0)    delta -1908944096
Iteration 4. t: 17270    min: 34540 (240)    max: 0 (0)    delta 0
Distance coding: Pulse length 17270

Short distance: 516, long distance: 1026, packet distance: 2254

p_limit: 17270
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
