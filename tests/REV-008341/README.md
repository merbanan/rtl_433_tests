# REV Model Number : 008341

gfile001.data
gfile002.data A/1/OFF
gfile003.data A/1/ON
gfile004.data A/2/OFF
gfile005.data A/2/ON
gfile006.data A/3/OFF
gfile007.data A/3/ON
gfile008.data B/1/OFF
gfile009.data B/1/ON
gfile010.data missfire on B/2/OFF
gfile011.data B/2/OFF
gfile012.data B/2/ON
gfile013.data B/3/OFF
gfile014.data B/3/ON
gfile015.data C/1/OFF
gfile016.data C/1/ON
gfile017.data C/2/OFF
gfile018.data C/2/ON
gfile019.data C/3/OFF
gfile020.data C/3/ON
gfile021.data D/1/OFF
gfile022.data D/1/ON
gfile023.data missfire on D/2/OFF
gfile024.data D/2/OFF
gfile025.data D/2/ON
gfile026.data D/3/OFF
gfile027.data D/3/ON 

files are encoded as follows;
 [A | B | C | D] channel
 [1 | 2 | 3 ]    row
 [OFF | ON ]     switch 

[jmb@gryhlo 01]$ rtl_433 -a -t 
Registering protocol [1] "Rubicson Temperature Sensor"
Registering protocol [2] "Prologue Temperature Sensor"
Registering protocol [3] "Waveman Switch Transmitter"
Registering protocol [4] "LaCrosse TX Temperature / Humidity Sensor"
Registering protocol [5] "Acurite 609TXC Temperature and Humidity Sensor"
Registering protocol [6] "Oregon Scientific Weather Sensor"
Registering protocol [7] "Mebus 433"
Registering protocol [8] "KlikAanKlikUit Wireless Switch"
Registering protocol [9] "AlectoV1 Weather Sensor (Alecto WS3500 WS4500 Ventus W155/W044 Oregon)"
Registering protocol [10] "Fine Offset Electronics, WH2 Temperature/Humidity Sensor"
Registering protocol [11] "Nexus Temperature & Humidity Sensor"
Registering protocol [12] "Ambient Weather Temperature Sensor"
Registering protocol [13] "Calibeur RF-104 Sensor"
Registering protocol [14] "Danfoss CFR Thermostat"
Registering protocol [15] "Chuango Security Technology"
Registering protocol [16] "Generic Remote SC226x EV1527"
Registering protocol [17] "TFA-Twin-Plus-30.3049 and Ea2 BL999"
Registering protocol [18] "Fine Offset WH1080 Weather Station"
Registering protocol [19] "WT450"
Registering protocol [20] "LaCrosse WS-2310 Weather Station"
Registering protocol [21] "Esperanza EWS"
Registering protocol [22] "Generic temperature sensor 1"
Registering protocol [23] "WG-PB12V1"
Registering protocol [24] "HIDEKI TS04 Temperature, Humidity, Wind and Rain Sensor"
Registering protocol [25] "Watchman Sonic / Apollo Ultrasonic / Beckett Rocket oil tank monitor"
Registering protocol [26] "CurrentCost Current Sensor"
Registering protocol [27] "emonTx OpenEnergyMonitor"
Registering protocol [28] "HT680 Remote control"
Registering protocol [29] "S3318P Temperature & Humidity Sensor"
Registering protocol [30] "Akhan 100F14 remote keyless entry"
Registering protocol [31] "Quhwa"
Registering protocol [32] "OSv1 Temperature Sensor"
Registering protocol [33] "Proove"
Registering protocol [34] "Bresser Thermo-/Hygro-Sensor 3CH"
Registering protocol [35] "Springfield Temperature and Soil Moisture"
Registering protocol [36] "Oregon Scientific SL109H Remote Thermal Hygro Sensor"
Registering protocol [37] "Acurite 606TX Temperature Sensor"
Registering protocol [38] "TFA pool temperature sensor"
Registering protocol [39] "Kedsum Temperature & Humidity Sensor"
Registering protocol [40] "blyss DC5-UK-WH (433.92 MHz)"
Registering protocol [41] "Steelmate TPMS"
Registering protocol [42] "Schraeder TPMS"
Registering protocol [43] "Elro DB286A Doorbell"
Registering protocol [44] "Efergy Optical"
Registering protocol [45] "Honda Car Key"
Registering protocol [46] "Fine Offset Electronics, XC0400"
Registering protocol [47] "Radiohead ASK"
Registering protocol [48] "Kerui PIR Sensor"
Registering protocol [49] "Fine Offset WH1050 Weather Station"
Registering protocol [50] "Honeywell Door/Window Sensor"
Registering protocol [51] "Maverick ET-732/733 BBQ Sensor"
Registering protocol [52] "LaCrosse TX141TH-Bv2 sensor"
Registering protocol [53] "Acurite 00275rm,00276rm Temp/Humidity with optional probe"
Registering protocol [54] "LaCrosse TX35DTH-IT Temperature sensor"
Registering protocol [55] "LaCrosse TX29IT Temperature sensor"
Registering protocol [56] "Fine Offset Electronics, WH25 Temperature/Humidity/Pressure Sensor"
Registering protocol [57] "Fine Offset Electronics, WH0530 Temperature/Rain Sensor"
Registered 57 out of 78 device decoding protocols
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Terratec T Stick PLUS
Detached kernel driver
Found Elonics E4000 tuner
Exact sample rate is: 250000.000414 Hz
Sample rate set to 250000.
Bit detection level set to 0 (Auto).
Tuner gain set to Auto.
Reading samples in async mode...
Tuned to 433920000 Hz.
*** signal_start = 19666722, signal_end = 19709526
signal_len = 42804,  pulses = 3
Iteration 1. t: 7    min: 5 (2)    max: 9 (1)    delta 0
Distance coding: Pulse length 7

