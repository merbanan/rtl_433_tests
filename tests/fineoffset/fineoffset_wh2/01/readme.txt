Fine Offset Electronics WH2 wireless Temperature/Humidity sensor 
 * aka Agimex Rosenborg 66796 (sold in Denmark)
 * aka ClimeMET CM9088 (Sold in UK)
 * aka ...

The sensor sends two identical packages of 48 bits each ~50s. The bits are PWM modulated with On Off Keying
Long pulse is 1, short is 0. The pulse gap is constant and hence the pulse rate and total burst length varies.

The data is grouped in 6 bytes / 12 nibbles
[pre] [pre] [type] [id] [id] [temp] [temp] [temp] [humi] [humi] [crc] [crc]

pre is always 0xFF
type is always 0x4 (may be different for different sensor type?)
id is a random id that is generated when the sensor starts
temp is 12 bit signed magnitude scaled by 10 celcius
humi is 8 bit relative humidity percentage
 
Based on reverse engineering with gnu-radio and the nice article here:
http://lucsmall.com/2012/04/29/weather-station-hacking-part-2/

Number of pulses:
Long pulse   = 366 samples = 1.5 ms = Logic 1
Short pulse  = 120 samples = 0.5 ms = Logic 0
Gap width    = 260 samples = 1.0 ms
Burst length = 18240-30000 samples = 72-120 ms (Theoretically)

