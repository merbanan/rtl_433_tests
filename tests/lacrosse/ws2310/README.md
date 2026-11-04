# LaCrosse WS-2310TWC

Lacrosse Weather Station WS-2310TWC (The Weather Channel branded WS2310)

Notes:
On initial power up of the sensor data is transmitted every 8 seconds for 128 transmissions.
The Update Speed indicated in nibble 6 is set as 100P = 8 seconds.
The 129th transmission is sent 8 seconds later as well, but the Update Speed is set to 111P = 128 seconds.
Subsequent transmissions are sent every 128 seconds.  There is documentaion that says if the Wind Speed is
over 22.36 mph the transmissions will happen every 32 seconds.
The Humidity will be set to AA in the first 4 transmissions and then will have the correct value.

```
09 0 25 7 8 529 AD 6  LaCrosse WS 25: Temperature 22.9 C / 73.2 F
09 5 25 7 8 AAA 55 C  LaCrosse WS 25: Humidity Error
09 6 25 7 8 000 FF 3  LaCrosse WS 25: Rain 0.00 mm / 0.00 in
09 7 25 7 8 00C FF 0  LaCrosse WS 25: Wind Dir 270.0  Speed 0.0 m/s / 0.0 mph
09 0 25 7 8 529 AD 6  LaCrosse WS 25: Temperature 22.9 C / 73.2 F
09 5 25 7 8 AAA 55 C  LaCrosse WS 25: Humidity Error
09 6 25 7 8 000 FF 3  LaCrosse WS 25: Rain 0.00 mm / 0.00 in
09 7 25 7 8 00C FF 0  LaCrosse WS 25: Wind Dir 270.0  Speed 0.0 m/s / 0.0 mph
```
