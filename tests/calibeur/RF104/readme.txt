Shenzhen Calibeur Industries Co. Ltd Wireless Thermometer RF-104 Temperature/Humidity sensor
 * aka Biltema Art. 84-056 (Sold in Denmark)
 * aka ...

NB. Only 3 unique sensors can be detected!

Update (LED flash) each 2:53

Pulse Width Modulation with fixed rate and startbit 
Startbit     = 390 samples = 1.56 ms
Long pulse   = 560 samples = 2.24 ms = Logic 1
Short pulse  = 190 samples = 0.76 ms = Logic 0
Pulse rate   = 740 samples = 2.96 ms
Burst length = 81000 samples = 324 ms

Sequence of 5 times 21 bit separated by start bit (total of 111 pulses)
S 21 S 21 S 21 S 21 S 21 S

Channel number is encoded into fractional temperature
Temperature is oddly arranged and offset for negative temperatures = <6543210> - 41 C
Allways an odd number of 1s (odd parity) 

Encoding legend:
f = fractional temperature + <ch no> * 10
0-6 = integer temperature + 41C
p = parity
H = Most significant bits of humidity [5:6]
h = Least significant bits of humidity [0:4]

LSB               MSB
ffffff4501236pHHhhhhh Encoding
111100011010011001001 -3,5C 50% Ch1
101100011001010101000  0,3C 66% Ch1
111100010101001011100  1.5C 39% Ch1
001100010111010110101  5,2C 85% Ch1
100010111000000111111  8,7C 95% Ch1 
110010111010000111111 12,9C 95% Ch1
001100111001010111111 16,2C 95% Ch1
110010110101010110111 17,9C 93% Ch1
011100110111000101100 21,4C 70% Ch1
000010000000101011101 23,6C 55% Ch1
100110000100100100001 25.5C 80% Ch2
001100001100100000011 26.2C 24% Ch1
101100001100101000011 26.3C 56% Ch1
011100001100110000011 26.4C 24% Ch1
111100001100100000011 26.5C 24% Ch1
110110001100100110110 26.7C 77% Ch2
010010001100100000011 26.8C 24% Ch1
011001001100100101100 26.8C 70% Ch3
110100000010100011101 27.1C 23% Ch1
010010000010100000111 27.8C 28% Ch1
110100001010110010111 28.1C 29% Ch1
101100001010111000100 28.3C 36% Ch1
101100001010111001000 28.3C 34% Ch1
100010001110110111111 30.7C 95% Ch1

