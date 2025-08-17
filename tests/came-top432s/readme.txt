CAME SpA - Remote Control Transmitter - TOP-432S

Commonly used for CAME electric gates. The same key is used to both open and close the gate.

FCC ID: M48T432S
FCC Duty Cycle: https://fccid.io/M48T432S/Test-Report/duty-cycle-plot-94348
FCC Test Report: https://fccid.io/M48T432S/Test-Report/Test-Report-94340

Signal Generation: Key 1 (CH 1)
Signal Capture: g043_433.92M_250k.cu8

Replay/Analyze of capture:


$ rtl_433 -r g043_433.92M_250k.cu8 -a -A

rtl_433 version 19.08-113-g2b6d5fd branch master at 201912162234 inputs file rtl_tcp RTL-SDR
Use -h for usage help and see https://triq.org/ for documentation.
Trying conf file at "rtl_433.conf"...
Trying conf file at "/home/pi/.config/rtl_433/rtl_433.conf"...
Trying conf file at "/usr/local/etc/rtl_433/rtl_433.conf"...
Trying conf file at "/etc/rtl_433/rtl_433.conf"...

        Consider using "-M newmodel" to transition to new model keys. This will become the default someday.
        A table of changes and discussion is at https://github.com/merbanan/rtl_433/pull/986.

