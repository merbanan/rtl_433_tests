# Elro Wireless Chime DB286A

Manufacturer product page: http://www.elro.eu/en/produkte/cat/tuerklingeln/kabellose-tuerklingeln/batterien1/kabellose-tuerklingel3

Attached are pictures of the sending part.
Signal logs captured a single door bell signal, the sending unit sends one signal per button press consisting of a leading zero pulse, followed by 15 repetitions of the same pulse pattern identifying the unit. The last repetition lacks the trailing zero pulse.

Both captures originated from a single unit, which seems to switch between the two pulse patterns on every button press.

```
*** signal_start = 2444431, signal_end = 2731893
signal_len = 287462,  pulses = 495
Iteration 1. t: 239    min: 115 (285)    max: 363 (210)    delta 41
Iteration 2. t: 239    min: 115 (285)    max: 363 (210)    delta 0
Pulse coding: Short pulse length 115 - Long pulse length 363

Short distance: 135, long distance: 383, packet distance: 1753

p_limit: 239
bitbuffer:: Number of rows: 16
[00] {1} 00 : 0
[01] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[02] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[03] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[04] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[05] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[06] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[07] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[08] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[09] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[10] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[11] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[12] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[13] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[14] {33} c8 09 d5 93 00 : 11001000 00001001 11010101 10010011 0
[15] {32} c8 09 d5 93 : 11001000 00001001 11010101 10010011
signal_bszie = 655360  -      sg_index = 2621440
start_pos    = 1662696  -   buffer_size = 3145728
*** Saving signal to file gfile001.data
*** Writing data from 1662696, len 655360
```

```
*** signal_start = 10805733, signal_end = 11092701
signal_len = 286968,  pulses = 495
Iteration 1. t: 246    min: 122 (255)    max: 370 (240)    delta 50
Iteration 2. t: 246    min: 122 (255)    max: 370 (240)    delta 0
Pulse coding: Short pulse length 122 - Long pulse length 370

Short distance: 127, long distance: 375, packet distance: 1741

p_limit: 246
bitbuffer:: Number of rows: 16 
[00] {1} 00 : 0
[01] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[02] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[03] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[04] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[05] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[06] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[07] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[08] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[09] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[10] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[11] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[12] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[13] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[14] {33} 99 47 85 d3 00 : 10011001 01000111 10000101 11010011 0
[15] {32} 99 47 85 d3 : 10011001 01000111 10000101 11010011 
signal_bszie = 655360  -      sg_index = 262144
start_pos    = -490056  -   buffer_size = 3145728
restart_pos = 2655672
*** Saving signal to file gfile002.data
*** Writing data from 2655672, len 490056
*** Writing data from 0, len 165304
```
