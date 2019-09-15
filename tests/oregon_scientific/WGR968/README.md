# WGR968 Anemometer

![WGR968 Anemometer](https://github.com/PuceBaboon/rtl_433_tests/tree/master/tests/oregon_scientific/07/Oregon-Scientific_WGR968_Anemometer.jpg)

This directory contains sample files for the Oregon Scientific WGR968 anemometer, showing the problem with out-of-sequence decoding of the nibbles for wind direction "quadrant" in the devices/oregon_scientific.c file.

gfile004.data - Output shows direction as "902", but should be 290.

gfile005.data - Output shows direction as "113", but should be 311.

gfile006.data - Output shows direction as "213", but should be 321.

gfile009.data - Output shows direction as "183", but should be 318.


Note that the readings were made in the space of a few minutes (the other files in the sequence are data from the THGR968 and BHTR968 sensors associated with this fairly old weather station and can be uploaded if deemed useful).

My quick-and-dirty demonstration fix for this issue is to change line #255 from:-

<code>float quadrant = (((msg[4] &0x0f)*100)+((msg[4]>>4)*10) + ((msg[5]>>4)&0x0f));</code>

to:-

<code>float quadrant = (((msg[4] &0x0f)*10) + ((msg[4]>>4)&0x0f) + (((msg[5]>>4)&0x0f)*100));</code>

