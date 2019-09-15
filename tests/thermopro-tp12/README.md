# ThermoPro TP-12 Wireless Meat Thermometer

[Product page](https://itronicsmall.com/products/thermopro-tp-12)

## Data capture log

    Total count:  714,  width: 273019		(1092.1 ms)
    Pulse width distribution:
     [ 0] count:    1,  width:    26 [26;26]	( 104 us)
     [ 1] count:  713,  width:   119 [116;140]	( 476 us)
    Gap width distribution:
     [ 0] count:   17,  width:   895 [841;945]	(3580 us)
     [ 1] count:  340,  width:   125 [123;128]	( 500 us)
     [ 2] count:  340,  width:   369 [366;372]	(1476 us)
     [ 3] count:   16,  width:   273 [272;274]	(1092 us)
    Pulse period distribution:
     [ 0] count:   17,  width:  1027 [867;1084]	(4108 us)
     [ 1] count:  340,  width:   244 [242;262]	( 976 us)
     [ 2] count:  356,  width:   483 [390;490]	(1932 us)
    Level estimates [high, low]:  15891,     83
    Frequency offsets [F1, F2]:   18586,      0	(+70.9 kHz, +0.0 kHz)

A normal sequence for the TP12:

    [00] {0} : 
    [01] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [02] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [03] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [04] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [05] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [06] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [07] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [08] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [09] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [10] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [11] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [12] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [13] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [14] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [15] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [16] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
    [17] {40} 38 73 21 bb 81 : 00111000 01110011 00100001 10111011 10000001 

Layout appears to be:

    [01] {41} 38 73 21 bb 81 80 : 00111000 01110011 00100001 10111011 10000001 1
                                  device   temp 1   temp     temp 2   checksum
                                           low bits 1   2    low bits
                                                    hi bits

## Analysis

The modulation for the TP-12 seems to be the same as the TP-11.  The format
is similar, just with more bits.

Unlike the TP-11, the device ID is simply the first 8 bits.  It changes
randomly each time the transmitter batteries are changed, which would allow
the receiver to pair with just one transmitter even if multiple ones are in
range.  But that means the length of data, number of repeats, and checksum
are the only way we can be sure the data comes from this device.

There's an 8-bit checksum at the end - it seems likely that this would be
the same mysterious algorithm as used by the TP-11, though I have not
verified this.

[Discussion about TP-11 checksum](https://groups.google.com/d/msg/rtl_433/KgKEs6rg9u0/kxeF0Ym1AQAJ)
