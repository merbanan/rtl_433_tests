# Fine Offset WH65b

These are samples collected from a Fine Offset WH65B sensor array with an RTL-SDR.com V3 dongle. The data sent from the Ambient Weather WS2902 console to WU is also included.

Note that the samples are incorrectly identified as being from a WH24.

## Collection
```
# rtl_433 -a -S known -R 78 -f 915000000 -F json -C customary
rtl_433 version 18.12-32-gd233adf branch master at 201812191913
Trying conf file at "rtl_433.conf"...
Trying conf file at "/root/.rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...
Registered 1 out of 120 device decoding protocols [ 78 ]
Detached kernel driver
Found Rafael Micro R820T tuner
Exact sample rate is: 250000.000414 Hz
[R82XX] PLL not locked!
Sample rate set to 250000 S/s.
Tuner gain set to Auto.
Tuned to 915.000MHz.
{"time" : "2018-12-20 08:47:19", "model" : "Fine Offset WH24", "id" : 65, "temperature_F" : 52.700, "humidity" : 64, "wind_dir_deg" : 37, "wind_speed_ms" : 7.560, "gust_speed_ms" : 8.960, "rainfall_inch" : 52.358, "uv" : 0, "uvi" : 0, "light_lux" : 6913.000, "battery" : "OK", "mic" : "CRC"}
signal_bsize = 131072  -      sg_index = 2097152
start_pos    = 1511730  -   buffer_size = 3145728
*** Saving signal to file g001_915M_250k.cu8
*** Writing data from 1511730, len 131072
{"time" : "2018-12-20 08:47:35", "model" : "Fine Offset WH24", "id" : 65, "temperature_F" : 52.700, "humidity" : 64, "wind_dir_deg" : 217, "wind_speed_ms" : 4.200, "gust_speed_ms" : 5.600, "rainfall_inch" : 52.358, "uv" : 99, "uvi" : 0, "light_lux" : 13237.000, "battery" : "OK", "mic" : "CRC"}
signal_bsize = 131072  -      sg_index = 524288
start_pos    = 74318  -   buffer_size = 3145728
*** Saving signal to file g002_915M_250k.cu8
*** Writing data from 74318, len 131072
{"time" : "2018-12-20 08:47:51", "model" : "Fine Offset WH24", "id" : 65, "temperature_F" : 52.700, "humidity" : 64, "wind_dir_deg" : 337, "wind_speed_ms" : 5.600, "gust_speed_ms" : 7.840, "rainfall_inch" : 52.358, "uv" : 99, "uvi" : 0, "light_lux" : 12307.000, "battery" : "OK", "mic" : "CRC"}
signal_bsize = 131072  -      sg_index = 2359296
start_pos    = 1782660  -   buffer_size = 3145728
*** Saving signal to file g003_915M_250k.cu8
*** Writing data from 1782660, len 131072
{"time" : "2018-12-20 08:48:07", "model" : "Fine Offset WH24", "id" : 65, "temperature_F" : 52.700, "humidity" : 64, "wind_dir_deg" : 250, "wind_speed_ms" : 4.200, "gust_speed_ms" : 8.960, "rainfall_inch" : 52.358, "uv" : 99, "uvi" : 0, "light_lux" : 13190.000, "battery" : "OK", "mic" : "CRC"}
signal_bsize = 131072  -      sg_index = 786432
start_pos    = 345982  -   buffer_size = 3145728
*** Saving signal to file g004_915M_250k.cu8
*** Writing data from 345982, len 131072
{"time" : "2018-12-20 08:48:23", "model" : "Fine Offset WH24", "id" : 65, "temperature_F" : 52.700, "humidity" : 63, "wind_dir_deg" : 247, "wind_speed_ms" : 3.920, "gust_speed_ms" : 4.480, "rainfall_inch" : 52.358, "uv" : 99, "uvi" : 0, "light_lux" : 13128.000, "battery" : "OK", "mic" : "CRC"}
signal_bsize = 131072  -      sg_index = 2621440
start_pos    = 2053554  -   buffer_size = 3145728
*** Saving signal to file g005_915M_250k.cu8
*** Writing data from 2053554, len 131072
{"time" : "2018-12-20 08:48:39", "model" : "Fine Offset WH24", "id" : 65, "temperature_F" : 52.700, "humidity" : 63, "wind_dir_deg" : 0, "wind_speed_ms" : 1.820, "gust_speed_ms" : 2.240, "rainfall_inch" : 52.358, "uv" : 0, "uvi" : 0, "light_lux" : 5487.000, "battery" : "OK", "mic" : "CRC"}
signal_bsize = 131072  -      sg_index = 1048576
start_pos    = 616142  -   buffer_size = 3145728
*** Saving signal to file g006_915M_250k.cu8
*** Writing data from 616142, len 131072
{"time" : "2018-12-20 08:48:55", "model" : "Fine Offset WH24", "id" : 65, "temperature_F" : 52.700, "humidity" : 63, "wind_dir_deg" : 348, "wind_speed_ms" : 2.660, "gust_speed_ms" : 3.360, "rainfall_inch" : 52.358, "uv" : 0, "uvi" : 0, "light_lux" : 5316.000, "battery" : "OK", "mic" : "CRC"}
signal_bsize = 131072  -      sg_index = 2883584
start_pos    = 2324484  -   buffer_size = 3145728
*** Saving signal to file g007_915M_250k.cu8
*** Writing data from 2324484, len 131072
^CSignal caught, exiting!
Reattached kernel driver
```

