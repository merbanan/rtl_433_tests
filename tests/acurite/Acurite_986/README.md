# Acurite 986 Refrigerator / Freezer Thermometer

Manufacturer link: 
http://www.acurite.com/kitchen-gadgets/digital-freezer-refrigerator-thermometer-with-temperature-alarms-00986.html

## Acurite_TX_51.data

51 F, normal battery
* 2015-11-20 20:26:20 Acurite 986 sensor 0x427d - 1R: 10.6 C 51 F

## Acurite_986_neg5f_lowbatt.data

Negative temp, -5 F, low battery
* 2015-11-20 20:27:11 Acurite 986 sensor 0x10ac - 1R: low battery, status 01
* 2015-11-20 20:27:11 Acurite 986 sensor 0x10ac - 1R: -20.6 C -5 F

## Note about Bad CRCs in test data

The current PPM demodulator looses a bit in one of the messages.  The
message is repeated so one of the repeats contains all of the bits.
If the missing bit is 0, the CRC check will succeed, otherwise there
should be one good message, and one CRC error.

