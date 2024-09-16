data captured with GIT hash: 9e973ce5b997725b235424f657b3b7016be1de58
this contains every two hours some wrong data packages like in files (g007_868.4M_250k.cu8 ... g011_868.4M_250k.cu8)


$ rtl_433 -f 868.4M -Y classic -s 250k -M level -M bits -M protocol -vv -R 69 -S known

rtl_433 version nightly-19-g9e973ce5 branch master at 202303271012 inputs file rtl_tcp RTL-SDR SoapySDR with TLS
Use -h for usage help and see https://triq.org/ for documentation.
Trying conf file at "rtl_433.conf"...
Trying conf file at "/home/martinschmitt/.config/rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...

New defaults active, use "-Y classic -s 250k" if you need the old defaults

Registering protocol [69] "Fine Offset WH1050 Weather Station"
[Protocols] Registered 1 out of 243 device decoding protocols
[Input] The internals of input handling changed, read about and report problems on PR #1978
[SDR] Found 1 device(s)
[SDR] trying device 0: NESDRv4, RTL2838UHIDIR, SN: 08150002
Found Rafael Micro R820T/2 tuner
[SDR] Using device 0: NESDRv4, RTL2838UHIDIR, SN: 08150002, "Generic RTL2832U OEM"
Exact sample rate is: 250000.000414 Hz
[SDR] Sample rate set to 250000 S/s.
[Input] Bit detection level set to 0.0 (Auto).
[SDR] Tuner gain set to Auto.
[Input] Reading samples in async mode...
[SDR] Tuned to 868.400MHz.
Allocating 15 zero-copy buffers
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:54:33                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 2.45      Wind gust : 3.67
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.5 MHz
RSSI      : -0.1 dB      SNR       : 24.5 dB       Noise     : -24.7 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a04060415f2               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0100 0000 0110 0000 0100 0001 0101 1111 001
*** Saving signal to file g001_868.4M_250k.cu8 (972786 samples, 1966080 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:55:21                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 2.45      Wind gust : 3.67
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.5 MHz
RSSI      : -0.1 dB      SNR       : 24.9 dB       Noise     : -25.0 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a04060415f2               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0100 0000 0110 0000 0100 0001 0101 1111 001
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:55:21                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 2.45      Wind gust : 3.67
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -9.2 dB      SNR       : 27.0 dB       Noise     : -36.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a04060415f2               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0100 0000 0110 0000 0100 0001 0101 1111 001
*** Saving signal to file g002_868.4M_250k.cu8 (636267 samples, 1310720 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:56:09                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 3.67      Wind gust : 6.12
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.5 MHz
RSSI      : -0.2 dB      SNR       : 25.9 dB       Noise     : -26.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a060a04158e               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0110 0000 1010 0000 0100 0001 0101 1000 111
*** Saving signal to file g003_868.4M_250k.cu8 (355926 samples, 786432 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:56:57                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 61 %          Wind avg speed: 4.90      Wind gust : 8.57
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.7 dB      SNR       : 22.0 dB       Noise     : -25.7 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7a080e041440               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1010 0000 1000 0000 1110 0000 0100 0001 0100 0100 000
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:56:57                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 61 %          Wind avg speed: 4.90      Wind gust : 8.57
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -10.2 dB     SNR       : 28.9 dB       Noise     : -39.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7a080e041440               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1010 0000 1000 0000 1110 0000 0100 0001 0100 0100 000
*** Saving signal to file g004_868.4M_250k.cu8 (472337 samples, 1048576 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:58:33                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 60 %          Wind avg speed: 1.22      Wind gust : 2.45
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.5 dB      SNR       : 23.5 dB       Noise     : -27.0 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc780204041412               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1000 0000 0010 0000 0100 0000 0100 0001 0100 0001 001
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:58:33                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 60 %          Wind avg speed: 1.22      Wind gust : 2.45
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -10.6 dB     SNR       : 26.8 dB       Noise     : -37.4 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc780204041412               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1000 0000 0010 0000 0100 0000 0100 0001 0100 0001 001
Signal bigger than buffer, signal = 4849664 > buffer 3145728 !!
*** Saving signal to file g005_868.4M_250k.cu8 (2368106 samples, 3145728 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 21:59:21                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 60 %          Wind avg speed: 1.22      Wind gust : 2.45
Total rainfall: 156.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 20.7 dB       Noise     : -24.5 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc780204041412               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1000 0000 0010 0000 0100 0000 0100 0001 0100 0001 001
Signal bigger than buffer, signal = 3276800 > buffer 3145728 !!
*** Saving signal to file g006_868.4M_250k.cu8 (1592687 samples, 3145728 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:02:33                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 27.4 C       Humidity  : 2 %           Wind avg speed: 63.65     Wind gust : 42.84
Total rainfall: 5157.6   Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -1.8 dB      SNR       : 25.2 dB       Noise     : -27.0 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed2154404684686502c               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 0100 0110 1000 0100 0110 1000 0110 0101 0000 0010 110
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:02:33                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 27.4 C       Humidity  : 2 %           Wind avg speed: 63.65     Wind gust : 42.84
Total rainfall: 5157.6   Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -10.6 dB     SNR       : 28.5 dB       Noise     : -39.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed2154404684686502c               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 0100 0110 1000 0100 0110 1000 0110 0101 0000 0010 110
*** Saving signal to file g007_868.4M_250k.cu8 (974282 samples, 1966080 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:03:21                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 27.4 C       Humidity  : 3 %           Wind avg speed: 41.62     Wind gust : 42.84
Total rainfall: 5157.6   Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -4.7 dB      SNR       : 21.2 dB       Noise     : -25.9 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440644468651e8               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 0110 0100 0100 0100 0110 1000 0110 0101 0001 1110 100
*** Saving signal to file g008_868.4M_250k.cu8 (76368 samples, 262144 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:04:09                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 27.4 C       Humidity  : 4 %           Wind avg speed: 19.58     Wind gust : 42.84
Total rainfall: 5157.6   Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -5.1 dB      SNR       : 20.8 dB       Noise     : -25.9 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440820468651c0               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1000 0010 0000 0100 0110 1000 0110 0101 0001 1100 000
*** Saving signal to file g009_868.4M_250k.cu8 (1240717 samples, 2490368 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:04:57                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 27.4 C       Humidity  : 4 %           Wind avg speed: 107.71    Wind gust : 42.84         Total rainfall: 5157.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 22.4 dB       Noise     : -26.2 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed2154408b046865038               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1000 1011 0000 0100 0110 1000 0110 0101 0000 0011 100
*** Saving signal to file g010_868.4M_250k.cu8 (768467 samples, 1572864 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:05:45                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 27.4 C       Humidity  : 5 %           Wind avg speed: 85.68     Wind gust : 42.84         Total rainfall: 5157.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 22.7 dB       Noise     : -26.5 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440a8c468651c4               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1010 1000 1100 0100 0110 1000 0110 0101 0001 1100 010
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:05:45                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 27.4 C       Humidity  : 5 %           Wind avg speed: 85.68     Wind gust : 42.84         Total rainfall: 5157.6    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -10.0 dB     SNR       : 23.1 dB       Noise     : -33.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440a8c468651c4               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1010 1000 1100 0100 0110 1000 0110 0101 0001 1100 010
*** Saving signal to file g011_868.4M_250k.cu8 (647613 samples, 1310720 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:06:33                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 58 %          Wind avg speed: 1.22      Wind gust : 2.45          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -2.9 dB      SNR       : 21.1 dB       Noise     : -24.0 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc740204041502               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0100 0000 0010 0000 0100 0000 0100 0001 0101 0000 001
*** Saving signal to file g012_868.4M_250k.cu8 (724621 samples, 1572864 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:07:21                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 58 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -5.6 dB      SNR       : 19.3 dB       Noise     : -24.9 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7404060414b6               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0100 0000 0100 0000 0110 0000 0100 0001 0100 1011 011
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:07:21                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 58 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -11.9 dB     SNR       : 27.3 dB       Noise     : -39.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7404060414b6               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0100 0000 0100 0000 0110 0000 0100 0001 0100 1011 011
*** Saving signal to file g013_868.4M_250k.cu8 (485323 samples, 1048576 bytes)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2023-03-28 22:08:09                    Protocol  : 69
model     : Fineoffset-WH1050                      StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 59 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 20.1 dB       Noise     : -23.9 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc760406041510               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0110 0000 0100 0000 0110 0000 0100 0001 0101 0001 000
*** Saving signal to file g014_868.4M_250k.cu8 (287316 samples, 655360 bytes)
^CSignal caught, exiting!
[Input] sdr_handler exit
[rtl_433] stopping...



###########################################################################################################################################################################################################
###########################################################################################################################################################################################################
###########################################################################################################################################################################################################
###########################################################################################################################################################################################################
###########################################################################################################################################################################################################
###########################################################################################################################################################################################################

data reprocessed with GIT hash: b2bb5cda39c601ca4d81cda754eef8f90cf36692


$ ./rtl_433 -f 868.4M -Y classic -s 250k -M level -M bits -M protocol -vv -R 69 -r test_samples/g*_868.4M_250k.cu8
rtl_433 version -128-NOTFOUND branch master at 202303271012 inputs file rtl_tcp RTL-SDR SoapySDR with TLS
Use -h for usage help and see https://triq.org/ for documentation.
Trying conf file at "rtl_433.conf"...
Trying conf file at "/home/martinschmitt/.config/rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...

New defaults active, use "-Y classic -s 250k" if you need the old defaults

Registering protocol [69] "Fine Offset WH1050 Weather Station"
[Protocols] Registered 1 out of 243 device decoding protocols
[Input] Test mode active. Reading samples from file: test_samples/g001_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @2.542544s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.5 MHz
RSSI      : -0.1 dB      SNR       : 24.5 dB       Noise     : -24.6 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a04060415f2               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0100 0000 0110 0000 0100 0001 0101 1111 001
[Input] Test mode file issued 8 packets
[Input] Test mode active. Reading samples from file: test_samples/g002_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @2.194832s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.5 MHz
RSSI      : -0.1 dB      SNR       : 24.9 dB       Noise     : -25.0 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a04060415f2               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0100 0000 0110 0000 0100 0001 0101 1111 001
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @2.383540s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -9.2 dB      SNR       : 27.0 dB       Noise     : -36.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a04060415f2               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0100 0000 0110 0000 0100 0001 0101 1111 001
[Input] Test mode file issued 5 packets
[Input] Test mode active. Reading samples from file: test_samples/g003_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.585012s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.7 C        Humidity  : 61 %          Wind avg speed: 3.67      Wind gust : 6.12          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.5 MHz
RSSI      : -0.2 dB      SNR       : 26.0 dB       Noise     : -26.2 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203ba7a060a04158e               bits      : 1111 1110 1011 0010 0000 0011 1011 1010 0111 1010 0000 0110 0000 1010 0000 0100 0001 0101 1000 111
[Input] Test mode file issued 3 packets
[Input] Test mode active. Reading samples from file: test_samples/g004_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.839580s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 61 %          Wind avg speed: 4.90      Wind gust : 8.57          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.7 dB      SNR       : 22.0 dB       Noise     : -25.7 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7a080e041440               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1010 0000 1000 0000 1110 0000 0100 0001 0100 0100 000
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @1.032200s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 61 %          Wind avg speed: 4.90      Wind gust : 8.57          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -10.2 dB     SNR       : 28.9 dB       Noise     : -39.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7a080e041440               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1010 0000 1000 0000 1110 0000 0100 0001 0100 0100 000
[Input] Test mode file issued 4 packets
[Input] Test mode active. Reading samples from file: test_samples/g005_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
[Input] Test mode file issued 12 packets
[Input] Test mode active. Reading samples from file: test_samples/g006_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @6.047620s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 60 %          Wind avg speed: 1.22      Wind gust : 2.45          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 20.7 dB       Noise     : -24.5 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc780204041412               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 1000 0000 0010 0000 0100 0000 0100 0001 0100 0001 001
[Input] Test mode file issued 12 packets
[Input] Test mode active. Reading samples from file: test_samples/g007_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.100568s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 1             Station ID: 144
Battery   : 1            Radio Clock: 2023-03-28T22:02:34                    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -1.8 dB      SNR       : 25.0 dB       Noise     : -26.8 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed2154404684686502c               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 0100 0110 1000 0100 0110 1000 0110 0101 0000 0010 110
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.293184s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 1             Station ID: 144
Battery   : 1            Radio Clock: 2023-03-28T22:02:34                    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -10.6 dB     SNR       : 26.8 dB       Noise     : -37.4 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed2154404684686502c               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 0100 0110 1000 0100 0110 1000 0110 0101 0000 0010 110
[Input] Test mode file issued 8 packets
[Input] Test mode active. Reading samples from file: test_samples/g008_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.284352s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 1             Station ID: 144
Battery   : 1            Radio Clock: 2023-03-28T22:03:22                    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -4.7 dB      SNR       : 21.2 dB       Noise     : -25.9 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440644468651e8               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 0110 0100 0100 0100 0110 1000 0110 0101 0001 1110 100
[Input] Test mode file issued 1 packets
[Input] Test mode active. Reading samples from file: test_samples/g009_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @3.532084s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 1             Station ID: 144
Battery   : 1            Radio Clock: 2023-03-28T22:04:10                    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -5.1 dB      SNR       : 20.7 dB       Noise     : -25.8 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440820468651c0               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1000 0010 0000 0100 0110 1000 0110 0101 0001 1100 000
[Input] Test mode file issued 10 packets
[Input] Test mode active. Reading samples from file: test_samples/g010_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @1.321732s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 1             Station ID: 144
Battery   : 1            Radio Clock: 2023-03-28T22:04:58                    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 22.4 dB       Noise     : -26.2 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed2154408b046865038               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1000 1011 0000 0100 0110 1000 0110 0101 0000 0011 100
[Input] Test mode file issued 6 packets
[Input] Test mode active. Reading samples from file: test_samples/g011_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.096524s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 1             Station ID: 144
Battery   : 1            Radio Clock: 2023-03-28T22:05:46                    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 22.6 dB       Noise     : -26.3 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440a8c468651c4               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1010 1000 1100 0100 0110 1000 0110 0101 0001 1100 010
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.287192s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 1             Station ID: 144
Battery   : 1            Radio Clock: 2023-03-28T22:05:46                    Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -10.0 dB     SNR       : 23.7 dB       Noise     : -33.7 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}fed215440a8c468651c4               bits      : 1111 1110 1101 0010 0001 0101 0100 0100 0000 1010 1000 1100 0100 0110 1000 0110 0101 0001 1100 010
[Input] Test mode file issued 5 packets
[Input] Test mode active. Reading samples from file: test_samples/g012_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.312780s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 58 %          Wind avg speed: 1.22      Wind gust : 2.45          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -2.9 dB      SNR       : 21.2 dB       Noise     : -24.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc740204041502               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0100 0000 0010 0000 0100 0000 0100 0001 0101 0000 001
[Input] Test mode file issued 6 packets
[Input] Test mode active. Reading samples from file: test_samples/g013_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @1.666680s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 58 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -5.6 dB      SNR       : 19.3 dB       Noise     : -24.9 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7404060414b6               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0100 0000 0100 0000 0110 0000 0100 0001 0100 1011 011
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @1.857352s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 58 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -11.9 dB     SNR       : 27.3 dB       Noise     : -39.1 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc7404060414b6               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0100 0000 0100 0000 0110 0000 0100 0001 0100 1011 011
[Input] Test mode file issued 4 packets
[Input] Test mode active. Reading samples from file: test_samples/g014_868.4M_250k.cu8
[Input] Input format "CU8 IQ (2ch uint8)"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.226992s   Protocol  : 69
model     : Fineoffset-WH1050                      Msg type  : 0             StationID : 0090
Battery   : 1            Temperature: 7.8 C        Humidity  : 59 %          Wind avg speed: 2.45      Wind gust : 3.67          Total rainfall: 156.6     Integrity : CRC
Modulation: ASK          Freq      : 868.4 MHz
RSSI      : -3.8 dB      SNR       : 20.1 dB       Noise     : -23.9 dB
[pulse_slicer_pwm] Fine Offset WH1050 Weather Station
codes     : {79}feb203bc760406041510               bits      : 1111 1110 1011 0010 0000 0011 1011 1100 0111 0110 0000 0100 0000 0110 0000 0100 0001 0101 0001 000
[Input] Test mode file issued 3 packets
