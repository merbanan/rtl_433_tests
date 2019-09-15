# Lacrosse Weather Station WS-3600 with Sensor TX13

## Device Info

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

