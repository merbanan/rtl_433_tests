TFA Pool thermometer test signals
====================
Cat nr.: 30.3160
http://www.amazon.de/TFA-Dostmann-Funk-Poolthermometer-Miami-30-3033/dp/B0017CIXL8
![alt tag](http://tfa-dostmann.de/uploads/tx_prodkat/303160gross.jpg)

bits from 13 to 25 describes the temperature:

25.1C:
11010111 01100000 11111011 0111

19.7C with different device id:
01000100 10100000 11000101 0110

if value exceeds 1024, take temperature vill be negative, take 1's complement:
if (temp>(1<<11)) {
  temp = ((1<<12) - temp)*-1;
}

