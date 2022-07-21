# InFactory PT310 (ZX-7074/7073) pool thermometer

![alt tag](https://raw.githubusercontent.com/gbraux/rtl_433_tests/master/tests/InFactroy-Temp-Humidity-Sensor-T05K-THC/front.JPG)

This InFactory branded waterproof floating pool sensor is sold by Pearl for it's Infactory Pool Thermometer PT-310 (ZX-7073). It's fairly well made and has
a LCD screen showing current temperature, channel and sending indicator.
- Page where you can buy an additional sensor: https://www.pearl.de/a-ZX7074-3041.shtml
- Sensor together with base station: https://www.pearl.de/a-ZX7073-3041.shtml
- Couldn't find Radio certification documents

Note that I do NOT have the base station. I have verified the temperature against the temp shown (also minus temps). 

## Initial findings
Sensor is transmitting 5 bytes with PPM OOK encoding. These 5 bytes are transmitted 6 times, every minute.

## Frame Structure

This is what I could read from the samples, it seems to match up nicely.

IIIIIIII IIIIVVVV VVVVVVVV FFFFCCCC CCCCGGGG

I = Sensor ID. Resets to a new value after battery is removed.
V = Sensor value as 12 bit number representing a fixed point float. If high bit is set, number is negativ. See data below
F = Framing 1, always 0xf (1111)
C = I assume this is a checksum, couldn't figure it out
G = Framing 2, always 0

### Open questions
- How is battery low encoded?
- There are three channels - are they reflected in the id?
- How is the checksum calculated?

## Sensor (front)
I'll send pics later, travelling right now.

## Data

Data can be decoded by `-X 'n=pool3,m=OOK_PPM,s=1000,l=2008,g=2024,r=4064'`. Data packets get repeated 6 times with an empty packet between - maybe I'm missreading the encoding?

Decoding: 
```
Detected OOK package    2022-07-21 15:03:32
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2022-07-21 15:03:32
model     : pool3        count     : 11            num_rows  : 11            rows      : 
len       : 37           data      : e49060f4b0, 
len       : 0            data      : , 
len       : 37           data      : e49060f4b0, 
len       : 0            data      : , 
len       : 37           data      : e49060f4b0, 
len       : 0            data      : , 
len       : 37           data      : e49060f4b0, 
len       : 0            data      : , 
len       : 37           data      : e49060f4b0, 
len       : 0            data      : , 
len       : 37           data      : e49060f4b0
codes     : {37}e49060f4b0, {0}, {37}e49060f4b0, {0}, {37}e49060f4b0, {0}, {37}e49060f4b0, {0}, {37}e49060f4b0, {0}, {37}e49060f4b0
```

Here are some data samples gathered

778116f9d0 = 27.8 (278)
7780abf0a0 = 17.1
778023f1e0 = 3.5
778feef450 = -1.8
778fe5f5f0 = -2.7
778ffffdf0 = -0.1

After reset, a new id is created:
f2904dfe60 = 7.7

Another reset:
e49059f3a0 = 8.9 
e49060f4b0 = 9.6