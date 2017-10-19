###Fine Offset WH-4000/2310 weather stations

#####Data is received via MeteoBridge Software.

ID	DateTime		TempOut		Tmin	Tmax	HumOut		Press		Dew	HeatIdx		WindSpeed	WindAvg		WindDir		WindDirEng	RainRate	RainDay		UV	Solar Rad
120721	2017-10-19 12:40:28	17.9		17.9	18.1	61.0		1019.200	10.3	17.9		5.6		4.1		318		NW		0.00		3.00		8.0	1242.00
120722	2017-10-19 12:40:59	17.9		17.9	18.1	61.0		1019.200	10.3	17.9		5.6		4.1		318		NW		0.00		3.00		8.0	1242.00
120723	2017-10-19 12:41:31	17.7		17.7	18.1	61.0		1019.200	10.1	17.7		5.6		4.2		254		WSW		0.00		3.00		8.0	1254.00
120724	2017-10-19 12:42:04	17.7		17.7	18.1	60.0		1019.200	9.8	17.7		6.7		3.8		263		W		0.00		3.00		8.0	1245.00
120725	2017-10-19 12:42:36	17.7		17.7	17.9	60.0		1019.200	9.8	17.7		3.4		2.9		253		WSW		0.00		3.00		8.0	1243.00
120726	2017-10-19 12:43:07	17.5		17.5	17.9	60.0		1019.000	9.6	17.5		5.6		4.8		217		SW		0.00		3.00		8.0	1244.00
120727	2017-10-19 12:43:40	17.6		17.5	17.9	60.0		1019.000	9.7	17.6		4.5		3.5		305		NW		0.00		3.00		8.0	1244.00
120728	2017-10-19 12:44:11	17.6		17.5	17.7	59.0		1019.000	9.5	17.6		7.8		6.2		269		W		0.00		3.00		8.0	1249.00
120729	2017-10-19 12:44:44	17.7		17.5	17.7	60.0		1019.200	9.8	17.7		5.6		3.8		277		W		0.00		3.00		8.0	1250.00
120730	2017-10-19 12:45:16	17.7		17.5	17.9	60.0		1019.200	9.8	17.7		4.5		3.6		295		WNW		0.00		3.00		8.0	1253.00
120731	2017-10-19 12:45:47	17.8		17.5	17.9	60.0		1019.200	9.9	17.8		5.6		4.5		242		WSW		0.00		3.00		8.0	1249.00

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



Spectrum Captured Using GQRX with an airspy.

Station Info pdf included.