## WS2902 Console's Interpretation

These are the web requests to WU that correspond to each collected sample.

```
/weatherstation/updateweatherstation.php?ID=redacted&PASSWORD=redacted&indoortempf=75.9&tempf=52.7&dewptf=40.8&windchillf=52.7&indoorhumidity=33&humidity=64&windspeedmph=7.6&windgustmph=9.2&winddir=37&absbaromin=28.88&baromin=30.64&rainin=0.00&dailyrainin=0.01&weeklyrainin=0.03&monthlyrainin=2.06&yearlyrainin=-9999&solarradiation=54.56&UV=0&dateutc=2018-12-20%2014:47:31&softwaretype=AMBWeatherV3.0.3&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0

/weatherstation/updateweatherstation.php?ID=redacted&PASSWORD=redacted&indoortempf=75.9&tempf=52.7&dewptf=40.8&windchillf=52.7&indoorhumidity=33&humidity=64&windspeedmph=4.3&windgustmph=5.8&winddir=217&absbaromin=28.88&baromin=30.64&rainin=0.00&dailyrainin=0.01&weeklyrainin=0.03&monthlyrainin=2.06&yearlyrainin=-9999&solarradiation=104.48&UV=1&dateutc=2018-12-20%2014:47:39&softwaretype=AMBWeatherV3.0.3&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0

/weatherstation/updateweatherstation.php?ID=redacted&PASSWORD=redacted&indoortempf=75.9&tempf=52.7&dewptf=40.8&windchillf=52.7&indoorhumidity=33&humidity=64&windspeedmph=5.8&windgustmph=8.1&winddir=337&absbaromin=28.88&baromin=30.64&rainin=0.00&dailyrainin=0.01&weeklyrainin=0.03&monthlyrainin=2.06&yearlyrainin=-9999&solarradiation=97.13&UV=1&dateutc=2018-12-20%2014:47:50&softwaretype=AMBWeatherV3.0.3&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0

/weatherstation/updateweatherstation.php?ID=redacted&PASSWORD=redacted&indoortempf=75.9&tempf=52.7&dewptf=40.8&windchillf=52.7&indoorhumidity=33&humidity=64&windspeedmph=4.3&windgustmph=9.2&winddir=250&absbaromin=28.88&baromin=30.64&rainin=0.00&dailyrainin=0.01&weeklyrainin=0.03&monthlyrainin=2.06&yearlyrainin=-9999&solarradiation=104.10&UV=1&dateutc=2018-12-20%2014:48:6&softwaretype=AMBWeatherV3.0.3&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0

/weatherstation/updateweatherstation.php?ID=redacted&PASSWORD=redacted&indoortempf=75.9&tempf=52.7&dewptf=40.5&windchillf=52.7&indoorhumidity=33&humidity=63&windspeedmph=4.0&windgustmph=4.5&winddir=247&absbaromin=28.88&baromin=30.64&rainin=0.00&dailyrainin=0.01&weeklyrainin=0.03&monthlyrainin=2.06&yearlyrainin=-9999&solarradiation=103.61&UV=1&dateutc=2018-12-20%2014:48:22&softwaretype=AMBWeatherV3.0.3&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0

/weatherstation/updateweatherstation.php?ID=redacted&PASSWORD=redacted&indoortempf=75.9&tempf=52.7&dewptf=40.5&windchillf=52.7&indoorhumidity=33&humidity=63&windspeedmph=1.8&windgustmph=2.2&winddir=0&absbaromin=28.88&baromin=30.64&rainin=0.00&dailyrainin=0.01&weeklyrainin=0.03&monthlyrainin=2.06&yearlyrainin=-9999&solarradiation=43.31&UV=0&dateutc=2018-12-20%2014:48:39&softwaretype=AMBWeatherV3.0.3&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0

/weatherstation/updateweatherstation.php?ID=redacted&PASSWORD=redacted&indoortempf=75.9&tempf=52.7&dewptf=40.5&windchillf=52.7&indoorhumidity=33&humidity=63&windspeedmph=2.7&windgustmph=3.4&winddir=348&absbaromin=28.88&baromin=30.64&rainin=0.00&dailyrainin=0.01&weeklyrainin=0.03&monthlyrainin=2.06&yearlyrainin=-9999&solarradiation=41.96&UV=0&dateutc=2018-12-20%2014:48:54&softwaretype=AMBWeatherV3.0.3&action=updateraw&realtime=1&rtfreq=5 HTTP/1.0
```
---