Short distance: 86, long distance: 86, packet distance: 22698

p_limit: 7
bitbuffer:: Number of rows: 2 
[00] {0} : 
[01] {0} : 
signal_bszie = 131072  -      sg_index = 1835008
start_pos    = 1539242  -   buffer_size = 3145728
*** Saving signal to file gfile001.data
*** Writing data from 1539242, len 131072
*** signal_start = 19740532, signal_end = 19760582
signal_len = 20050,  pulses = 2
Iteration 1. t: 9    min: 0 (0)    max: 19 (2)    delta 162
Iteration 2. t: 9    min: 0 (0)    max: 19 (2)    delta 0
Distance coding: Pulse length 9

Short distance: 30, long distance: 0, packet distance: 30

p_limit: 9
bitbuffer:: Number of rows: 2 
[00] {0} : 
[01] {0} : 
signal_bszie = 131072  -      sg_index = 2097152
start_pos    = 1641354  -   buffer_size = 3145728
*** Saving signal to file gfile002.data
*** Writing data from 1641354, len 131072
*** signal_start = 23055719, signal_end = 23187603
signal_len = 131884,  pulses = 250
Iteration 1. t: 167    min: 77 (142)    max: 258 (108)    delta 1300
Iteration 2. t: 167    min: 77 (142)    max: 258 (108)    delta 0
Pulse coding: Short pulse length 77 - Long pulse length 258

Short distance: 101, long distance: 280, packet distance: 2779

p_limit: 167
bitbuffer:: Number of rows: 10 
[00] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[01] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[02] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[03] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[04] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[05] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[06] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[07] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[08] {25} d5 d4 0c 00 : 11010101 11010100 00001100 0
[09] {25} d5 d4 00 00 : 11010101 11010100 00000000 0
signal_bszie = 393216  -      sg_index = 2621440
start_pos    = 1941796  -   buffer_size = 3145728
*** Saving signal to file gfile003.data
*** Writing data from 1941796, len 393216
*** signal_start = 25953818, signal_end = 26085650
signal_len = 131832,  pulses = 250
Iteration 1. t: 165    min: 75 (143)    max: 256 (107)    delta 820
Iteration 2. t: 165    min: 75 (143)    max: 256 (107)    delta 0
Pulse coding: Short pulse length 75 - Long pulse length 256

Short distance: 102, long distance: 281, packet distance: 2783

p_limit: 165
bitbuffer:: Number of rows: 10 
[00] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[01] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[02] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[03] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[04] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[05] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[06] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[07] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[08] {25} d5 74 03 00 : 11010101 01110100 00000011 0
[09] {25} d5 54 00 00 : 11010101 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 2097152
start_pos    = 1446434  -   buffer_size = 3145728
*** Saving signal to file gfile004.data
*** Writing data from 1446434, len 393216
*** signal_start = 28964097, signal_end = 29061799
signal_len = 97702,  pulses = 175
Iteration 1. t: 173    min: 83 (98)    max: 264 (77)    delta 101
Iteration 2. t: 173    min: 83 (98)    max: 264 (77)    delta 0
Pulse coding: Short pulse length 83 - Long pulse length 264

