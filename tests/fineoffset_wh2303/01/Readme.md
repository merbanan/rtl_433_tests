**Fine Offset WH-4000/2310 weather stations**

**Data is received via MeteoBridge Software.**

|ID|DateTime|TempOut|Tmin|Tmax|HumOut|Press|Dew|HeatIdx|WindSpeed|WindAvg|WindDir|WindDirEng|RainRate|RainDay|UV|Solar Rad|
|--|--------|-------|----|----|------|-----|---|-------|---------|-------|-------|----------|--------|-------|--|---------|
|120721|2017-10-19 12:40:28|17.9|17.9|18.1|61.0|1019.200|10.3|17.9|5.6|4.1|318|NW|0.00|3.00|8.0|1242.00|
|120722|2017-10-19 12:40:59|17.9|17.9|18.1|61.0|1019.200|10.3|17.9|5.6|4.1|318|NW|0.00|3.00|8.0|1242.00|
|120723|2017-10-19 12:41:31|17.7|17.7|18.1|61.0|1019.200|10.1|17.7|5.6|4.2|254|WSW|0.00|3.00|8.0|1254.00|
|120724|2017-10-19 12:42:04|17.7|17.7|18.1|60.0|1019.200|9.8|17.7|6.7|3.8|263|W|0.00|3.00|8.0|1245.00|
|120725|2017-10-19 12:42:36|17.7|17.7|17.9|60.0|1019.200|9.8|17.7|3.4|2.9|253|WSW|0.00|3.00|8.0|1243.00|
|120726|2017-10-19 12:43:07|17.5|17.5|17.9|60.0|1019.000|9.6|17.5|5.6|4.8|217|SW|0.00|3.00|8.0|1244.00|
|120727|2017-10-19 12:43:40|17.6|17.5|17.9|60.0|1019.000|9.7|17.6|4.5|3.5|305|NW|0.00|3.00|8.0|1244.00|
|120728|2017-10-19 12:44:11|17.6|17.5|17.7|59.0|1019.000|9.5|17.6|7.8|6.2|269|W|0.00|3.00|8.0|1249.00|
|120729|2017-10-19 12:44:44|17.7|17.5|17.7|60.0|1019.200|9.8|17.7|5.6|3.8|277|W|0.00|3.00|8.0|1250.00|
|120730|2017-10-19 12:45:16|17.7|17.5|17.9|60.0|1019.200|9.8|17.7|4.5|3.6|295|WNW|0.00|3.00|8.0|1253.00|
|120731|2017-10-19 12:45:47|17.8|17.5|17.9|60.0|1019.200|9.9|17.8|5.6|4.5|242|WSW|0.00|3.00|8.0|1249.00|

The Fine Offset WH2303 sends two frequency pulses simultaneously at different Radio Frequencies one at 433.85MHz and the other at 433.988MHz.

This according to the icasa.pdf datasheet : 

	ITU Code : A1D 	A: Double sideband, DSB, including DSB full carrier
			1: One channel containing digital information without the use of modulating sub-carriers 
			D: Data transmission, telemetry or command
	Modulation : ASK
	Power Output: 10mW
	Channel Spacing: 10kHz
						

The test data(gfileNNN.data) was recorded with two RTL SDR's running together, both directories files where created simultaneously for each pair of pulses.

One ID entry into the above database is approximately 2 pulses at both frequencies from the WH2303 device spaced ~16 seconds apart.

For Example:

ID: 120721 = ./**433_850MHz**/gfile001.data + gfile002.data 
	
	./gfile001.data

		Input format: uint8
		
		p_limit: 62
		bitbuffer:: Number of rows: 3 
		[00] {30} 00 00 01 00 : 00000000 00000000 00000001 000000
		[01] {8} 2b : 00101011 
		[02] {15} 48 08 : 01001000 0000100

	./gfile002.data

		Input format: uint8
		
		p_limit: 62 - 
		bitbuffer:: Number of rows: 5 
		[00] {29} 80 00 04 00 : 10000000 00000000 00000100 00000
		[01] {4} 20 : 0010
		[02] {5} a8 : 10101
		[03] {7} 58 : 0101100
		[04] {7} 20 : 0010000



ID: 120721 = ./**433_988MHz**/gfile001.data + gfile002.data 

	./gfile001.data

		Input format: uint8
		
		p_limit: 48
		bitbuffer:: Number of rows: 2 
		[00] {36} c4 00 10 08 80 : 11000100 00000000 00010000 00001000 1000
		[01] {16} 88 44 : 10001000 01000100 


	./gfile002.data

		Input format: uint8
		
		p_limit: 48
		bitbuffer:: Number of rows: 2 
		[00] {40} 80 00 04 01 10 : 10000000 00000000 00000100 00000001 00010000 
		[01] {15} 81 04 : 10000001 0000010 



