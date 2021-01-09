# TFA Marbella Pool thermometer

TFA Marbella is a wireless pool termomenter with main a display.

Sensor cat no:       30.3238.06

Main display cat no: 3066.01

External links
https://www.tfa-dostmann.de/produkt/funk-poolthermometer-marbella-30-3066/
https://clientmedia.trade-server.net/1768_tfadost/media/3/52/21352.pdf


Analysis
========    

Radio encoding

The Marbella sensor operates at 868MHz frequency band.
Using rtl_433 with -A option indicates: FSK_PCM with s=424,l=424 and r=434176

![Radio analysis using triq.org ](triq.gif)

Data encoding

Using 







======
Transmitter reset: (probably got new device id)
```
25.9C:
11011010 10010001 00000011 0111
26.0C:
11101010 10010001 00000100 0111
```

03
======
Another transmitter: (certanly with different device id)
```
19.8C:
01010100 10100000 11000110 0110
20.4C:
10110100 10100000 11001100 0110
20.5C:
11000100 10100000 11001101 0110
```

04
======
changing channels: 1,2,3

Protocol
======
```
AAAABBBB BBBBCCCC CCCCCCCC DDEE

A: ?
B: device id (changing only after reset)
C: templerature
D: channel number
E: ? 
```
If the temperature value exceeds 1024, take temperature vill be negative, take 1's complement