Registered 112 out of 141 device decoding protocols [ 1-4 8 11-12 15-17 19-21 23 25-26 29-36 38-60 63 67-71 73-100 102-104 108-116 119 121 124-128 131-141 ]
Test mode active. Reading samples from file: g043_433.92M_250k.cu8
Detected OOK package    @0.112220s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3144 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  688 us [684;692]    ( 172 S)
Gap width distribution:
 [ 0] count:    4,  width:  328 us [328;332]    (  82 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15895,      7
RSSI: -0.1 dB SNR: 33.6 dB Noise: -33.7 dB
Frequency offsets [F1, F2]:  -19959,      0     (-76.1 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.136628s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3144 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;356]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  328 us [328;332]    (  82 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;688]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  16002,     10
RSSI: -0.1 dB SNR: 32.0 dB Noise: -32.1 dB
Frequency offsets [F1, F2]:  -20961,      0     (-80.0 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.161036s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3145 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  328 us [328;332]    (  82 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15903,     15
RSSI: -0.1 dB SNR: 30.3 dB Noise: -30.4 dB
Frequency offsets [F1, F2]:  -20352,      0     (-77.6 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.185448s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;676]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  684 us [680;692]    ( 171 S)
 [ 1] count:    3,  width: 1356 us [1356;1356]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15879,     10
RSSI: -0.1 dB SNR: 32.0 dB Noise: -32.1 dB
Frequency offsets [F1, F2]:  -19524,      0     (-74.5 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.209864s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3145 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;332]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1012;1024]  ( 254 S)
Level estimates [high, low]:  15912,     23
RSSI: -0.1 dB SNR: 28.4 dB Noise: -28.5 dB
Frequency offsets [F1, F2]:  -20566,      0     (-78.5 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.234280s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  344 us [344;360]    (  86 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  672 us [668;676]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1024]  ( 254 S)
Level estimates [high, low]:  15903,     15
RSSI: -0.1 dB SNR: 30.3 dB Noise: -30.4 dB
Frequency offsets [F1, F2]:  -20139,      0     (-76.8 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 344, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=344,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.258696s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;332]    (  83 S)
 [ 1] count:    8,  width:  672 us [668;676]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15890,     10
RSSI: -0.1 dB SNR: 32.0 dB Noise: -32.1 dB
Frequency offsets [F1, F2]:  -20611,      0     (-78.6 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.283116s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;356]    (  87 S)
 [ 1] count:    4,  width:  688 us [688;688]    ( 172 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;332]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [680;688]    ( 170 S)
 [ 1] count:    3,  width: 1360 us [1360;1360]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15872,      8
RSSI: -0.1 dB SNR: 33.0 dB Noise: -33.1 dB
Frequency offsets [F1, F2]:  -20446,      0     (-78.0 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.307532s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1360 us [1360;1360]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15910,     17
RSSI: -0.1 dB SNR: 29.7 dB Noise: -29.8 dB
Frequency offsets [F1, F2]:  -20376,      0     (-77.7 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.331952s
Analyzing pulses...
Total count:   13,  width: 12.59 ms             ( 3147 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  688 us [688;688]    ( 172 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;332]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;676]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  684 us [680;692]    ( 171 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1024]  ( 254 S)
Level estimates [high, low]:  15897,     15
RSSI: -0.1 dB SNR: 30.3 dB Noise: -30.4 dB
Frequency offsets [F1, F2]:  -20534,      0     (-78.3 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.356376s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3145 S)
Pulse width distribution:
 [ 0] count:    9,  width:  344 us [344;356]    (  86 S)
 [ 1] count:    4,  width:  688 us [688;688]    ( 172 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;332]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;676]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;688]    ( 170 S)
 [ 1] count:    3,  width: 1360 us [1360;1360]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1012;1020]  ( 254 S)
Level estimates [high, low]:  15945,     13
RSSI: -0.1 dB SNR: 30.9 dB Noise: -31.0 dB
Frequency offsets [F1, F2]:  -20121,      0     (-76.8 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 344, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=344,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.380796s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;356]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [680;688]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1024]  ( 254 S)
Level estimates [high, low]:  15902,      8
RSSI: -0.1 dB SNR: 33.0 dB Noise: -33.1 dB
Frequency offsets [F1, F2]:  -20645,      0     (-78.8 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.405216s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  344 us [340;360]    (  86 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  328 us [328;332]    (  82 S)
 [ 1] count:    8,  width:  672 us [672;680]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  676 us [672;692]    ( 169 S)
 [ 1] count:    3,  width: 1360 us [1356;1368]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15931,     14
RSSI: -0.1 dB SNR: 30.6 dB Noise: -30.7 dB
Frequency offsets [F1, F2]:  -20621,      0     (-78.7 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 344, long_width: 0, reset_limit: 684, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=344,l=0,r=684'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.429640s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;356]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15942,      9
RSSI: -0.1 dB SNR: 32.5 dB Noise: -32.6 dB
Frequency offsets [F1, F2]:  -20414,      0     (-77.9 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.454060s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;332]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;676]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1024]  ( 254 S)
Level estimates [high, low]:  15951,      7
RSSI: -0.1 dB SNR: 33.6 dB Noise: -33.7 dB
Frequency offsets [F1, F2]:  -20173,      0     (-77.0 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.478484s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  684 us [680;692]    ( 171 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15945,     14
RSSI: -0.1 dB SNR: 30.6 dB Noise: -30.7 dB
Frequency offsets [F1, F2]:  -20214,      0     (-77.1 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.502908s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  344 us [344;356]    (  86 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  672 us [672;672]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15927,      9
RSSI: -0.1 dB SNR: 32.5 dB Noise: -32.6 dB
Frequency offsets [F1, F2]:  -20734,      0     (-79.1 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 344, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=344,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.527332s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  344 us [344;360]    (  86 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  672 us [672;676]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15972,     10
RSSI: -0.1 dB SNR: 32.0 dB Noise: -32.1 dB
Frequency offsets [F1, F2]:  -20169,      0     (-76.9 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 344, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=344,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.551752s
Analyzing pulses...
Total count:   13,  width: 12.59 ms             ( 3147 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;364]    (  87 S)
 [ 1] count:    4,  width:  688 us [688;688]    ( 172 S)
Gap width distribution:
 [ 0] count:    4,  width:  328 us [328;332]    (  82 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [680;692]    ( 170 S)
 [ 1] count:    3,  width: 1360 us [1360;1360]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15894,      8
RSSI: -0.1 dB SNR: 33.0 dB Noise: -33.1 dB
Frequency offsets [F1, F2]:  -21263,      0     (-81.1 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.576180s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  688 us [688;692]    ( 172 S)
Gap width distribution:
 [ 0] count:    4,  width:  328 us [328;332]    (  82 S)
 [ 1] count:    8,  width:  672 us [672;672]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  676 us [676;688]    ( 169 S)
 [ 1] count:    3,  width: 1360 us [1360;1364]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  16002,     13
RSSI: -0.1 dB SNR: 30.9 dB Noise: -31.0 dB
Frequency offsets [F1, F2]:  -20372,      0     (-77.7 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.600604s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;332]    (  83 S)
 [ 1] count:    8,  width:  672 us [668;676]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1360 us [1360;1360]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1012;1024]  ( 254 S)
Level estimates [high, low]:  15952,     10
RSSI: -0.1 dB SNR: 32.0 dB Noise: -32.1 dB
Frequency offsets [F1, F2]:  -20187,      0     (-77.0 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.625032s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;356]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  684 us [680;692]    ( 171 S)
 [ 1] count:    3,  width: 1356 us [1352;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15942,     10
RSSI: -0.1 dB SNR: 32.0 dB Noise: -32.1 dB
Frequency offsets [F1, F2]:  -20343,      0     (-77.6 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.649456s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;356]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  672 us [668;676]    ( 168 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1360]  ( 339 S)
 [ 2] count:    5,  width: 1016 us [1016;1020]  ( 254 S)
Level estimates [high, low]:  15951,      9
RSSI: -0.1 dB SNR: 32.5 dB Noise: -32.6 dB
Frequency offsets [F1, F2]:  -20479,      0     (-78.1 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.673880s
Analyzing pulses...
Total count:   13,  width: 12.59 ms             ( 3147 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [340;360]    (  87 S)
 [ 1] count:    4,  width:  688 us [688;692]    ( 172 S)
Gap width distribution:
 [ 0] count:    4,  width:  328 us [328;332]    (  82 S)
 [ 1] count:    8,  width:  668 us [668;676]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [680;688]    ( 170 S)
 [ 1] count:    3,  width: 1360 us [1356;1368]  ( 340 S)
 [ 2] count:    5,  width: 1016 us [1012;1020]  ( 254 S)
Level estimates [high, low]:  15912,     10
RSSI: -0.1 dB SNR: 32.0 dB Noise: -32.1 dB
Frequency offsets [F1, F2]:  -20244,      0     (-77.2 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 680, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=680'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

Detected OOK package    @0.698308s
Analyzing pulses...
Total count:   13,  width: 12.58 ms             ( 3146 S)
Pulse width distribution:
 [ 0] count:    9,  width:  348 us [344;360]    (  87 S)
 [ 1] count:    4,  width:  684 us [684;688]    ( 171 S)
Gap width distribution:
 [ 0] count:    4,  width:  332 us [332;336]    (  83 S)
 [ 1] count:    8,  width:  668 us [668;672]    ( 167 S)
Pulse period distribution:
 [ 0] count:    4,  width:  680 us [676;692]    ( 170 S)
 [ 1] count:    3,  width: 1356 us [1356;1356]  ( 339 S)
 [ 2] count:    5,  width: 1020 us [1016;1024]  ( 255 S)
Level estimates [high, low]:  15944,     15
RSSI: -0.1 dB SNR: 30.3 dB Noise: -30.4 dB
Frequency offsets [F1, F2]:  -20886,      0     (-79.7 kHz, +0.0 kHz)
Guessing modulation: Manchester coding
Attempting demodulation... short_width: 348, long_width: 0, reset_limit: 676, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_MC_ZEROBIT,s=348,l=0,r=676'
pulse_demod_manchester_zerobit(): Analyzer Device
bitbuffer:: Number of rows: 1
[00] {17} 20 90 80  : 00100000 10010000 1

*** signal_start = 18058, signal_end = 187724, signal_len = 169666, pulses_found = 325
Iteration 1. t: 129    min: 87 (225)    max: 172 (100)    delta 5
Iteration 2. t: 129    min: 87 (225)    max: 172 (100)    delta 0
Distance coding: Pulse length 129

Short distance: 82, long distance: 167, packet distance: 2961

p_limit: 129
bitbuffer:: Number of rows: 25
[00] {12} 7a e0     : 01111010 1110
[01] {12} 7a e0     : 01111010 1110
[02] {12} 7a e0     : 01111010 1110
[03] {12} 7a e0     : 01111010 1110
[04] {12} 7a e0     : 01111010 1110
[05] {12} 7a e0     : 01111010 1110
[06] {12} 7a e0     : 01111010 1110
[07] {12} 7a e0     : 01111010 1110
[08] {12} 7a e0     : 01111010 1110
[09] {12} 7a e0     : 01111010 1110
[10] {12} 7a e0     : 01111010 1110
[11] {12} 7a e0     : 01111010 1110
[12] {12} 7a e0     : 01111010 1110
[13] {12} 7a e0     : 01111010 1110
[14] {12} 7a e0     : 01111010 1110
[15] {12} 7a e0     : 01111010 1110
[16] {12} 7a e0     : 01111010 1110
[17] {12} 7a e0     : 01111010 1110
[18] {12} 7a e0     : 01111010 1110
[19] {12} 7a e0     : 01111010 1110
[20] {12} 7a e0     : 01111010 1110
[21] {12} 7a e0     : 01111010 1110
[22] {12} 7a e0     : 01111010 1110
[23] {12} 7a e0     : 01111010 1110
[24] {12} 7a e0     : 01111010 1110
... Maximum number of rows reached. Message is likely truncated.
Iteration 1. t: 0    min: 0 (0)    max: 0 (0)    delta 3567587328
Iteration 2. t: 0    min: 0 (0)    max: 0 (0)    delta 0
Distance coding: Pulse length 0

Short distance: 1000000, long distance: 0, packet distance: 0

p_limit: 0
bitbuffer:: Number of rows: 0