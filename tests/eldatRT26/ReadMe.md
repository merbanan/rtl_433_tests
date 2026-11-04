# RT26 Wristband transmitter

The RT26 Wristband transmitter is a 868.3 MHz button to page caregiver.

Please consider supporting this device. It would help a lot for sick and/or handicapped people. 

> "The RT26 wristband transmitter has been specially adapted to the requirements of people in need of care. The large push button makes it easy to operate.
> Switching electrical devices on and off with a 1-button operation or activating paging systems are among the standard application areas of this transmitter.
> An LED indicates if the battery needs to be changed. If the battery is running low, a separate radio signal is transmitted which can be analyzed by a corresponding Easywave receiver."

(http://www.eldat.de/produkte/sender/rt26e_en.html)

Set of button and outlet receiver: http://www.eldat.de/produkte/sets/rs16e_en.html

    ./rtl_433 -f 868.30e6 -A
     
    Detected FSK package
    Analyzing pulses...
    Total count:   29,  width:  2713                (10.9 ms)
    Pulse width distribution:
     [ 0] count:    1,  width:     0 [ 0; 0]        (   0 us)
     [ 1] count:   20,  width:    26 [25;27]        ( 104 us)
     [ 2] count:    3,  width:    52 [52;52]        ( 208 us)
     [ 3] count:    2,  width:    78 [78;78]        ( 312 us)
     [ 4] count:    2,  width:   104 [104;104]      ( 416 us)
     [ 5] count:    1,  width:    15 [15;15]        (  60 us)
    Gap width distribution:
     [ 0] count:    1,  width:   267 [267;267]      (1068 us)
     [ 1] count:   18,  width:    26 [25;27]        ( 104 us)
     [ 2] count:    4,  width:    78 [78;79]        ( 312 us)
     [ 3] count:    3,  width:    52 [52;53]        ( 208 us)
     [ 4] count:    1,  width:   105 [105;105]      ( 420 us)
     [ 5] count:    1,  width:   343 [343;343]      (1372 us)
    Pulse period distribution:
     [ 0] count:    1,  width:   267 [267;267]      (1068 us)
     [ 1] count:   14,  width:    52 [52;53]        ( 208 us)
     [ 2] count:    3,  width:   104 [104;104]      ( 416 us)
     [ 3] count:    4,  width:    78 [78;79]        ( 312 us)
     [ 4] count:    5,  width:   140 [130;157]      ( 560 us)
     [ 5] count:    1,  width:   369 [369;369]      (1476 us)
    Level estimates [high, low]:   1320,     17
    Frequency offsets [F1, F2]:   -6274, -22866     (-23.9 kHz, -87.2 kHz)
    Guessing modulation: No clue...
    
    Detected OOK package
    Analyzing pulses...
    Total count:    1,  width:    37                ( 0.1 ms)
    Pulse width distribution:
     [ 0] count:    1,  width:    37 [37;37]        ( 148 us)
    Gap width distribution:
    Pulse period distribution:
    Level estimates [high, low]:   4910,      8
    Frequency offsets [F1, F2]:     605,      0     (+2.3 kHz, +0.0 kHz)
    Guessing modulation: Single pulse detected. Probably Frequency Shift Keying or just noise...
    
    Detected OOK package
    Analyzing pulses...
    Total count:    1,  width:    37                ( 0.1 ms)
    Pulse width distribution:
     [ 0] count:    1,  width:    37 [37;37]        ( 148 us)
    Gap width distribution:
    Pulse period distribution:
    Level estimates [high, low]:   4802,      8
    Frequency offsets [F1, F2]:    1021,      0     (+3.9 kHz, +0.0 kHz)
    Guessing modulation: Single pulse detected. Probably Frequency Shift Keying or just noise...
    
    Detected OOK package
    Analyzing pulses...
    Total count:    1,  width:    37                ( 0.1 ms)
    Pulse width distribution:
     [ 0] count:    1,  width:    37 [37;37]        ( 148 us)
    Gap width distribution:
    Pulse period distribution:
    Level estimates [high, low]:   5122,     23
    Frequency offsets [F1, F2]:     368,      0     (+1.4 kHz, +0.0 kHz)
    Guessing modulation: Single pulse detected. Probably Frequency Shift Keying or just noise...
    
    Detected OOK package
    Analyzing pulses...
    Total count:    3,  width: 49742                (199.0 ms)
    Pulse width distribution:
     [ 0] count:    1,  width:    38 [38;38]        ( 152 us)
     [ 1] count:    1,  width: 48080 [48080;48080]  (192320 us)
     [ 2] count:    1,  width:   450 [450;450]      (1800 us)
    Gap width distribution:
     [ 0] count:    1,  width:   207 [207;207]      ( 828 us)
     [ 1] count:    1,  width:   967 [967;967]      (3868 us)
    Pulse period distribution:
     [ 0] count:    1,  width:   245 [245;245]      ( 980 us)
     [ 1] count:    1,  width: 49047 [49047;49047]  (196188 us)
    Level estimates [high, low]:  15959,     16
    Frequency offsets [F1, F2]:    1883,      0     (+7.2 kHz, +0.0 kHz)
    Guessing modulation: Pulse Width Modulation with startbit/delimiter
    Attempting demodulation... short_limit: 244, long_limit: 24265, reset_limit: 968, demod_arg: 0
    pulse_demod_pwm_ternary(): Analyzer Device
    bitbuffer:: Number of rows: 2
    [00] {0} :
    [01] {2} 80 : 10
