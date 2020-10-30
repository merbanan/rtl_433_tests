LaCrosse Technology View TH3 Thermo/Hygro Sensor

Product Pages:
https://www.lacrossetechnology.com/products/ltv-th3  (sensor)
https://www.lacrossetechnology.com/products/S84060   (console)

Specifications:
- Outdoor Temperature Range: -40 C to 60 C
- Outdoor Humidity Range: 10 to 99 %RH

Packet Structure:

  SYN:32h ID:24h ?:4b SEQ:3b ?:1b TEMP:12d HUM:12d CHK:8h END:

  CHK is CRC-8 poly 0x31 init 0x00 over 7 bytes following SYN

Flex_decoder:  'n=TH3,m=FSK_PCM,s=104,l=104,r=9600'

Many of the 915MHz LTV sensors use the same signal parameters.  No product ID code
is embedded in the packet so the only way to determine which model is transmitting
data is based solely on packet length.  It is possible that model information is
encoded in the Sensor ID but that remains to be discovered.  Note that the sensor
ID is fixed (does not change following battery replacement) and should match the
barcode on the bottom of the sensor.

I have yet to determine the decoding of the flags (lable: unknown) for this sensor.

file: g119_915M_1000k.cu8
codes: {253}fff8000055555555695516ea08842880139812c4800000000000000000000000
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.077943s
model     : LaCrosse-TH3 Sensor ID : 110851
Sequence  : 0            unknown   : 0             Temperature: 22.7 C
Humidity  : 37 %         Integrity : CRC


file: g498_915M_1000k.cu8
codes: {253}fff8000055555555695516ea088428840e202a89800000000000000000000000
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.077933s
model     : LaCrosse-TH3 Sensor ID : 110851
Sequence  : 4            unknown   : 0             Temperature: 5.2 C
Humidity  : 85 %         Integrity : CRC