Short distance: 95, long distance: 275, packet distance: 2781

p_limit: 173
bitbuffer:: Number of rows: 7 
[00] {25} d5 74 0c 00 : 11010101 01110100 00001100 0
[01] {25} d5 74 0c 00 : 11010101 01110100 00001100 0
[02] {25} d5 74 0c 00 : 11010101 01110100 00001100 0
[03] {25} d5 74 0c 00 : 11010101 01110100 00001100 0
[04] {25} d5 74 0c 00 : 11010101 01110100 00001100 0
[05] {25} d5 74 0c 00 : 11010101 01110100 00001100 0
[06] {25} d5 74 0c 00 : 11010101 01110100 00001100 0
signal_bszie = 262144  -      sg_index = 1835008
start_pos    = 1238348  -   buffer_size = 3145728
*** Saving signal to file gfile005.data
*** Writing data from 1238348, len 262144
*** signal_start = 30437824, signal_end = 30592491
signal_len = 154667,  pulses = 300
Iteration 1. t: 171    min: 81 (171)    max: 262 (129)    delta 776
Iteration 2. t: 171    min: 81 (171)    max: 262 (129)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 262

Short distance: 97, long distance: 276, packet distance: 2774

p_limit: 171
bitbuffer:: Number of rows: 12 
[00] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[01] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[02] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[03] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[04] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[05] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[06] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[07] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[08] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[09] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[10] {25} d5 5c 03 00 : 11010101 01011100 00000011 0
[11] {25} d5 54 00 00 : 11010101 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 1572864
start_pos    = 1022932  -   buffer_size = 3145728
*** Saving signal to file gfile006.data
*** Writing data from 1022932, len 393216
*** signal_start = 31790814, signal_end = 31945367
signal_len = 154553,  pulses = 300
Iteration 1. t: 169    min: 79 (171)    max: 260 (129)    delta 585
Iteration 2. t: 169    min: 79 (171)    max: 260 (129)    delta 0
Pulse coding: Short pulse length 79 - Long pulse length 260

Short distance: 98, long distance: 277, packet distance: 2773

p_limit: 169
bitbuffer:: Number of rows: 12 
[00] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[01] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[02] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[03] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[04] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[05] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[06] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[07] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[08] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[09] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[10] {25} d5 5c 0c 00 : 11010101 01011100 00001100 0
[11] {25} d5 54 00 00 : 11010101 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 1310720
start_pos    = 582956  -   buffer_size = 3145728
*** Saving signal to file gfile007.data
*** Writing data from 582956, len 393216
*** signal_start = 35898466, signal_end = 36064556
signal_len = 166090,  pulses = 326
Iteration 1. t: 170    min: 80 (186)    max: 261 (140)    delta 850
Iteration 2. t: 170    min: 80 (186)    max: 261 (140)    delta 0
Pulse coding: Short pulse length 80 - Long pulse length 261

Short distance: 98, long distance: 276, packet distance: 2774

p_limit: 170
bitbuffer:: Number of rows: 13 
[00] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[01] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[02] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[03] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[04] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[05] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[06] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[07] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[08] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[09] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[10] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[11] {25} 75 d4 03 00 : 01110101 11010100 00000011 0
[12] {26} 75 8a 00 00 : 01110101 10001010 00000000 00
signal_bszie = 393216  -      sg_index = 0
start_pos    = 2529878  -   buffer_size = 3145728
*** Saving signal to file gfile008.data
*** Writing data from 2529878, len 393216
*** signal_start = 37699523, signal_end = 37831257
signal_len = 131734,  pulses = 250
Iteration 1. t: 168    min: 78 (143)    max: 259 (107)    delta 650
Iteration 2. t: 168    min: 78 (143)    max: 259 (107)    delta 0
Pulse coding: Short pulse length 78 - Long pulse length 259

Short distance: 99, long distance: 278, packet distance: 2777

