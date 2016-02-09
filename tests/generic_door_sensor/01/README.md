# Generic Door Sensor

This is a cheap door/window contact sensor available from various vendors on [Aliexpress](http://www.aliexpress.com/item/High-Quality-Intelligent-433Mhz-Wireless-Magnetic-Door-Sensor-Window-Contact-Door-Alarm-For-Home-Alarm-Burglar/32507992813.html). It is based on a reed switch and the HS1527 encoder.

## Protocol

See page 2 of the [datasheet](http://sc-tech.cn/en/hs1527.pdf). The first 20 bits are the address code. The remaining 4 bits are always '1110' (pin 8/K3 is tied to the ground).

