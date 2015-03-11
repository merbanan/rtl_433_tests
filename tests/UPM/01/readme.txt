UPM website: http://www.upm-marketing.com/entry/new_index.html


WT405H is wireless temperature and humidity transmitter.
Outdoor sensor that transmits data temperature, humidity. Transmissions also include channel code and house code. The sensor transmits every 60 seconds 3 packets.


Sample Data:

-----------------------------------------------------------------------------------
House code 13, Channel code 1, Humidity LOW (maybe 14%?), Temperature 25.5

rtl_433 -r gfile001.data  -a
Test mode active. Reading samples from file: gfile001.data
Iteration 1. t: 362    min: 236 (51)    max: 489 (30)    delta 21634
Iteration 2. t: 362    min: 236 (51)    max: 489 (30)    delta 0
Pulse coding: Short pulse length 236 - Long pulse length 489

Short distance: 242, long distance: 486, packet distance: 23317

p_limit: 362

[00] {27} 25 31 43 80 : 00100101 00110001 01000011 10000000
[01] {27} 25 31 43 80 : 00100101 00110001 01000011 10000000
[02] {27} 25 31 43 80 : 00100101 00110001 01000011 10000000

Test mode file issued 2 packets
Filter coeffs used:
a: 32768 31754
b: 506 506

-----------------------------------------------------------------------------------
House code 3, Channel code 2, Humidity LOW (maybe 14%?), Temperature 25.8

rtl_433 -r gfile002.data  -a
Test mode active. Reading samples from file: gfile002.data
Iteration 1. t: 364    min: 237 (51)    max: 491 (30)    delta 23185
Iteration 2. t: 364    min: 237 (51)    max: 491 (30)    delta 0
Pulse coding: Short pulse length 237 - Long pulse length 491

Short distance: 240, long distance: 486, packet distance: 23313

p_limit: 364

[00] {27} 34 62 a0 c0 : 00110100 01100010 10100000 11000000
[01] {27} 34 62 a0 c0 : 00110100 01100010 10100000 11000000
[02] {27} 34 62 a0 c0 : 00110100 01100010 10100000 11000000

Test mode file issued 2 packets
Filter coeffs used:
a: 32768 31754
b: 506 506

-----------------------------------------------------------------------------------
House code 1, Channel code 1, Humidity LOW (maybe 14%?), Temperature 25.1

rtl_433 -r gfile003.data  -a
Test mode active. Reading samples from file: gfile003.data
Iteration 1. t: 361    min: 233 (39)    max: 489 (36)    delta 22265
Iteration 2. t: 361    min: 233 (39)    max: 489 (36)    delta 0
Pulse coding: Short pulse length 233 - Long pulse length 489

Short distance: 244, long distance: 486, packet distance: 23312

p_limit: 361

[00] {25} 3a 62 9b 00 : 00111010 01100010 10011011 00000000
[01] {25} 3a 62 9b 00 : 00111010 01100010 10011011 00000000
[02] {25} 3a 62 9b 00 : 00111010 01100010 10011011 00000000

Test mode file issued 2 packets
Filter coeffs used:
a: 32768 31754
b: 506 506

-----------------------------------------------------------------------------------