## rtl_433 Analysis
```
# rtl_433 -a -A -Fjson -r g00*_915M_250k.cu8
rtl_433 version 18.12-32-gd233adf branch master at 201812191913
Trying conf file at "rtl_433.conf"...
Trying conf file at "/root/.rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...
Registered 96 out of 120 device decoding protocols [ 1-4 8 11-12 15-21 23 25-26 29-36 38-60 62-64 67-71 73-100 102-103 108-116 119 ]
Test mode active. Reading samples from file: g001_915M_250k.cu8
Detected FSK package	@0.184800s
{"time" : "@0.184800s", "model" : "Fine Offset WH24", "id" : 65, "temperature_C" : 11.500, "humidity" : 64, "wind_dir_deg" : 37, "wind_speed_ms" : 7.560, "gust_speed_ms" : 8.960, "rainfall_mm" : 1329.900, "uv" : 0, "uvi" : 0, "light_lux" : 6913.000, "battery" : "OK", "mic" : "CRC"}
Analyzing pulses...
Total count:   58,  width: 11.80 ms		( 2951 S)
Pulse width distribution:
 [ 0] count:    6,  width:  112 us [100;116]	(  28 S)
 [ 1] count:   48,  width:   56 us [56;60]	(  14 S)
 [ 2] count:    2,  width:  172 us [172;172]	(  43 S)
 [ 3] count:    1,  width:  236 us [236;236]	(  59 S)
 [ 4] count:    1,  width:   40 us [40;40]	(  10 S)
Gap width distribution:
 [ 0] count:   36,  width:   56 us [56;60]	(  14 S)
 [ 1] count:    6,  width:  172 us [172;176]	(  43 S)
 [ 2] count:    2,  width:  232 us [232;232]	(  58 S)
 [ 3] count:    6,  width:  112 us [112;116]	(  28 S)
 [ 4] count:    4,  width:  304 us [292;348]	(  76 S)
 [ 5] count:    2,  width:  432 us [404;464]	( 108 S)
 [ 6] count:    1,  width: 1336 us [1336;1336]	( 334 S)
Pulse period distribution:
 [ 0] count:   10,  width:  172 us [160;176]	(  43 S)
 [ 1] count:   30,  width:  116 us [116;116]	(  29 S)
 [ 2] count:   10,  width:  252 us [228;292]	(  63 S)
 [ 3] count:    6,  width:  432 us [348;524]	( 108 S)
 [ 4] count:    1,  width: 1392 us [1392;1392]	( 348 S)
Level estimates [high, low]:   3369,      4
RSSI: -6.9 dB SNR: 28.3 dB Noise: -36.1 dB
Frequency offsets [F1, F2]:    8616,  -8916	(+32.9 kHz, -34.0 kHz)
Guessing modulation: No clue...
```