p_limit: 168
bitbuffer:: Number of rows: 10 
[00] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[01] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[02] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[03] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[04] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[05] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[06] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[07] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[08] {25} 75 d4 0c 00 : 01110101 11010100 00001100 0
[09] {25} 75 54 00 00 : 01110101 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 262144
start_pos    = -228176  -   buffer_size = 3145728
restart_pos = 2917552
*** Saving signal to file gfile009.data
*** Writing data from 2917552, len 228176
*** Writing data from 0, len 165040
*** signal_start = 39138002, signal_end = 39166743
signal_len = 28741,  pulses = 25
Iteration 1. t: 160    min: 66 (17)    max: 254 (8)    delta 305
Iteration 2. t: 160    min: 66 (17)    max: 254 (8)    delta 0
Pulse coding: Short pulse length 66 - Long pulse length 254

Short distance: 97, long distance: 116, packet distance: 293

p_limit: 160
bitbuffer:: Number of rows: 17 
[00] {1} 00 : 0
[01] {4} e0 : 1110
[02] {2} 80 : 10
[03] {2} 80 : 10
[04] {2} 80 : 10
[05] {2} 80 : 10
[06] {2} 80 : 10
[07] {1} 00 : 0
[08] {1} 00 : 0
[09] {1} 00 : 0
[10] {1} 00 : 0
[11] {1} 00 : 0
[12] {1} 00 : 0
[13] {1} 00 : 0
[14] {1} 00 : 0
[15] {1} 00 : 0
[16] {1} 00 : 0
signal_bszie = 131072  -      sg_index = 0
start_pos    = 2704940  -   buffer_size = 3145728
*** Saving signal to file gfile010.data
*** Writing data from 2704940, len 131072
*** signal_start = 40915405, signal_end = 41047258
signal_len = 131853,  pulses = 250
Iteration 1. t: 171    min: 81 (143)    max: 262 (107)    delta 776
Iteration 2. t: 171    min: 81 (143)    max: 262 (107)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 262

Short distance: 96, long distance: 276, packet distance: 2776

p_limit: 171
bitbuffer:: Number of rows: 10 
[00] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[01] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[02] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[03] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[04] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[05] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[06] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[07] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[08] {25} 75 74 03 00 : 01110101 01110100 00000011 0
[09] {25} 75 54 00 00 : 01110101 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 524288
start_pos    = -87630  -   buffer_size = 3145728
restart_pos = 3058098
*** Saving signal to file gfile011.data
*** Writing data from 3058098, len 87630
*** Writing data from 0, len 305586
*** signal_start = 42894715, signal_end = 43060779
signal_len = 166064,  pulses = 325
Iteration 1. t: 172    min: 82 (182)    max: 262 (143)    delta 101
Iteration 2. t: 172    min: 82 (182)    max: 262 (143)    delta 0
Pulse coding: Short pulse length 82 - Long pulse length 262

Short distance: 96, long distance: 274, packet distance: 2770

p_limit: 172
bitbuffer:: Number of rows: 13 
[00] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[01] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[02] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[03] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[04] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[05] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[06] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[07] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[08] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[09] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[10] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[11] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
[12] {25} 75 74 0c 00 : 01110101 01110100 00001100 0
signal_bszie = 393216  -      sg_index = 1310720
start_pos    = 793684  -   buffer_size = 3145728
*** Saving signal to file gfile012.data
*** Writing data from 793684, len 393216
*** signal_start = 44941352, signal_end = 45073310
signal_len = 131958,  pulses = 250
Iteration 1. t: 173    min: 83 (142)    max: 264 (108)    delta 725
Iteration 2. t: 173    min: 83 (142)    max: 264 (108)    delta 0
Pulse coding: Short pulse length 83 - Long pulse length 264

Short distance: 95, long distance: 275, packet distance: 2776

p_limit: 173
bitbuffer:: Number of rows: 10 
[00] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[01] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[02] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[03] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[04] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[05] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[06] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[07] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[08] {25} 75 5c 03 00 : 01110101 01011100 00000011 0
[09] {25} 75 5c 00 00 : 01110101 01011100 00000000 0
signal_bszie = 393216  -      sg_index = 2359296
start_pos    = 1673018  -   buffer_size = 3145728
*** Saving signal to file gfile013.data
*** Writing data from 1673018, len 393216
*** signal_start = 46489904, signal_end = 46667122
signal_len = 177218,  pulses = 350
Iteration 1. t: 170    min: 80 (199)    max: 260 (151)    delta 628
Iteration 2. t: 170    min: 80 (199)    max: 260 (151)    delta 0
Pulse coding: Short pulse length 80 - Long pulse length 260

