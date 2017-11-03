TFA Pool thermometer test signals
====================
Cat nr.: 30.3160
http://www.amazon.de/TFA-Dostmann-Funk-Poolthermometer-Miami-30-3033/dp/B0017CIXL8
![alt tag](http://tfa-dostmann.de/uploads/tx_prodkat/303160gross.jpg)


01
======
```
25.1C:
11010111 01100000 11111011 0111
25.5C:
00010111 01100000 11111111 0111
25.8C:
01100111 01100001 00000010 0111
25.9C:
01110111 01100001 00000011 0111
```
02
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