```
Test mode active. Reading samples from file: g002_915M_250k.cu8
Detected FSK package	@0.184800s
{"time" : "@0.184800s", "model" : "Fine Offset WH24", "id" : 65, "temperature_C" : 11.500, "humidity" : 64, "wind_dir_deg" : 217, "wind_speed_ms" : 4.200, "gust_speed_ms" : 5.600, "rainfall_mm" : 1329.900, "uv" : 99, "uvi" : 0, "light_lux" : 13237.000, "battery" : "OK", "mic" : "CRC"}
Analyzing pulses...
Total count:   58,  width: 11.81 ms		( 2952 S)
Pulse width distribution:
 [ 0] count:    9,  width:  112 us [100;116]	(  28 S)
 [ 1] count:   45,  width:   56 us [56;60]	(  14 S)
 [ 2] count:    2,  width:  176 us [176;176]	(  44 S)
 [ 3] count:    1,  width:  232 us [232;232]	(  58 S)
 [ 4] count:    1,  width:    8 us [8;8]	(   2 S)
Gap width distribution:
 [ 0] count:   34,  width:   56 us [56;60]	(  14 S)
 [ 1] count:    8,  width:  172 us [172;176]	(  43 S)
 [ 2] count:    3,  width:  248 us [232;288]	(  62 S)
 [ 3] count:    5,  width:  116 us [116;116]	(  29 S)
 [ 4] count:    5,  width:  368 us [348;408]	(  92 S)
 [ 5] count:    2,  width:  520 us [520;520]	( 130 S)
Pulse period distribution:
 [ 0] count:    7,  width:  168 us [160;176]	(  42 S)
 [ 1] count:   29,  width:  116 us [116;116]	(  29 S)
 [ 2] count:    9,  width:  232 us [232;232]	(  58 S)
 [ 3] count:    5,  width:  312 us [292;348]	(  78 S)
 [ 4] count:    4,  width:  456 us [404;504]	( 114 S)
 [ 5] count:    3,  width:  580 us [580;580]	( 145 S)
Level estimates [high, low]:   2295,      6
RSSI: -8.5 dB SNR: 25.2 dB Noise: -34.4 dB
Frequency offsets [F1, F2]:    7717,  -8332	(+29.4 kHz, -31.8 kHz)
Guessing modulation: No clue...
```

