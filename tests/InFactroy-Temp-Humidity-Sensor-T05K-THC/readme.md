# InFactroy Temperature & Humidity Sensor

// Photos

This InFactory branded sensor comes with several Wheather Stations sold by Pearl (pearl.fr or pearl.de). This looks like generic chinese made products.
- Page where you can buy an additionnal sensor (this is what I bought) : https://www.pearl.fr/article/NC3981/station-meteo-radiopilotee-avec-capteur-exterieur-et-ecran-couleur-portrait
- Supported Weather Stations : https://www.pearl.fr/article/NC3981/station-meteo-radiopilotee-avec-capteur-exterieur-et-ecran-couleur-portrait & https://www.pearl.fr/article/PV8796/station-meteo-radiopilotee-avec-capteur-exterieur-et-ecran-led-couleur
- FCC Radio Certification documents (you can get the manual, pictures ...) : https://fccid.io/WEC-1502 (the certified version is the TXC, which only seems to have temperature sensor, not humidity)

Note that I do NOT have the weather base station, and the sensor do NOT have any kind of lcd screen to get the current Temp/Humidity 

##My initial findings

Sensor is transmiting 5 bytes with PWM OOK encoding + a few 0000 for preamb. Those 5 bytes are transmitted 6 times, every minute.
The PWM values looks the same as Esperanza EWS and Oregon, so RTL_433 tries to decode the frame using those decoders, but without success.

##Frame Structure

Not a lot of answers here, I need help ;-)

IIIIIIII ???????? ???????? ???????? ?????NNN

I = Sensor ID. Resets to a new value after battery is removed.
N = Those 3 bits never ever changed

##Datas

I grabbed the following datas. Notice that I think that there is a glitch in my RTL_433 setup, as a -A (bellow) shows empty frame. May be the same for my *.data files.

```
*** signal_start = 1436510, signal_end = 1718418
signal_len = 281908,  pulses = 276
Iteration 1. t: 200    min: 143 (253)    max: 258 (23)    delta 17
Iteration 2. t: 200    min: 143 (253)    max: 258 (23)    delta 0
Distance coding: Pulse length 200

Short distance: 710, long distance: 2003, packet distance: 4004

p_limit: 200
bitbuffer:: Number of rows: 6
[00] {45} 08 00 00 00 00 00 : 00001000 00000000 00000000 00000000 00000000 00000
[01] {45} 08 00 00 00 00 00 : 00001000 00000000 00000000 00000000 00000000 00000
[02] {45} 08 00 00 00 00 00 : 00001000 00000000 00000000 00000000 00000000 00000
[03] {45} 08 00 00 00 00 00 : 00001000 00000000 00000000 00000000 00000000 00000
[04] {45} 08 00 00 00 00 00 : 00001000 00000000 00000000 00000000 00000000 00000
[05] {45} 08 00 00 00 00 00 : 00001000 00000000 00000000 00000000 00000000 00000
```

But if I use -D, I am getting the frame !

```
Detected OOK package
pulse_demod_ppm(): Esperanza EWS
bitbuffer:: Number of rows: 2
[00] {4} 00 : 0000
[01] {40} 56 31 6d 92 61 : 01010110 00110001 01101101 10010010 01100001
pulse_demod_ppm(): Oregon Scientific SL109H Remote Thermal Hygro Sensor
bitbuffer:: Number of rows: 2
[00] {4} 00 : 0000
[01] {40} 56 31 6d 92 61 : 01010110 00110001 01101101 10010010 01100001
RH ASK preamble not found
RH ASK preamble not found
Analyzing pulses...
Total count:   46,  width: 39146                (156.6 ms)
Pulse width distribution:
 [ 0] count:    4,  width:   257 [257;258]      (1028 us)
 [ 1] count:   42,  width:   143 [141;153]      ( 572 us)
Gap width distribution:
 [ 0] count:    4,  width:   253 [253;254]      (1012 us)
 [ 1] count:    1,  width:  1997 [1997;1997]    (7988 us)
 [ 2] count:   22,  width:   485 [468;502]      (1940 us)
 [ 3] count:   18,  width:  1022 [988;1045]     (4088 us)
Pulse period distribution:
 [ 0] count:   26,  width:   611 [511;646]      (2444 us)
 [ 1] count:    1,  width:  2148 [2148;2148]    (8592 us)
 [ 2] count:   18,  width:  1164 [1134;1186]    (4656 us)
Level estimates [high, low]:  16087,     58
Frequency offsets [F1, F2]:    6157,      0     (+23.5 kHz, +0.0 kHz)
Guessing modulation: No clue...
```

