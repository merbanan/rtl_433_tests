# Conrad Wireless Pool Thermometer

https://www.conrad.at/de/schwimmbecken-thermometer-silber-672182.html

Frequency: 433 Mhz

The .cu8 files are named after the temperatures shown on the display (115 = 11.5°C, 259 = 25.9°C, etc.).

Here are some read-outs after analyzing the files with "rtl_433 -r XXX.cu8 -A":

```
[02] {36} fe d3 6e 6e e0 : 11111110 11010011 01101110 01101110 1110	30.4°C
[02] {36} fe d3 be 6e d0 : 11111110 11010011 10111110 01101110 1101	28.4°C
[02] {36} fe d3 e6 6e 60 : 11111110 11010011 11100110 01101110 0110	27.4°C
[01] {36} fe d4 0e 6e 10 : 11111110 11010100 00001110 01101110 0001	26.4°C
[01] {36} fe d4 5e 6e b0 : 11111110 11010100 01011110 01101110 1011	24.4°C
[02] {36} fe d3 de 6e 10 : 11111110 11010011 11011110 01101110 0001	27.6°C
[01] {36} fe d3 e2 6e a0 : 11111110 11010011 11100010 01101110 1010	27.5°C
[02] {36} fe d3 e6 6e 60 : 11111110 11010011 11100110 01101110 0110	27.4°C
```