```
Test mode active. Reading samples from file: g003_915M_250k.cu8
Detected FSK package	@0.184800s
{"time" : "@0.184800s", "model" : "Fine Offset WH24", "id" : 65, "temperature_C" : 11.500, "humidity" : 64, "wind_dir_deg" : 337, "wind_speed_ms" : 5.600, "gust_speed_ms" : 7.840, "rainfall_mm" : 1329.900, "uv" : 99, "uvi" : 0, "light_lux" : 12307.000, "battery" : "OK", "mic" : "CRC"}
Analyzing pulses...
Total count:   58,  width: 11.81 ms		( 2952 S)
Pulse width distribution:
 [ 0] count:    5,  width:  112 us [100;116]	(  28 S)
 [ 1] count:   47,  width:   56 us [56;60]	(  14 S)
 [ 2] count:    2,  width:  172 us [172;172]	(  43 S)
 [ 3] count:    2,  width:  232 us [232;232]	(  58 S)
 [ 4] count:    1,  width:  292 us [292;292]	(  73 S)
 [ 5] count:    1,  width:   16 us [16;16]	(   4 S)
Gap width distribution:
 [ 0] count:   34,  width:   56 us [56;60]	(  14 S)
 [ 1] count:   10,  width:  176 us [172;204]	(  44 S)
 [ 2] count:    3,  width:  268 us [232;292]	(  67 S)
 [ 3] count:    5,  width:  116 us [116;116]	(  29 S)
 [ 4] count:    5,  width:  452 us [404;524]	( 113 S)
Pulse period distribution:
 [ 0] count:    8,  width:  172 us [160;176]	(  43 S)
 [ 1] count:   30,  width:  116 us [116;116]	(  29 S)
 [ 2] count:    9,  width:  248 us [232;292]	(  62 S)
 [ 3] count:    5,  width:  404 us [348;464]	( 101 S)
 [ 4] count:    5,  width:  532 us [520;580]	( 133 S)
Level estimates [high, low]:   3056,      4
RSSI: -7.3 dB SNR: 27.9 dB Noise: -36.1 dB
Frequency offsets [F1, F2]:    7779,  -8211	(+29.7 kHz, -31.3 kHz)
Guessing modulation: No clue...
```

```
Test mode active. Reading samples from file: g004_915M_250k.cu8
Detected FSK package	@0.184800s
{"time" : "@0.184800s", "model" : "Fine Offset WH24", "id" : 65, "temperature_C" : 11.500, "humidity" : 64, "wind_dir_deg" : 250, "wind_speed_ms" : 4.200, "gust_speed_ms" : 8.960, "rainfall_mm" : 1329.900, "uv" : 99, "uvi" : 0, "light_lux" : 13190.000, "battery" : "OK", "mic" : "CRC"}
Analyzing pulses...
Total count:   54,  width: 11.81 ms		( 2952 S)
Pulse width distribution:
 [ 0] count:    7,  width:  112 us [100;116]	(  28 S)
 [ 1] count:   41,  width:   56 us [56;60]	(  14 S)
 [ 2] count:    1,  width:  172 us [172;172]	(  43 S)
 [ 3] count:    2,  width:  320 us [292;348]	(  80 S)
 [ 4] count:    2,  width:  232 us [232;232]	(  58 S)
 [ 5] count:    1,  width:   28 us [28;28]	(   7 S)
Gap width distribution:
 [ 0] count:   32,  width:   56 us [56;60]	(  14 S)
 [ 1] count:    6,  width:  172 us [172;176]	(  43 S)
 [ 2] count:    4,  width:  276 us [232;308]	(  69 S)
 [ 3] count:    4,  width:  112 us [112;116]	(  28 S)
 [ 4] count:    5,  width:  356 us [292;404]	(  89 S)
 [ 5] count:    2,  width:  524 us [524;524]	( 131 S)
Pulse period distribution:
 [ 0] count:    5,  width:  172 us [160;176]	(  43 S)
 [ 1] count:   27,  width:  116 us [116;116]	(  29 S)
 [ 2] count:    9,  width:  248 us [232;288]	(  62 S)
 [ 3] count:    8,  width:  408 us [348;464]	( 102 S)
 [ 4] count:    4,  width:  564 us [520;580]	( 141 S)
Level estimates [high, low]:   2375,      8
RSSI: -8.4 dB SNR: 24.2 dB Noise: -33.1 dB
Frequency offsets [F1, F2]:    7609,  -8129	(+29.0 kHz, -31.0 kHz)
Guessing modulation: No clue...
```

