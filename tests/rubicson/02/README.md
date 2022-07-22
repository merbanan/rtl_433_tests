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

Frame structure is like standard Rubicson but with one or two bits added to the end.

## Sensor (front)
Pics of front, side and board attached.
