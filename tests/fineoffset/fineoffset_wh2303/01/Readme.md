# Fine Offset WH-4000/2310 weather stations

**Data is received via MeteoBridge Software.**

|ID|DateTime|TempOut|Tmin|Tmax|HumOut|Press|Dew|HeatIdx|WindSpeed(m/s)|WindAvg(m/s)|WindDir(Deg)|RainRate(mm)|RainDay(mm)|UV|Solar Rad|
|--|--------|-------|----|----|------|-----|---|-------|---------|-------|-------|--------|-------|--|---------|
|124074|2017-10-20 18:29:27|16.1|15.8|16.1|69.0|1024.700|10.4|16.1|1.1|1.0|289|0.00|0.00|1.0|39.00|
|124075|2017-10-20 18:30:00|16.1|16.0|16.1|69.0|1024.700|10.4|16.1|1.1|1.1|225|0.00|0.00|1.0|38.00|
|124076|2017-10-20 18:30:31|16.2|16.0|16.2|69.0|1024.800|10.5|16.2|3.4|2.4|287|0.00|0.00|1.0|38.00|
|124077|2017-10-20 18:31:03|16.1|16.0|16.2|69.0|1024.600|10.4|16.1|2.2|1.8|305|0.00|0.00|1.0|37.00|
|124078|2017-10-20 18:31:36|16.0|16.0|16.2|69.0|1024.600|10.3|16.0|4.5|2.9|240|0.00|0.00|1.0|36.00|
|124079|2017-10-20 18:32:07|16.0|16.0|16.2|69.0|1024.800|10.3|16.0|2.2|1.3|297|0.00|0.00|0.0|35.00|
|124080|2017-10-20 18:32:39|16.0|16.0|16.1|69.0|1024.800|10.3|16.0|1.1|0.1|253|0.00|0.00|0.0|34.00|
|124081|2017-10-20 18:33:10|16.0|16.0|16.1|69.0|1024.900|10.3|16.0|1.1|0.8|208|0.00|0.00|0.0|34.00|
|124082|2017-10-20 18:33:43|15.9|15.9|16.1|69.0|1024.900|10.2|15.9|2.2|1.5|283|0.00|0.00|0.0|33.00|
|124083|2017-10-20 18:34:16|16.0|15.9|16.0|69.0|1024.900|10.3|16.0|5.6|3.8|244|0.00|0.00|0.0|32.00|
|124084|2017-10-20 18:34:49|15.9|15.8|16.0|69.0|1024.800|10.2|15.9|3.4|2.0|201|0.00|0.00|0.0|32.00|
|124085|2017-10-20 18:35:21|15.9|15.8|16.0|69.0|1024.900|10.2|15.9|3.4|2.8|290|0.00|0.00|0.0|31.00|




The Fine Offset WH2303 sends two frequency pulses simultaneously at different Radio Frequencies one at 433.85MHz and the other at 433.988MHz.

This according to the icasa.pdf datasheet : 

	ITU Code : A1D 	A: Double sideband, DSB, including DSB full carrier
					1: One channel containing digital information without the use of modulating sub-carriers 
					D: Data transmission, telemetry or command
	Modulation : ASK
	Power Output: 10mW
	Channel Spacing: 10kHz


**Spectrum Captured Using GQRX with an Airspy.**
						

The test data(gfileNNN.data) was recorded with three RTL SDR's running together, all directories files where created simultaneously for each pair of pulses.

This includes sideband fc- "433.850MHz", sideband fc+ "433.988MHz" and the carrier frequency at 433.892Mhz.

One ID entry into the above database is approximately 2 pulses(gfiles) of all three frequencies from the WH2303 device spaced ~16 seconds apart.

For Example:

<!-- This is Fc(-) -->
ID: 124074 = ./**433_850MHz**/gfile001.data + gfile002.data 
	
	./gfile001.data

		Input format: uint8
		
		p_limit: 75
		bitbuffer:: Number of rows: 3 
		[00] {40} 00 00 00 00 00 : 00000000 00000000 00000000 00000000 00000000 
		[01] {2} c0 : 11
		[02] {13} 4c 00 : 01001100 00000


	./gfile002.data

		Input format: uint8
		
		p_limit: 86
		bitbuffer:: Number of rows: 3 
		[00] {41} 00 00 00 00 01 80 : 00000000 00000000 00000000 00000000 00000001 1
		[01] {6} 48 : 010010
		[02] {8} 00 : 00000000 



<!-- This is Fc(+) -->
ID: 124074 = ./**433_988MHz**/gfile001.data + gfile002.data 

	./gfile001.data

		Input format: uint8
		
		p_limit: 61
		bitbuffer:: Number of rows: 3 
		[00] {32} 90 01 04 02 : 10010000 00000001 00000100 00000010 
		[01] {2} 80 : 10
		[02] {10} 02 00 : 00000010 00


	./gfile002.data

		Input format: uint8
		
		p_limit: 73
		bitbuffer:: Number of rows: 4 
		[00] {25} 81 80 80 00 : 10000001 10000000 10000000 0
		[01] {1} 00 : 0
		[02] {2} 80 : 10
		[03] {12} 08 00 : 00001000 0000