Short distance: 98, long distance: 276, packet distance: 2769

p_limit: 170
bitbuffer:: Number of rows: 14 
[00] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[01] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[02] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[03] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[04] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[05] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[06] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[07] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[08] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[09] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[10] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[11] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[12] {25} 75 5c 0c 00 : 01110101 01011100 00001100 0
[13] {25} 75 54 00 00 : 01110101 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 2359296
start_pos    = 1714914  -   buffer_size = 3145728
*** Saving signal to file gfile014.data
*** Writing data from 1714914, len 393216
*** signal_start = 53844046, signal_end = 53975975
signal_len = 131929,  pulses = 250
Iteration 1. t: 171    min: 81 (142)    max: 262 (108)    delta 725
Iteration 2. t: 171    min: 81 (142)    max: 262 (108)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 262

Short distance: 96, long distance: 276, packet distance: 2778

p_limit: 171
bitbuffer:: Number of rows: 10 
[00] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[01] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[02] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[03] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[04] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[05] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[06] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[07] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[08] {25} 5d d4 03 00 : 01011101 11010100 00000011 0
[09] {25} 5d d4 00 00 : 01011101 11010100 00000000 0
signal_bszie = 393216  -      sg_index = 1310720
start_pos    = 603980  -   buffer_size = 3145728
*** Saving signal to file gfile015.data
*** Writing data from 603980, len 393216
*** signal_start = 55301208, signal_end = 55421715
signal_len = 120507,  pulses = 225
Iteration 1. t: 171    min: 81 (127)    max: 262 (98)    delta 865
Iteration 2. t: 171    min: 81 (127)    max: 262 (98)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 262

Short distance: 97, long distance: 276, packet distance: 2778

p_limit: 171
bitbuffer:: Number of rows: 9 
[00] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[01] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[02] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[03] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[04] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[05] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[06] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[07] {25} 5d d4 0c 00 : 01011101 11010100 00001100 0
[08] {25} 5d d4 08 00 : 01011101 11010100 00001000 0
signal_bszie = 262144  -      sg_index = 1048576
start_pos    = 480804  -   buffer_size = 3145728
*** Saving signal to file gfile016.data
*** Writing data from 480804, len 262144
*** signal_start = 56787190, signal_end = 56919027
signal_len = 131837,  pulses = 250
Iteration 1. t: 171    min: 81 (143)    max: 262 (107)    delta 928
Iteration 2. t: 171    min: 81 (143)    max: 262 (107)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 262

Short distance: 97, long distance: 276, packet distance: 2776

p_limit: 171
bitbuffer:: Number of rows: 10 
[00] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[01] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[02] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[03] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[04] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[05] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[06] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[07] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[08] {25} 5d 74 03 00 : 01011101 01110100 00000011 0
[09] {25} 5d 54 00 00 : 01011101 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 786432
start_pos    = 198628  -   buffer_size = 3145728
*** Saving signal to file gfile017.data
*** Writing data from 198628, len 393216
*** signal_start = 57851790, signal_end = 57960837
signal_len = 109047,  pulses = 200
Iteration 1. t: 172    min: 81 (114)    max: 263 (86)    delta 725
Iteration 2. t: 172    min: 81 (114)    max: 263 (86)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 263

Short distance: 96, long distance: 276, packet distance: 2779

p_limit: 172
bitbuffer:: Number of rows: 8 
[00] {25} 5d 74 0c 00 : 01011101 01110100 00001100 0
[01] {25} 5d 74 0c 00 : 01011101 01110100 00001100 0
[02] {25} 5d 74 0c 00 : 01011101 01110100 00001100 0
[03] {25} 5d 74 0c 00 : 01011101 01110100 00001100 0
[04] {25} 5d 74 0c 00 : 01011101 01110100 00001100 0
[05] {25} 5d 74 0c 00 : 01011101 01110100 00001100 0
[06] {25} 5d 74 0c 00 : 01011101 01110100 00001100 0
[07] {25} 5d 74 00 00 : 01011101 01110100 00000000 0
signal_bszie = 262144  -      sg_index = 2883584
start_pos    = 2413320  -   buffer_size = 3145728
*** Saving signal to file gfile018.data
*** Writing data from 2413320, len 262144
*** signal_start = 59018410, signal_end = 59127564
signal_len = 109154,  pulses = 200
Iteration 1. t: 174    min: 84 (112)    max: 264 (88)    delta 109
Iteration 2. t: 174    min: 84 (112)    max: 264 (88)    delta 0
Pulse coding: Short pulse length 84 - Long pulse length 264

