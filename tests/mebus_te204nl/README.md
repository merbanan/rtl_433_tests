
These are rtl_433 -a -t samples from a Mebus TE204NL 3 channel indoor/outdoor temperature sensor, with two remote units (CH1 and CH2) transmitting.

The sensor appears to be Hideki, according to Certpedia:

  https://www.certipedia.com/certificates/50078864?locale=en

2603104000_31-E0204.pdf is the closest device I was wable to find what comes to manual.

´´rtl_433 -p 42 -a -t -f 433075000

Found 2 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001
  1:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Exact sample rate is: 250000.000414 Hz
Sample rate set to 250000.
Bit detection level set to 0 (Auto).
Tuner gain set to Auto.
Reading samples in async mode...
Tuned to 433075000 Hz.
*** signal_start = 6726751, signal_end = 6826943
signal_len = 100192,  pulses = 164
Iteration 1. t: 174    min: 112 (109)    max: 237 (55)    delta 8845
Iteration 2. t: 174    min: 112 (109)    max: 237 (55)    delta 0
Pulse coding: Short pulse length 112 - Long pulse length 237

Short distance: 128, long distance: 250, packet distance: 13700

p_limit: 174
bitbuffer:: Number of rows: 3
[00] {56} e2 a4 5c 22 02 50 40
[01] {55} e2 a4 5c 22 02 50 28
[02] {53} e2 a4 5d 44 04 a9 80
signal_bszie = 262144  -      sg_index = 1310720
start_pos    = 808828  -   buffer_size = 3145728
*** Saving signal to file gfile009.data
*** Writing data from 808828, len 262144
*** signal_start = 9267270, signal_end = 9367456
signal_len = 100186,  pulses = 166
Iteration 1. t: 171    min: 109 (113)    max: 234 (53)    delta 9220
Iteration 2. t: 171    min: 109 (113)    max: 234 (53)    delta 0
Pulse coding: Short pulse length 109 - Long pulse length 234

Short distance: 132, long distance: 254, packet distance: 13705

p_limit: 171
bitbuffer:: Number of rows: 3
[00] {57} e2 42 2e 24 01 48 04 00
[01] {55} e2 42 2e 24 01 4c 50
[02] {54} e2 42 2e c8 02 94 50
signal_bszie = 262144  -      sg_index = 0
start_pos    = 2744126  -   buffer_size = 3145728
*** Saving signal to file gfile010.data
*** Writing data from 2744126, len 262144´´


