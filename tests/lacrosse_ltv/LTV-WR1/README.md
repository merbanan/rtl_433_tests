LaCrosse Technology View WR1 Multi Sensor (Wind/Rain)

Product Pages:
https://www.lacrossetechnology.com/products/ltv-wr1  (sensor)
https://www.lacrossetechnology.com/products/S84060   (console)

Specifications:
- Wind Speed Range: 0 to 188 kmh
- Degrees of Direction: 0 to 359 degrees
- Rainfall 0 to 9999.9 mm
- Update Interval: Every 30 Seconds

Packet Structure:

  SYN:32h ID:24h ?:4b SEQ:3d ?:1b WSPD:12d WDIR:12d RAIN1:12d RAIN2:12d CHK:8h

  CHK is CRC-8 poly 0x31 init 0x00 over 7 bytes following SYN

Flex_decoder:  'n=WR1,m=FSK_PCM,s=104,l=104,r=9600'

Many of the 915MHz LTV sensors use the same signal parameters.  No product ID code
is embedded in the packet so the only way to determine which model is transmitting
data is based solely on packet length.  It is possible that model information is
encoded in the Sensor ID but that remains to be discovered.  Note that the sensor
ID is fixed (does not change following battery replacement) and should match the
barcode on the bottom of the sensor.

I have yet to determine the decoding of the flags (lable: unknown) for this sensor.
Rainfall information is provided as transmitted by the sensor (raw_rain1 & raw_rain2)
until such time that I understand how to map them to 'rain_mm'.


file: g165_915M_1000k.cu8
codes: {156}aaaaaaab4aa8b7506411e868328374142aab190
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.098397s
model     : LaCrosse-WR1 Sensor ID : 19047a
Sequence  : 5            unknown   : 16            Wind speed: 20.2 km/h
Wind direction: 221      raw_rain1 : 050           raw_rain2 : aaa
Integrity : CRC


file: g222_915M_1000k.cu8
codes: {156}aaaaaaab4aa8b7506411e84810c03419aaaae90
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.098413s
model     : LaCrosse-WR1 Sensor ID : 19047a
Sequence  : 1            unknown   : 16            Wind speed: 6.7 km/h
Wind direction: 13       raw_rain1 : 066           raw_rain2 : aaa
Integrity : CRC


file: g2750_915M_1000k.cu8
codes: {156}aaaaaaab4aa8b7506411e8782040f01aaaaa910
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.098411s
model     : LaCrosse-WR1 Sensor ID : 19047a
Sequence  : 7            unknown   : 16            Wind speed: 12.9 km/h
Wind direction: 60       raw_rain1 : 06a           raw_rain2 : aaa
Integrity : CRC