Spectrum Captured Using GQRX with an Airspy.

**PS. $./rtl_433 -f 433892e3 -A** yields the following results - >

Detected FSK package	@ 2017-10-19 20:46:01

	Analyzing pulses...
	Total count:   45,  width:  2799		(11.2 ms)
	Pulse width distribution:
	 [ 0] count:    3,  width:    28 [28;29]	( 112 us)
	 [ 1] count:   37,  width:    14 [14;15]	(  56 us)
	 [ 2] count:    2,  width:    43 [43;43]	( 172 us)
	 [ 3] count:    2,  width:    58 [58;58]	( 232 us)
	 [ 4] count:    1,  width:    73 [73;73]	( 292 us)
	Gap width distribution:
	 [ 0] count:   26,  width:    14 [14;16]	(  56 us)
	 [ 1] count:    5,  width:    43 [43;44]	( 172 us)
	 [ 2] count:    6,  width:    65 [58;73]	( 260 us)
	 [ 3] count:    3,  width:    29 [29;29]	( 116 us)
	 [ 4] count:    2,  width:   123 [116;131]	( 492 us)
	 [ 5] count:    1,  width:   232 [232;232]	( 928 us)
	 [ 6] count:    1,  width:   348 [348;348]	(1392 us)
	Pulse period distribution:
	 [ 0] count:    4,  width:    43 [43;44]	( 172 us)
	 [ 1] count:   21,  width:    29 [29;29]	( 116 us)
	 [ 2] count:    9,  width:    64 [58;73]	( 256 us)
	 [ 3] count:    6,  width:    89 [87;101]	( 356 us)
	 [ 4] count:    2,  width:   137 [130;145]	( 548 us)
	 [ 5] count:    1,  width:   247 [247;247]	( 988 us)
	 [ 6] count:    1,  width:   362 [362;362]	(1448 us)
	Level estimates [high, low]:  15953,    113
	Frequency offsets [F1, F2]:   22978,  -6544	(+87.7 kHz, -25.0 kHz)
	Guessing modulation: Pulse Code Modulation (Not Return to Zero)
	Attempting demodulation... short_limit: 14, long_limit: 14, reset_limit: 14336, demod_arg: 0
	pulse_demod_pcm(): Analyzer Device 
	bitbuffer:: Number of rows: 1 
	[00] {198} d5 55 55 55 55 16 ea 12 51 10 f1 06 20 82 00 80 7d 00 00 40 00 00 10 f3 a0 

Detected FSK package	@ 2017-10-19 20:46:49

	Analyzing pulses...
	Total count:   47,  width:  2799		(11.2 ms)
	Pulse width distribution:
	 [ 0] count:    3,  width:    29 [29;29]	( 116 us)
	 [ 1] count:   39,  width:    14 [14;15]	(  56 us)
	 [ 2] count:    1,  width:    43 [43;43]	( 172 us)
	 [ 3] count:    4,  width:    69 [58;73]	( 276 us)
	Gap width distribution:
	 [ 0] count:   31,  width:    14 [14;15]	(  56 us)
	 [ 1] count:    4,  width:    43 [43;43]	( 172 us)
	 [ 2] count:    4,  width:    69 [58;73]	( 276 us)
	 [ 3] count:    3,  width:    29 [29;29]	( 116 us)
	 [ 4] count:    2,  width:   123 [116;131]	( 492 us)
	 [ 5] count:    1,  width:   232 [232;232]	( 928 us)
	 [ 6] count:    1,  width:   363 [363;363]	(1452 us)
	Pulse period distribution:
	 [ 0] count:    5,  width:    43 [43;44]	( 172 us)
	 [ 1] count:   25,  width:    29 [29;29]	( 116 us)
	 [ 2] count:    5,  width:    60 [58;72]	( 240 us)
	 [ 3] count:    3,  width:   130 [116;145]	( 520 us)
	 [ 4] count:    6,  width:    87 [87;87]	( 348 us)
	 [ 5] count:    1,  width:   247 [247;247]	( 988 us)
	 [ 6] count:    1,  width:   377 [377;377]	(1508 us)
	Level estimates [high, low]:  15979,     95
	Frequency offsets [F1, F2]:   22680,  -4768	(+86.5 kHz, -18.2 kHz)
	Guessing modulation: Pulse Code Modulation (Not Return to Zero)
	Attempting demodulation... short_limit: 14, long_limit: 14, reset_limit: 14336, demod_arg: 0
	pulse_demod_pcm(): Analyzer Device 
	bitbuffer:: Number of rows: 1 
	[00] {198} d5 55 55 55 55 16 ea 12 51 15 f1 05 a0 82 00 80 7d 00 00 40 00 00 0b cf a0 



