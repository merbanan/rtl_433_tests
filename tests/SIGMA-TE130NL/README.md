# SIGMA TE 130NL

Temperature only Sensor/Receiver using HIDEKI temperature sensor.

Assembled in 2004. Seems same model was published from Honeywell.

I've tried to decode signal but still stucked with decoding the temperature value...

What I've discovered so far:

1. Sender uses HIDEKI TS02 chipset. FCCID [1] points to TS02 but on circuit it is labelled as TS12-MAIN / TS12-KEY.
2. Signal interval is aprox. 20-30secs
3. Data is sent 3 times each interval (perhaps this means there is no CRC?)
4. First three byte seems to be the device ID (e1 01 17). When replacing the battery (aprox. after 5 secs.) the device ID is renewed.
5. Discovered timing diagram of sensor [2] 

Probe:
------

	Detected OOK package
	Analyzing pulses...
	Total count:   57,  width: 17614		(70.5 ms)
	Pulse width distribution:
	 [ 0] count:   16,  width:   237 [232;248]	( 948 us)
	 [ 1] count:   40,  width:   114 [109;118]	( 456 us)
	 [ 2] count:    1,  width:    23 [23;23]	(  92 us)
	Gap width distribution:
	 [ 0] count:   16,  width:   251 [249;255]	(1004 us)
	 [ 1] count:   40,  width:   129 [127;134]	( 516 us)
	Pulse period distribution:
	 [ 0] count:    7,  width:   490 [487;503]	(1960 us)
	 [ 1] count:   18,  width:   366 [364;369]	(1464 us)
	 [ 2] count:   31,  width:   244 [242;246]	( 976 us)
	Level estimates [high, low]:  15970,     15
	Frequency offsets [F1, F2]:  -20184,      0	(-77.0 kHz, +0.0 kHz)
	Guessing modulation: Pulse Width Modulation with startbit/delimiter
	Attempting demodulation... short_limit: 68, long_limit: 175, reset_limit: 256, demod_arg: 0
	pulse_demod_pwm_ternary(): Analyzer Device 
	bitbuffer:: Number of rows: 2 
	[00] {56} e1 01 17 04 08 62 44 
	[01] {0} : 

	Detected OOK package
	Analyzing pulses...
	Total count:   57,  width: 17614		(70.5 ms)
	Pulse width distribution:
	 [ 0] count:   16,  width:   239 [237;250]	( 956 us)
	 [ 1] count:   40,  width:   116 [115;119]	( 464 us)
	 [ 2] count:    1,  width:    23 [23;23]	(  92 us)
	Gap width distribution:
	 [ 0] count:   16,  width:   249 [248;251]	( 996 us)
	 [ 1] count:   40,  width:   127 [126;129]	( 508 us)
	Pulse period distribution:
	 [ 0] count:    7,  width:   490 [487;501]	(1960 us)
	 [ 1] count:   18,  width:   366 [364;367]	(1464 us)
	 [ 2] count:   31,  width:   244 [242;246]	( 976 us)
	Level estimates [high, low]:  15991,     19
	Frequency offsets [F1, F2]:  -19827,      0	(-75.6 kHz, +0.0 kHz)
	Guessing modulation: Pulse Width Modulation with startbit/delimiter
	Attempting demodulation... short_limit: 69, long_limit: 177, reset_limit: 252, demod_arg: 0
	pulse_demod_pwm_ternary(): Analyzer Device 
	bitbuffer:: Number of rows: 2 
	[00] {56} e1 01 17 04 08 62 44 
	[01] {0} : 

	Detected OOK package
	Analyzing pulses...
	Total count:   57,  width: 17615		(70.5 ms)
	Pulse width distribution:
	 [ 0] count:   16,  width:   239 [237;250]	( 956 us)
	 [ 1] count:   40,  width:   116 [115;119]	( 464 us)
	 [ 2] count:    1,  width:    24 [24;24]	(  96 us)
	Gap width distribution:
	 [ 0] count:   16,  width:   249 [247;251]	( 996 us)
	 [ 1] count:   40,  width:   127 [126;130]	( 508 us)
	Pulse period distribution:
	 [ 0] count:    7,  width:   490 [487;501]	(1960 us)
	 [ 1] count:   18,  width:   365 [364;368]	(1460 us)
	 [ 2] count:   31,  width:   244 [242;246]	( 976 us)
	Level estimates [high, low]:  15986,     15
	Frequency offsets [F1, F2]:  -19735,      0	(-75.3 kHz, +0.0 kHz)
	Guessing modulation: Pulse Width Modulation with startbit/delimiter
	Attempting demodulation... short_limit: 70, long_limit: 177, reset_limit: 252, demod_arg: 0
	pulse_demod_pwm_ternary(): Analyzer Device 
	bitbuffer:: Number of rows: 2 
	[00] {56} e1 01 17 04 08 62 44 
	[01] {0} : 

[1] https://fccid.io/Q9PTS02-C
[2] https://fccid.io/document.php?id=350860

