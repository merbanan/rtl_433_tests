# InFactory PT310 (ZX-7074/7073) pool thermometer

![alt tag](https://raw.githubusercontent.com/gbraux/rtl_433_tests/master/tests/InFactroy-Temp-Humidity-Sensor-T05K-THC/front.JPG)

This InFactory branded waterproof floating pool sensor is sold by Pearl for it's Infactory Pool Thermometer PT-310 (ZX-7073). It's fairly well made and has
a LCD screen showing current temperature, channel and sending indicator.
- Page where you can buy an additional sensor: https://www.pearl.de/a-ZX7074-3041.shtml
- Sensor together with base station: https://www.pearl.de/a-ZX7073-3041.shtml
- Couldn't find Radio certification documents

Note that I do NOT have the base station. I have verified the temperature against the temp shown (also minus temps). 

## Initial findings
Sensor is transmitting 5 bytes with PPM OOK encoding. These 5 bytes are transmitted 6 times but only at value change.

## Frame Structure

This is what I could read from the samples, it seems to match up nicely.

IIIIIIII KKKKVVVV VVVVVVVV FFFFCCCC CCCCGGGG

I = Sensor ID. Resets to a new value after battery is removed.
K = Channel ID (1000 = Ch1, 1001 = Ch2, 1010 = Ch3)
V = Sensor value as 12 bit number representing a fixed point float. If high bit is set, number is negativ. See data below
F = Framing 1, always 0xf (1111)
C = I assume this is a checksum, couldn't figure it out
G = Framing 2, always 0x4 (1000)

### Open questions
- How is battery low encoded?
- How is the checksum calculated?

## Sensor (front)
I'll send pics later, travelling right now.

## Data

Data can be decoded by `-X 'n=pool3,m=OOK_PPM,s=1000,l=2008,g=2024,r=4064'` (thanks @zuckerschwedt). Data packets get repeated 6 times.

Decoding: 
```
baseband_demod_FM: low pass filter for 250000 Hz at cutoff 25000 Hz, 40.0 us
Detected OOK package    @0.224144s
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.224144s
model     : pool3        count     : 6             num_rows  : 6             rows      : 
len       : 38           data      : 7e810ffb74, 
len       : 38           data      : 7e810ffb74, 
len       : 38           data      : 7e810ffb74, 
len       : 38           data      : 7e810ffb74, 
len       : 38           data      : 7e810ffb74, 
len       : 37           data      : 7e810ffb70
codes     : {38}7e810ffb74, {38}7e810ffb74, {38}7e810ffb74, {38}7e810ffb74, {38}7e810ffb74, {37}7e810ffb70
Analyzing pulses...
Total count:  233,  width: 486.75 ms            (121687 S)
Pulse width distribution:
 [ 0] count:  227,  width:  492 us [440;508]    ( 123 S)
 [ 1] count:    6,  width:  128 us [124;132]    (  32 S)
Gap width distribution:
 [ 0] count:   90,  width:  968 us [964;980]    ( 242 S)
 [ 1] count:  137,  width: 1948 us [1936;2040]  ( 487 S)
 [ 2] count:    5,  width: 3896 us [3896;3900]  ( 974 S)
Pulse period distribution:
 [ 0] count:   90,  width: 1464 us [1456;1484]  ( 366 S)
 [ 1] count:  137,  width: 2428 us [2148;2448]  ( 607 S)
 [ 2] count:    5,  width: 4344 us [4336;4352]  (1086 S)
Pulse timing distribution:
 [ 0] count:  227,  width:  492 us [440;508]    ( 123 S)
 [ 1] count:    6,  width:  128 us [124;132]    (  32 S)
 [ 2] count:   90,  width:  968 us [964;980]    ( 242 S)
 [ 3] count:  137,  width: 1948 us [1936;2040]  ( 487 S)
 [ 4] count:    5,  width: 3896 us [3896;3900]  ( 974 S)
 [ 5] count:    1,  width: 10004 us [10004;10004]       (2501 S)
Level estimates [high, low]:  16010,     90
RSSI: -0.1 dB SNR: 22.5 dB Noise: -22.6 dB
Frequency offsets [F1, F2]:   -4742,      0     (-18.1 kHz, +0.0 kHz)

```

The `8e8115f6e0` would be for 27.7 degrees centigrate.

Here are some data samples gathered for a different device ids and channels:

channel 1:
3280ebff64: 23.5
2980ecfe04: 23.6
3a80edfb04: 23.7
c280edff54: 23.7


channel 2:
e490eaf864: 23.4
3690f3f054: 24.3


channel 3:
3ba0eef7f4: 23.8
e7a0eef444: 23.8
8ba0ebfb14: 23.5