<!-- This is the carrier in Pulse Analyzer mode and analyze mode (rtl_433 -A option) -->
ID: 124074 = ./gfile001.data + gfile002.data 
	
	./gfile001.data
	
		Input format: uint8
		Detected FSK package	@ @0.000000s
		Analyzing pulses...
		Total count:   55,  width:  2770		(11.1 ms)
		Pulse width distribution:
		 [ 0] count:   10,  width:    28 [28;29]	( 112 us)
		 [ 1] count:   39,  width:    14 [14;15]	(  56 us)
		 [ 2] count:    4,  width:    43 [43;44]	( 172 us)
		 [ 3] count:    2,  width:    65 [58;72]	( 260 us)
		Gap width distribution:
		 [ 0] count:   35,  width:    14 [14;15]	(  56 us)
		 [ 1] count:    6,  width:    43 [43;44]	( 172 us)
		 [ 2] count:    3,  width:    58 [58;58]	( 232 us)
		 [ 3] count:    5,  width:    29 [29;29]	( 116 us)
		 [ 4] count:    3,  width:    82 [73;87]	( 328 us)
		 [ 5] count:    2,  width:   138 [131;145]	( 552 us)
		Pulse period distribution:
		 [ 0] count:    8,  width:    43 [43;44]	( 172 us)
		 [ 1] count:   28,  width:    29 [29;30]	( 116 us)
		 [ 2] count:   12,  width:    66 [58;87]	( 264 us)
		 [ 3] count:    3,  width:   149 [145;159]	( 596 us)
		 [ 4] count:    3,  width:   111 [101;116]	( 444 us)
		Level estimates [high, low]:  15921,      2
		Frequency offsets [F1, F2]:   22023,  -5488	(+84.0 kHz, -20.9 kHz)
		Guessing modulation: Pulse Code Modulation (Not Return to Zero)
		Attempting demodulation... short_limit: 14, long_limit: 14, reset_limit: 14336, demod_arg: 0
		pulse_demod_pcm(): Analyzer Device 
		bitbuffer:: Number of rows: 1 
		[00] {196} d5 55 55 55 55 16 ea 12 51 6b 31 18 a2 87 81 00 7d 00 35 81 c1 c2 9b 96 00

		>>>rtl_433 -r gfile001.data -a >>> OUTPUT

		Input format: uint8
		*** signal_start = 42706, signal_end = 65537
		signal_len = 22831,  pulses = 1
		Distance coding: Pulse length 2830

		Short distance: 1000000, long distance: 0, packet distance: 0

		p_limit: 2831
		bitbuffer:: Number of rows: 0 


	./gfile002.data

		Input format: uint8
		Detected FSK package	@ @0.000000s
		Analyzing pulses...
		Total count:   55,  width:  2756		(11.0 ms)
		Pulse width distribution:
		 [ 0] count:   10,  width:    29 [29;29]	( 116 us)
		 [ 1] count:   40,  width:    14 [14;15]	(  56 us)
		 [ 2] count:    3,  width:    43 [43;44]	( 172 us)
		 [ 3] count:    2,  width:    80 [73;87]	( 320 us)
		Gap width distribution:
		 [ 0] count:   37,  width:    14 [14;15]	(  56 us)
		 [ 1] count:    6,  width:    43 [43;44]	( 172 us)
		 [ 2] count:    3,  width:    58 [58;58]	( 232 us)
		 [ 3] count:    4,  width:    29 [29;29]	( 116 us)
		 [ 4] count:    2,  width:   145 [145;145]	( 580 us)
		 [ 5] count:    2,  width:   108 [101;116]	( 432 us)
		Pulse period distribution:
		 [ 0] count:    8,  width:    43 [43;44]	( 172 us)
		 [ 1] count:   28,  width:    29 [29;29]	( 116 us)
		 [ 2] count:   11,  width:    63 [58;73]	( 252 us)
		 [ 3] count:    4,  width:   105 [87;116]	( 420 us)
		 [ 4] count:    3,  width:   150 [130;160]	( 600 us)
		Level estimates [high, low]:  15987,      8
		Frequency offsets [F1, F2]:   22165,  -6151	(+84.6 kHz, -23.5 kHz)
		Guessing modulation: Pulse Code Modulation (Not Return to Zero)
		Attempting demodulation... short_limit: 14, long_limit: 14, reset_limit: 14336, demod_arg: 0
		pulse_demod_pcm(): Analyzer Device 
		bitbuffer:: Number of rows: 1 
		[00] {196} d5 55 55 55 55 16 ea 12 51 70 b1 18 a2 84 00 80 7d 00 35 01 bf 3b 5a cc 00 


		>>>rtl_433 -r gfile001.data -a >>> Output

		Input format: uint8
		*** signal_start = 42706, signal_end = 65537
		signal_len = 22831,  pulses = 1
		Distance coding: Pulse length 2830

		Short distance: 1000000, long distance: 0, packet distance: 0

		p_limit: 2830
		bitbuffer:: Number of rows: 0 
