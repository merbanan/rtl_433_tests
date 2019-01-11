Lacrosse Weather Station WS-3600 with Sensor TX13
===========================================================

Device Info
-----------
manual: https://www.heavyweather.info/new_english_us/3600pdf/WS3600uk_manual.pdf

more info in german: http://wiki.wetterstationen.info/index.php?title=LaCrosse_WS3600
	
Do note that these weather stations are often not precisely tuned to 433.9 MHz, 
you might need to start rtl_433 with a command like "rtl_433 -f 433800000".

Protocol compared to WS-2310 (lacrossews.c)
----------------------	

ASF modulation / OOK / 12 nibbles - see lacrossews.c

http://makin-things.com/articles/decoding-lacrosse-weather-sensor-rf-transmissions/ (2019: no longer online, use archive.org)

	
LaCrosse WS-2310:

* preamble/sync byte: 00001001 (0x09)
* temp_c = (msg_value_bcd - 300.0) / 10.0;
* long pulse 1464 µs
* short pulse 368 µs
* fixed gap 1336 µs
 	
WS-3600 & TX13 Sensor:

* preamble/sync byte: 00000110 (0x06)
* temp_c = (msg_value_bcd - 400.0) / 10.0;
* long pulse 1400 µs
* short pulse 300 µs
* fixed gap 1400 µs 

Example Data WS-3600
----------------------	
rtl_433 -r g014_433.8M_250k.cu8 -A

```
[...]
time      : @1.893632s   brand     : LaCrosse
model     : WS-3600      ws_id     : 6             id        : 196
Humidity  : 87
Analyzing pulses...
Total count:   52,  width: 114.82 ms            (28705 S)
Pulse width distribution:
 [ 0] count:   25,  width: 1392 us [1380;1416]  ( 348 S)
 [ 1] count:   27,  width:  296 us [288;304]    (  74 S)
Gap width distribution:
 [ 0] count:   51,  width: 1408 us [1288;1428]  ( 352 S)
Pulse period distribution:
 [ 0] count:   25,  width: 2800 us [2676;2824]  ( 700 S)
 [ 1] count:   26,  width: 1708 us [1700;1724]  ( 427 S)
Level estimates [high, low]:  15934,    186
RSSI: -0.1 dB SNR: 19.3 dB Noise: -19.4 dB
Frequency offsets [F1, F2]:  -24157,      0     (-92.2 kHz, +0.0 kHz)
Guessing modulation: Pulse Width Modulation with fixed gap
Attempting demodulation... short_width: 296, long_width: 1392, reset_limit: 1432, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_PWM,s=296,l=1392,r=1432,g=0,t=436,y=0'
pulse_demod_pwm(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {52} 06 1c 4f e8 7b 78 d0

Detected OOK package    @2.155968s
[...]
```