# Alecto v1 protocol

Documentation also at http://www.tfd.hu/tfdhu/files/wsprotocol/auriol_protocol_v20.pdf
Message Format: (9 nibbles, 36 bits):
Please note that bytes need to be reversed before processing!

## Format for Temperature Humidity

    AAAAAAAA BBBB CCCC CCCC CCCC DDDDDDDD EEEE

 - RC       Type Temperature___ Humidity Checksum
 - A = Rolling Code / Device ID
      Device ID: AAAABBAA BB is used for channel, base channel is 01
      When channel selector is used, channel can be 10 (2) and 11 (3)
 - B = Message type (xyyz = temp/humidity if yy <> '11') else wind/rain sensor
      x indicates battery status (0 normal, 1 voltage is below ~2.6 V)
      z 0 indicates regular transmission, 1 indicates requested by pushbutton
 - C = Temperature (two's complement)
 - D = Humidity BCD format
 - E = Checksum

## Format for Rain

    AAAAAAAA BBBB CCCC DDDD DDDD DDDD DDDD EEEE

 - RC       Type      Rain                Checksum
 - A = Rolling Code /Device ID
 - B = Message type (xyyx = NON temp/humidity data if yy = '11')
 - C = fixed to 1100
 - D = Rain (bitvalue * 0.25 mm)
 - E = Checksum

## Format for Windspeed

    AAAAAAAA BBBB CCCC CCCC CCCC DDDDDDDD EEEE

 - RC       Type                Windspd  Checksum
 - A = Rolling Code
 - B = Message type (xyyx = NON temp/humidity data if yy = '11')
 - C = Fixed to 1000 0000 0000
 - D = Windspeed  (bitvalue * 0.2 m/s, correction for webapp = 3600/1000 * 0.2 * 100 = 72)
 - E = Checksum
 - F = Checksum

## Device description

Windmeter WS3500 which holds wind and temp/hum. 1 package is wind data (this package) other package is below.
gfile001.data: AlectoV1 Wind Sensor ID: 44: Wind speed 5 units = 1.00 m/s: Wind gust 8 units = 1.60 m/s: Direction 135 degrees: Battery OK

WS3500 wind sensor sends also temp and humidity data in seperate package
gfile002.data
AlectoV1 Sensor 44 Channel 1: Temperature 28.8 C: Humidity 36 %: Battery OK

WS3500 rain sensor
gfile004.data AlectoV1 Rain Sensor ID: 12: Rain 188.00 mm/m2: Battery OK

Ventus W155 temp/hygrometer (same protocol):
gfile005.data: AlectoV1 Sensor ID: 247 Channel 3: Temperature 23.7 C: Humidity 62 %: Battery OK

