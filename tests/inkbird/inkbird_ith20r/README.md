# Inkbird ITH-20R
A 433MHz FSK wireless temperature and humidity sensor with base station
https://www.ink-bird.com/products-data-logger-ith20r.html

## Format

```Total packet length 14563 bits:
Preamble: aa aa aa ... aa aa (14400 on-off sync bits)
Sync Word (16 bits): 2DD4
Data (147 bits):
Byte Sample Comment
0-2 D3910F Always the same across devices, a device type?
3 00 00 - normal work , 40 - unlink sensor (button pressed 5s), 80 - battery replaced
4 01 Changes from 1 to 2 if external sensor present
5-6 0301 Unknown (also seen 0201), sw version?
7 58 Battery % 0-100
8-9 A221 Device id, always the same for a sensor but each sensor is different
10-11 D600 Temperature in °C * 10, little endian, so 0xD200 is 210, 21.0°C or 69.8°F
12-13 F400 Temperature °C * 10 for the external sensor, 0x1405 if not connected
14-15 D301 Relative humidity % * 10, little endian, so 0xC501 is 453 or 45.3%
16-17 38FB CRC16
18 0 Unknown 3 bits (seen 0 and 2)

CRC16 (bytes 0-15), without sync word):
poly=0x8005 init=0x2f61 refin=true refout=true xorout=0x0000 check=0x3583 residue=0x0000
```
## Notes
The sensors broadcast roughly every 80 seconds unless there are substantial temperature or humidity changes in which case they will broadcast more often. The sensor module has a port for connecting an external temperature probe. Doing so changes a single byte counter and causes the secondary temperature value to be set to something other than 0x1405.

