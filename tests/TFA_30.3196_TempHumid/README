TFA Dostmann 30.3196 T/H outdoor sensor
=======================================

https://www.tfa-dostmann.de/en/produkt/temperature-humidity-transmitter-11/
https://clientmedia.trade-server.net/1768_tfadost/media/7/86/3786.pdf

The device comes with 'TFA Modus Plus' (indoor) base station.
Up to three outdoor sensors can be operated
(channel numbers 1, 2, or 3).

Some recordings:

Ch. #   Temp. [C]   Humid. [%]  Filename
-------------------------------------------------------------
3       10.6        91      g001_868.33M_250k.cu8
3       14.6        94      g002_868.33M_250k.cu8
3       16.5        93      g003_868.33M_250k.cu8
3       17.7        90      g004_868.33M_250k.cu8
3       18.6        87      g005_868.33M_250k.cu8
3       19.2        82      g006_868.33M_250k.cu8
3       19.9        75      g007_868.33M_250k.cu8

1       22.8        70      g008_868.33M_250k.cu8
1       21.8        61      g009_868.33M_250k.cu8
1       11.7        53      g010_868.33M_250k.cu8
1       9.2         58      g011_868.33M_250k.cu8
1       8.4         65      g012_868.33M_250k.cu8
1       7.0         74      g013_868.33M_250k.cu8
1       -1.2        50      g014_868.33M_250k.cu8
1       -3.1        57      g015_868.33M_250k.cu8


After some testing with a homebrewn C program it turned out
that the code is 'FSK Differential Manchester'.
I couldn't decode using rtl_433. I did the demodulation using
rtl_fm in fm mode instead and used the above mentioned C program:

(Apparently the program rtl_433 is not as sensitive as rtl_fm
since recording was only possible over shorter distances.)


Here are some findings:

- A data row consists of 64 bits (8 Bytes).

- LSB of byte is first bit sent.

- First two bytes seem to be always 0xFF.

- Third byte seems to be always 0xA8.

- Last two bytes vary strongly, maybe check sum?

- Temperature (Celsius) is found in bits 0-1 of fourth byte and
  bits 0-7 of fifth byte. ( Value = 10 * ( T + 40) )
  (Bit 0 is LSB, 7 is MSB)

- Humidity is found in bits 0-6 of sixth byte.

- Bit 7 of sixth byte seems to indicate 'low battery' if set.

- Bits 4-5 of fourth byte represent channel numbers:
  Bits 5 4 | Ch.
  --------------
       0 0 | 1
       0 1 | 2
       1 0 | 3

- At the start there is a ~ 600 us low signal (see e.g., rtl_record.wav).

- Long pulse is ~ 520 us, short pulse is ~ 240 us.

- The data row is repeated four times with ~ 720 us gaps (low signal)
  in between.

----

rtl_record.wav contains a recording which translates into the
bit pattern shown in code.out (22.6 C, 52 %) if differential
Manchester coding is assumed.
'-' indicates beginning of row, '|' is byte delimiter.

----

Analysis output of file g015_868.33M_250k.cu8:

debian 520% rtl_433 -r g015_868.33M_250k.cu8 -a -A
rtl_433 version unknown inputs file rtl_tcp RTL-SDR SoapySDR
Trying conf file at "rtl_433.conf"...
Trying conf file at "/home/user/.config/rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...
Registered 96 out of 120 device decoding protocols [ 1-4 8 11-12 15-17 19-21 23 25-26 29-36 38-60 62-64 67-71 73-100 102-103 108-116 119 ]
Test mode active. Reading samples from file: g015_868.33M_250k.cu8
Detected FSK package    @0.161832s
Analyzing pulses...
Total count:  306,  width: 296.92 ms            (74230 S)
Pulse width distribution:
 [ 0] count:   96,  width:  236 us [164;260]    (  59 S)
 [ 1] count:  208,  width:  500 us [468;516]    ( 125 S)
 [ 2] count:    1,  width:   72 us [72;72]      (  18 S)
 [ 3] count:    1,  width:    4 us [4;4]        (   1 S)
Gap width distribution:
 [ 0] count:    1,  width: 5508 us [5508;5508]  (1377 S)
 [ 1] count:  207,  width:  492 us [400;512]    ( 123 S)
 [ 2] count:   92,  width:  236 us [212;260]    (  59 S)
 [ 3] count:    3,  width: 6892 us [6892;6892]  (1723 S)
 [ 4] count:    1,  width:  388 us [388;388]    (  97 S)
 [ 5] count:    1,  width: 19120 us [19120;19120]       (4780 S)
Pulse period distribution:
 [ 0] count:    1,  width: 5672 us [5672;5672]  (1418 S)
 [ 1] count:  160,  width:  984 us [900;1012]   ( 246 S)
 [ 2] count:   96,  width:  744 us [720;768]    ( 186 S)
 [ 3] count:   44,  width:  480 us [464;500]    ( 120 S)
 [ 4] count:    3,  width: 7092 us [7092;7092]  (1773 S)
 [ 5] count:    1,  width: 19192 us [19192;19192]       (4798 S)
Level estimates [high, low]:  16006,      6
RSSI: -0.1 dB SNR: 33.6 dB Noise: -33.7 dB
Frequency offsets [F1, F2]:    5782,  -4949     (+22.1 kHz, -18.9 kHz)
Guessing modulation: No clue...

*** signal_start = 30462, signal_end = 124680, signal_len = 94218, pulses_found = 1
Distance coding: Pulse length 74217

Short distance: 1000000, long distance: 0, packet distance: 0

p_limit: 74217
bitbuffer:: Number of rows: 0 
Iteration 1. t: 0    min: 0 (0)    max: 0 (0)    delta -727379968
Iteration 2. t: 0    min: 0 (0)    max: 0 (0)    delta 0
Distance coding: Pulse length 0

Short distance: 1000000, long distance: 0, packet distance: 0

p_limit: 0
bitbuffer:: Number of rows: 0 