```
Test mode active. Reading samples from file: g005_915M_250k.cu8
Detected FSK package	@0.184800s
{"time" : "@0.184800s", "model" : "Fine Offset WH24", "id" : 65, "temperature_C" : 11.500, "humidity" : 63, "wind_dir_deg" : 247, "wind_speed_ms" : 3.920, "gust_speed_ms" : 4.480, "rainfall_mm" : 1329.900, "uv" : 99, "uvi" : 0, "light_lux" : 13128.000, "battery" : "OK", "mic" : "CRC"}
Analyzing pulses...
Total count:   54,  width: 11.81 ms		( 2952 S)
Pulse width distribution:
 [ 0] count:    7,  width:  112 us [100;116]	(  28 S)
 [ 1] count:   38,  width:   56 us [56;60]	(  14 S)
 [ 2] count:    5,  width:  172 us [172;176]	(  43 S)
 [ 3] count:    2,  width:  320 us [292;348]	(  80 S)
 [ 4] count:    1,  width:  232 us [232;232]	(  58 S)
 [ 5] count:    1,  width:   20 us [20;20]	(   5 S)
Gap width distribution:
 [ 0] count:   33,  width:   56 us [56;60]	(  14 S)
 [ 1] count:    9,  width:  168 us [140;176]	(  42 S)
 [ 2] count:    1,  width:  228 us [228;228]	(  57 S)
 [ 3] count:    2,  width:  116 us [116;116]	(  29 S)
 [ 4] count:    4,  width:  316 us [288;348]	(  79 S)
 [ 5] count:    2,  width:  404 us [404;408]	( 101 S)
 [ 6] count:    2,  width:  520 us [520;524]	( 130 S)
Pulse period distribution:
 [ 0] count:    4,  width:  168 us [160;176]	(  42 S)
 [ 1] count:   26,  width:  116 us [112;120]	(  29 S)
 [ 2] count:   11,  width:  248 us [232;292]	(  62 S)
 [ 3] count:    6,  width:  360 us [348;408]	(  90 S)
 [ 4] count:    6,  width:  528 us [464;580]	( 132 S)
Level estimates [high, low]:   2627,      4
RSSI: -7.9 dB SNR: 27.2 dB Noise: -36.1 dB
Frequency offsets [F1, F2]:    7478,  -8200	(+28.5 kHz, -31.3 kHz)
Guessing modulation: No clue...
```