Short distance: 95, long distance: 274, packet distance: 2779

p_limit: 174
bitbuffer:: Number of rows: 8 
[00] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
[01] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
[02] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
[03] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
[04] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
[05] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
[06] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
[07] {25} 5d 5c 03 00 : 01011101 01011100 00000011 0
signal_bszie = 262144  -      sg_index = 2097152
start_pos    = 1601046  -   buffer_size = 3145728
*** Saving signal to file gfile019.data
*** Writing data from 1601046, len 262144
*** signal_start = 60232826, signal_end = 60353149
signal_len = 120323,  pulses = 225
Iteration 1. t: 169    min: 79 (129)    max: 260 (96)    delta 584
Iteration 2. t: 169    min: 79 (129)    max: 260 (96)    delta 0
Pulse coding: Short pulse length 79 - Long pulse length 260

Short distance: 98, long distance: 277, packet distance: 2778

p_limit: 169
bitbuffer:: Number of rows: 9 
[00] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[01] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[02] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[03] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[04] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[05] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[06] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[07] {25} 5d 5c 0c 00 : 01011101 01011100 00001100 0
[08] {25} 5d 54 00 00 : 01011101 01010100 00000000 0
signal_bszie = 262144  -      sg_index = 1310720
start_pos    = 906488  -   buffer_size = 3145728
*** Saving signal to file gfile020.data
*** Writing data from 906488, len 262144
*** signal_start = 62192805, signal_end = 62324759
signal_len = 131954,  pulses = 250
Iteration 1. t: 171    min: 81 (142)    max: 262 (108)    delta 1061
Iteration 2. t: 171    min: 81 (142)    max: 262 (108)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 262

Short distance: 97, long distance: 276, packet distance: 2778

p_limit: 171
bitbuffer:: Number of rows: 10 
[00] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[01] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[02] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[03] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[04] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[05] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[06] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[07] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[08] {25} 57 d4 03 00 : 01010111 11010100 00000011 0
[09] {25} 57 d4 00 00 : 01010111 11010100 00000000 0
signal_bszie = 393216  -      sg_index = 2097152
start_pos    = 1572908  -   buffer_size = 3145728
*** Saving signal to file gfile021.data
*** Writing data from 1572908, len 393216
*** signal_start = 63251455, signal_end = 63360386
signal_len = 108931,  pulses = 200
Iteration 1. t: 169    min: 79 (115)    max: 260 (85)    delta 820
Iteration 2. t: 169    min: 79 (115)    max: 260 (85)    delta 0
Pulse coding: Short pulse length 79 - Long pulse length 260

Short distance: 99, long distance: 278, packet distance: 2781

p_limit: 169
bitbuffer:: Number of rows: 8 
[00] {25} 57 d4 0c 00 : 01010111 11010100 00001100 0
[01] {25} 57 d4 0c 00 : 01010111 11010100 00001100 0
[02] {25} 57 d4 0c 00 : 01010111 11010100 00001100 0
[03] {25} 57 d4 0c 00 : 01010111 11010100 00001100 0
[04] {25} 57 d4 0c 00 : 01010111 11010100 00001100 0
[05] {25} 57 d4 0c 00 : 01010111 11010100 00001100 0
[06] {25} 57 d4 0c 00 : 01010111 11010100 00001100 0
[07] {25} 57 54 00 00 : 01010111 01010100 00000000 0
signal_bszie = 262144  -      sg_index = 1048576
start_pos    = 629506  -   buffer_size = 3145728
*** Saving signal to file gfile022.data
*** Writing data from 629506, len 262144
*** signal_start = 64625544, signal_end = 64654322
signal_len = 28778,  pulses = 25
Iteration 1. t: 169    min: 70 (16)    max: 268 (9)    delta 109
Iteration 2. t: 169    min: 70 (16)    max: 268 (9)    delta 0
Pulse coding: Short pulse length 70 - Long pulse length 268

Short distance: 97, long distance: 121, packet distance: 289

