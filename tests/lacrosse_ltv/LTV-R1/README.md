LaCrosse Technology View R1 Rainfall Gauge

Product Pages:
https://www.lacrossetechnology.com/products/ltv-r1     (sensor)
https://www.lacrossetechnology.com/products/724-2310   (console)

Specifications:
- Rainfall 0 to 9999.9 mm

Packet Structure:

  PRE:32h SYN:32h ID:24h ?:4b SEQ:3d ?:1b RAIN:16d RAIN:16d CHK:8h END:32h

  CHK is CRC-8 poly 0x31 init 0x00 over 7 bytes following SYN

Flex_decoder:  'n=R1,m=FSK_PCM,s=104,l=104,r=9600'

Many of the 915MHz LTV sensors use the same signal parameters.  No product ID code
is embedded in the packet so the only way to determine which model is transmitting
data is based solely on packet length.  It is possible that model information is
encoded in the Sensor ID but that remains to be discovered.  Note that the sensor
ID is fixed (does not change following battery replacement) and should match the
barcode on the bottom of the sensor.

I have yet to determine the decoding of the flags (lable: unknown) for this sensor.
Rainfall information is provided as transmitted by the sensor (raw_rain1 & raw_rain2)
until such time that I understand how to map them to 'rain_mm'.

The sensor used to generate these samples often times repeats a given packet several
times.  This behaviour is not understood at this time.  I believe the dupes should
be ignored by the end user if the raw_rain values and sequence number match that of
the previous packet.


file: g002_915M_250k.cu8
codes: {261}fff8000055555555695516ea1c01910700550a3549800000000000000000000000
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.159060s
model     : LaCrosse-R1  Sensor ID : 380322
Sequence  : 7            unknown   : 0             raw_rain1 : 00aa
raw_rain2 : 146a         Integrity : CRC


file: g005_915M_250k.cu8
codes: {261}fff8000055555555695516ea1c01910000550d3040800000000000000000000000
       {267}ffffe0000155555555a5545ba870064400015434c10200000000000000000000000
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.127724s
model     : LaCrosse-R1  Sensor ID : 380322
Sequence  : 0            unknown   : 0             raw_rain1 : 00aa
raw_rain2 : 1a60         Integrity : CRC
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.127724s
model     : LaCrosse-R1  Sensor ID : 380322
Sequence  : 0            unknown   : 0             raw_rain1 : 00aa
raw_rain2 : 1a60         Integrity : CRC


file: g016_915M_250k.cu8
codes: {259}fff8000055555555695516ea1c019103005513688200000000000000000000000
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.159272s
model     : LaCrosse-R1  Sensor ID : 380322
Sequence  : 3            unknown   : 0             raw_rain1 : 00aa
raw_rain2 : 26d1         Integrity : CRC