```
Test mode active. Reading samples from file: g006_915M_250k.cu8
Detected FSK package	@0.184800s
{"time" : "@0.184800s", "model" : "Fine Offset WH24", "id" : 65, "temperature_C" : 11.500, "humidity" : 63, "wind_dir_deg" : 0, "wind_speed_ms" : 1.820, "gust_speed_ms" : 2.240, "rainfall_mm" : 1329.900, "uv" : 0, "uvi" : 0, "light_lux" : 5487.000, "battery" : "OK", "mic" : "CRC"}
Analyzing pulses...
Total count:   55,  width: 11.53 ms		( 2883 S)
Pulse width distribution:
 [ 0] count:    9,  width:  112 us [100;116]	(  28 S)
 [ 1] count:   43,  width:   56 us [56;60]	(  14 S)
 [ 2] count:    2,  width:  172 us [172;172]	(  43 S)
 [ 3] count:    1,  width:  344 us [344;344]	(  86 S)
Gap width distribution:
 [ 0] count:   36,  width:   56 us [56;60]	(  14 S)
 [ 1] count:    5,  width:  172 us [172;172]	(  43 S)
 [ 2] count:    5,  width:  244 us [232;288]	(  61 S)
 [ 3] count:    4,  width:  116 us [116;116]	(  29 S)
 [ 4] count:    1,  width:  520 us [520;520]	( 130 S)
 [ 5] count:    2,  width:  376 us [348;408]	(  94 S)
 [ 6] count:    1,  width: 1392 us [1392;1392]	( 348 S)
Pulse period distribution:
 [ 0] count:    6,  width:  168 us [160;176]	(  42 S)
 [ 1] count:   30,  width:  116 us [112;120]	(  29 S)
 [ 2] count:    8,  width:  228 us [228;232]	(  57 S)
 [ 3] count:    4,  width:  300 us [288;348]	(  75 S)
 [ 4] count:    3,  width:  540 us [468;580]	( 135 S)
 [ 5] count:    2,  width:  404 us [404;408]	( 101 S)
 [ 6] count:    1,  width: 1452 us [1452;1452]	( 363 S)
Level estimates [high, low]:   3682,      4
RSSI: -6.5 dB SNR: 28.7 dB Noise: -36.1 dB
Frequency offsets [F1, F2]:    7649,  -8903	(+29.2 kHz, -34.0 kHz)
Guessing modulation: Pulse Code Modulation (Not Return to Zero)
Attempting demodulation... short_width: 56, long_width: 56, reset_limit: 57344, sync_width: 0
Use a flex decoder with -X 'n=name,m=FSK_PCM,s=56,l=56,r=57344'
```

```
Test mode active. Reading samples from file: g007_915M_250k.cu8
Detected FSK package	@0.184800s
{"time" : "@0.184800s", "model" : "Fine Offset WH24", "id" : 65, "temperature_C" : 11.500, "humidity" : 63, "wind_dir_deg" : 348, "wind_speed_ms" : 2.660, "gust_speed_ms" : 3.360, "rainfall_mm" : 1329.900, "uv" : 0, "uvi" : 0, "light_lux" : 5316.000, "battery" : "OK", "mic" : "CRC"}
Analyzing pulses...
Total count:   57,  width: 11.81 ms		( 2952 S)
Pulse width distribution:
 [ 0] count:    7,  width:  112 us [100;116]	(  28 S)
 [ 1] count:   43,  width:   56 us [56;60]	(  14 S)
 [ 2] count:    4,  width:  172 us [172;172]	(  43 S)
 [ 3] count:    2,  width:  320 us [292;348]	(  80 S)
 [ 4] count:    1,  width:    4 us [4;4]	(   1 S)
Gap width distribution:
 [ 0] count:   35,  width:   56 us [56;60]	(  14 S)
 [ 1] count:    9,  width:  172 us [172;176]	(  43 S)
 [ 2] count:    2,  width:  224 us [220;232]	(  56 S)
 [ 3] count:    6,  width:  116 us [116;116]	(  29 S)
 [ 4] count:    2,  width:  320 us [292;348]	(  80 S)
 [ 5] count:    1,  width:  404 us [404;404]	( 101 S)
 [ 6] count:    1,  width: 1392 us [1392;1392]	( 348 S)
Pulse period distribution:
 [ 0] count:    5,  width:  168 us [160;176]	(  42 S)
 [ 1] count:   30,  width:  116 us [112;120]	(  29 S)
 [ 2] count:   12,  width:  240 us [228;288]	(  60 S)
 [ 3] count:    5,  width:  332 us [292;352]	(  83 S)
 [ 4] count:    3,  width:  484 us [464;524]	( 121 S)
 [ 5] count:    1,  width: 1452 us [1452;1452]	( 363 S)
Level estimates [high, low]:   3367,      4
RSSI: -6.9 dB SNR: 28.3 dB Noise: -36.1 dB
Frequency offsets [F1, F2]:    8129,  -8129	(+31.0 kHz, -31.0 kHz)
Guessing modulation: No clue...
```
