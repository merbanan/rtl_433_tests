# Opus/Imagintronix XH300 / XT300 Soil Moisture Sensor

https://www.plantcaretools.com/product/wireless-moisture-monitor/

Sensor trasmite data every 30 sec.
It use basic OOK with pulse with modulation.

```
$ rtl_433 -X 'n=XT300,m=OOK_PWM,s=540,l=950,g=10000,r=31408,match=0xff56,bits=48' -R 0
time      : 2019-01-06 00:04:07
model     : XT300        count     : 2             num_rows  : 2             rows      : 
len       : 48           data      : ff560531ff8b, 
len       : 48           data      : ff560531ff8b
codes     : {48}ff560531ff8b, {48}ff560531ff8b
```



    FF ID SM TT ?? CC
{48}ff 56 05 43 ff 9d


SM: soil moisure (decimal 05 -> 99 %)
TT: temperature °C + 40°C (decimal)
??: always FF... maybe spare bytes
CC: check sum (simple sum) except 0xFF preamble

