# Fine Offset WH65B

This is the sensor array for the Fine Offset WH2900.

http://www.foshk.com/Wifi_Weather_Station/WH2900.html

Specifically, my unit is from the Ambient Weather WS-2902A.

https://www.ambientweather.com/amws2902.html

This same sensor array is used in three other Ambient Weather offerings
so far.

https://www.ambientweather.com/amws1900.html

https://www.ambientweather.com/amws2000.html

https://www.ambientweather.com/amws1500.html

They sell the sensor array separately here.

https://www.ambientweather.com/amws2902array.html

Here's a link to the FCC documents for this sensor.

https://fccid.io/WA5WH65BV1


I believe this array collects and sends this data.

o Outdoor Temperature
o Outdoor Humidity
o Solar Radiation
o UV
o Rain
o Wind Direction
o Wind Speed
o Gust

The data that is collected in this directory was from a sensor that was
indoors.  I think the temperature was about 78F and the humidity was about 58%.
Of course, there was no wind and I don't really know what direction the
vane was pointing.  There wasn't much light and no rain.

I'm not very familiar with rtl_433.  But I noticed here:

https://github.com/merbanan/rtl_433/issues/764

some rtl_433 commands that seem to produce reasonable output with these 
data files as well.  Actually, this protocol may be mostly implemented already.
Hopefully, my data files can get this sensor array protocol fully implemented.