Some datas.

```
<At home. Temp around 23C, Humidity around 30%. I may have blowed on the sensor at some time to have some value change>

[01] {40} 2d 70 6b 92 91 : 00101101 01110000 01101011 10010010 10010001
[01] {40} 2d c0 6b b2 81 : 00101101 11000000 01101011 10110010 10000001
[01] {40} 2d 61 6d 13 71 : 00101101 01100001 01101101 00010011 01110001
[01] {40} 2d 71 6d 84 41 : 00101101 01110001 01101101 10000100 01000001
[01] {40} 2d d2 6d 43 41 : 00101101 11010010 01101101 01000011 01000001
[01] {40} 2d 82 6c c3 01 : 00101101 10000010 01101100 11000011 00000001
[01] {40} 2d 22 6c c2 91 : 00101101 00100010 01101100 11000010 10010001

<Battery removed>

[01] {40} ab 60 6c a3 11 : 10101011 01100000 01101100 10100011 00010001
[01] {40} ab e0 6c c2 71 : 10101011 11100000 01101100 11000010 01110001
[01] {40} ab f0 6c 72 71 : 10101011 11110000 01101100 01110010 01110001
[01] {40} ab f2 6b 82 61 : 10101011 11110010 01101011 10000010 01100001
[01] {40} ab e2 6b 32 61 : 10101011 11100010 01101011 00110010 01100001

<Battery removed>

[01] {40} d0 a0 6b 32 71 : 11010000 10100000 01101011 00110010 01110001
[01] {40} d0 10 6b 12 61 : 11010000 00010000 01101011 00010010 01100001
[01] {40} d0 20 6b 12 51 : 11010000 00100000 01101011 00010010 01010001

<Battery removed + Placed the sensor in a very warm & wet environnement - T > 60C, H > 80%)

[00] {40} 5d 42 68 42 71 : 01011101 01000010 01101000 01000010 01110001
[00] {40} 5d c2 68 02 81 : 01011101 11000010 01101000 00000010 10000001
[00] {40} 5d b2 67 e3 51 : 01011101 10110010 01100111 11100011 01010001
[01] {40} 5d 71 81 a7 31 : 01011101 01110001 10000001 10100111 00110001
[00] {40} 5d 12 87 b5 81 : 01011101 00010010 10000111 10110101 10000001
[01] {40} 5d 72 7f a7 11 : 01011101 01110010 01111111 10100111 00010001
[01] {40} 5d d2 74 a7 81 : 01011101 11010010 01110100 10100111 10000001
[00] {40} 5d 92 66 f5 71 : 01011101 10010010 01100110 11110101 01110001
[00] {40} 5d 92 66 f5 71 : 01011101 10010010 01100110 11110101 01110001
[00] {40} 5d e2 66 a5 21 : 01011101 11100010 01100110 10100101 00100001
[00] {40} 5d d2 66 a5 11 : 01011101 11010010 01100110 10100101 00010001
[00] {40} 5d 62 66 a4 91 : 01011101 01100010 01100110 10100100 10010001
[00] {40} 5d 72 66 a4 81 : 01011101 01110010 01100110 10100100 10000001

<Battery removed>

[00] {40} 91 e0 68 43 41 : 10010001 11100000 01101000 01000011 01000001
[00] {40} 91 a0 68 53 51 : 10010001 10100000 01101000 01010011 01010001
[00] {40} 91 80 68 03 51 : 10010001 10000000 01101000 00000011 01010001
```