p_limit: 169
bitbuffer:: Number of rows: 16 
[00] {1} 00 : 0
[01] {2} 80 : 10
[02] {2} 80 : 10
[03] {4} e0 : 1110
[04] {4} e0 : 1110
[05] {2} 80 : 10
[06] {1} 00 : 0
[07] {1} 00 : 0
[08] {1} 00 : 0
[09] {1} 00 : 0
[10] {1} 00 : 0
[11] {1} 00 : 0
[12] {1} 00 : 0
[13] {1} 00 : 0
[14] {1} 00 : 0
[15] {1} 00 : 0
signal_bszie = 131072  -      sg_index = 524288
start_pos    = 202722  -   buffer_size = 3145728
*** Saving signal to file gfile023.data
*** Writing data from 202722, len 131072
*** signal_start = 65851649, signal_end = 65983641
signal_len = 131992,  pulses = 250
Iteration 1. t: 172    min: 82 (141)    max: 262 (109)    delta 884
Iteration 2. t: 172    min: 82 (141)    max: 262 (109)    delta 0
Pulse coding: Short pulse length 82 - Long pulse length 262

Short distance: 97, long distance: 275, packet distance: 2778

p_limit: 172
bitbuffer:: Number of rows: 10 
[00] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[01] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[02] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[03] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[04] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[05] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[06] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[07] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[08] {25} 57 74 03 00 : 01010111 01110100 00000011 0
[09] {25} 57 74 02 00 : 01010111 01110100 00000010 0
signal_bszie = 393216  -      sg_index = 0
start_pos    = 2599216  -   buffer_size = 3145728
*** Saving signal to file gfile024.data
*** Writing data from 2599216, len 393216
*** signal_start = 67958553, signal_end = 68090420
signal_len = 131867,  pulses = 250
Iteration 1. t: 171    min: 81 (142)    max: 262 (108)    delta 725
Iteration 2. t: 171    min: 81 (142)    max: 262 (108)    delta 0
Pulse coding: Short pulse length 81 - Long pulse length 262

Short distance: 97, long distance: 276, packet distance: 2775

p_limit: 171
bitbuffer:: Number of rows: 10 
[00] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[01] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[02] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[03] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[04] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[05] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[06] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[07] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[08] {25} 57 74 0c 00 : 01010111 01110100 00001100 0
[09] {25} 57 74 00 00 : 01010111 01110100 00000000 0
signal_bszie = 393216  -      sg_index = 1048576
start_pos    = 521318  -   buffer_size = 3145728
*** Saving signal to file gfile025.data
*** Writing data from 521318, len 393216
*** signal_start = 69705380, signal_end = 69848774
signal_len = 143394,  pulses = 275
Iteration 1. t: 173    min: 83 (154)    max: 263 (121)    delta 90
Iteration 2. t: 173    min: 83 (154)    max: 263 (121)    delta 0
Pulse coding: Short pulse length 83 - Long pulse length 263

Short distance: 96, long distance: 274, packet distance: 2775

p_limit: 173
bitbuffer:: Number of rows: 11 
[00] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[01] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[02] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[03] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[04] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[05] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[06] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[07] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[08] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[09] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
[10] {25} 57 5c 03 00 : 01010111 01011100 00000011 0
signal_bszie = 393216  -      sg_index = 1572864
start_pos    = 892298  -   buffer_size = 3145728
*** Saving signal to file gfile026.data
*** Writing data from 892298, len 393216
*** signal_start = 71311563, signal_end = 71466150
signal_len = 154587,  pulses = 300
Iteration 1. t: 169    min: 79 (171)    max: 260 (129)    delta 746
Iteration 2. t: 169    min: 79 (171)    max: 260 (129)    delta 0
Pulse coding: Short pulse length 79 - Long pulse length 260

Short distance: 98, long distance: 277, packet distance: 2773

p_limit: 169
bitbuffer:: Number of rows: 12 
[00] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[01] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[02] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[03] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[04] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[05] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[06] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[07] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[08] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[09] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[10] {25} 57 5c 0c 00 : 01010111 01011100 00001100 0
[11] {25} 57 54 00 00 : 01010111 01010100 00000000 0
signal_bszie = 393216  -      sg_index = 1572864
start_pos    = 981322  -   buffer_size = 3145728
*** Saving signal to file gfile027.data
*** Writing data from 981322, len 393216
^CSignal caught, exiting!

User cancel, exiting...

