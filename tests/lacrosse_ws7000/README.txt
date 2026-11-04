# Lacrosse WS7000/2500 Sensors (#1029)

s.a. https://github.com/merbanan/rtl_433/issues/1029

- WS2500-19 brightness sensor
- WS7000-20 meteo sensor (temperature/humidity/pressure)
- WS7000-16 Rain Sensor
- WS7000-15 wind sensor

protocol description attached to this issue
based on http://www.f6fbb.org/domo/sensors/index.php
and http://plevenon-meteo.info/technique/station/WS2500_sensors_infos.html

Lacrosse WS2500-19
Frame: 5=0101 7=0111 8=1000 2=0010 5=0101 2=0010 9=1001 9=1001 8=1000 7=0111 3=0011
Light = 52800 lux;
Exposure = 899 min ;

Lacrosse WS7000-15
Frame: 3=0011 7=0111 5=0101 2=0010 1=0001 0=0000 0=0000 8=1000 A=1010 9=1001
Windspeed = 12.5 km/h;
Direction = 200 degrees +/- 0.1 degree;

Lacrosse WS7000-16
Frame: 2=0010 7=0111 E=1110 2=0010 B=1011 2=0010 B=1011
Counts = 2862;

Lacrosse WS7000-20
Frame: 4=0100 F=1111 4=0100 5=0101 2=0010 9=1001 7=0111 4=0100 5=0101 9=1001 7=0111 2=0010 B=1011 9=1001
Temperature = -25.4 C;
Humidity = 47.9 %;
Pressure = 995 hPa;

Lacrosse WS7000-22
Frame: 1=0001 F=1111 4=0100 5=0101 2=10 9=1001 7=0111 4=0100 7=0111 B=1011
Temperature = -25.4 C;
Humidity = 47.9 %;

Lacrosse WS7000-27
Frame: 0=0000 F=1111 3=0011 5=0101 2=0010 B=1011 9=1001
Temperature = -25.3;
