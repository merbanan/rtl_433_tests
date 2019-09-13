Axel wireless temperature sensor
==========================================================================

Folder 01 contains test files and information about Axel wireless temperature sensor. I have used Astrometa DVB-T / DVB-T2 usb-device in my Raspberry Pi model B (Raspbian OS) to collect all the binary data with command: "./rtl_433 -a".

Folder 02 contains PHP-scripts to read temperature values from sqlite-database and to create a line graph using JpGraph-library.

==========================================================================
Here are some commands and scripts I have used to convert temperature binary data to decimal values and automatically inserting values to a local sqlite3 database.
==========================================================================

==========================================================================
Writes rtl_433 output to the text file and running in background:
==========================================================================

./rtl_433 -a 2>testi001.txt &

==========================================================================
Creates sqlite3 table for temperature values:
==========================================================================

BEGIN;
CREATE TABLE temp(id INTEGER PRIMARY KEY, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, temperature NUMERIC);
COMMIT;

==========================================================================
Converts binary values to decimal values and insert celsius value to sqlite3 database:
==========================================================================

#!/bin/bash

# bash script "calculate_temp.sh" to decode 42 bit Axel 433 Mhz temperature sensor
# as captured by rtl_433 -a
#
# script has no real error checking and is not optimized
# (e.g. loops or better variable handling)
#
# 2016-09-12, keonen

# finds the last line with string "[12]" from rtl_433 output's text-file and sets it to the $parameter value
parameter=$(grep "\[12\]" /home/pi/Scripts/rtl_433/build/src/testi001.txt | tail -n 1)

# check length declaration (bits 7 and 8)
length=${parameter:6:2}
if [ $length != "42" ]
then
    echo "Length declaration not 42, exiting."
    exit 1
fi

# remove unused characters and spaces
nospace=$(echo $parameter | cut -d" " -f 10-15 | tr -d " ")

# get binary values from specific locations
bitsfrom22to25=${nospace:22:4}
bitsfrom18to21=${nospace:18:4}
bitsfrom14to17=${nospace:14:4}

# convert bin to dec
binaryvalue=$(echo $bitsfrom22to25$bitsfrom18to21$bitsfrom14to17)

decimalvalue=$(echo "ibase=2;obase=A;$binaryvalue" | bc)

fahrenheitvalue=$(echo "scale=1;$decimalvalue / 10 - 90" | bc -l)
echo "Fahrenheit = "$fahrenheitvalue

celsiusvalue=$(echo "scale=2;($fahrenheitvalue - 32 ) * 5 / 9" | bc -l)
echo "Celsius = "$celsiusvalue

# insert celsius value to sqlite3 database
sqlite3 /home/pi/Scripts/rtl_433/build/src/temperature.db  "insert into temp (temperature) values ($celsiusvalue);"

==========================================================================
Added new task to crontab:
==========================================================================

*/5 * * * * /home/pi/Scripts/rtl_433/build/src/calculate_temp.sh

==========================================================================
Some temperature data from sqlite3 database:
==========================================================================

sqlite> select * from temp;
1|2016-09-13 08:05:04|11.66
2|2016-09-13 08:32:15|12.05
3|2016-09-13 08:35:01|11.88
4|2016-09-13 08:40:01|12.05
5|2016-09-13 08:45:01|12.27
6|2016-09-13 08:50:01|12.5

==========================================================================

