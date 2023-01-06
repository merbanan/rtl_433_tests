# Fuzhou EMAX Weather Sensor 

Emax 5-in-1 Station EM9930W6, 
Rebrand ref : Optex 99040 SM040, Infactory FWS-1200, Newentor Q9

This weather station are composed of 2 x 433.92 MHz devices :
- 1 External Temp/Hum : already decode by rtl_433 under Altronics X7064 temperature and humidity sensor.
- 1 External 5-in-1 Weather sensor with Rain Gauge/Wind Speed/Wind Direction/UV index/Lux/Temperature/Humidity not properly decode by Altronics X7064 temperature and humidity sensor, bad humidity decoding and missing all the rest.

```
rtl_433 -X "n=STATION,m=FSK_PCM,s=90,l=90,g=1200,r=9000,preamble={40}aaaacaca54" -F json
```

Result for the 5-in-1 :
```
{"time" : "2023-01-06 14:44:01", "model" : "STATION", "count" : 3, "num_rows" : 6, "rows" : [{"len" : 27, "data" : "fffc000"},
{"len" : 276, "data" : "aa0459410623420101011201180101490405060708091011121314151617e1d0e2000"}, {"len" : 33, "data" : "fffff0000"}, 
{"len" : 276, "data" : "aa0459410623420101011201180101490405060708091011121314151617e1d0e2000"}, {"len" : 33, "data" : "fffff0000"}, 
{"len" : 276, "data" : "aa0459410623420101011201180101490405060708091011121314151617e1d0e2000"}], 
"codes" : ["{27}fffc000", "{276}aa0459410623420101011201180101490405060708091011121314151617e1d0e2000", "{33}fffff0000", "{276}aa0459410623420101011201180101490405060708091011121314151617e1d0e2000", "{33}fffff0000", "{276}aa0459410623420101011201180101490405060708091011121314151617e1d0e2000"]}
```
Result for the Temp/Hum :
```
{"time" : "2023-01-06 14:47:33", "model" : "STATION", "count" : 3, "num_rows" : 3, "rows" : [
{"len" : 276, "data" : "aaa123d1a63aa53faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa49aa000"}, 
{"len" : 276, "data" : "aaa123d1a63aa53faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa49aa000"}, 
{"len" : 276, "data" : "aaa123d1a63aa53faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa49aa000"}], 
"codes" : ["{276}aaa123d1a63aa53faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa49aa000", "{276}aaa123d1a63aa53faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa49aa000", "{276}aaa123d1a63aa53faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa49aa000"]}
```

I bought this weather station, Optex SM40 990040, but I have a wrong decode situation.

https://www.bricodepot.fr/catalogue/station-meteo-couleur-professionnelle-connectee/prod84533/
![image](https://user-images.githubusercontent.com/62882637/210964198-6144406c-f529-4525-ab68-d878b485e08b.png)

After a deep dive I found the reason of the bad decode and share here my findings ;

The Rain Wind multi-sensor provides more data than the Temp/Hum sensor and not in the same order.

Here the differences :
Temp/Hum Sensor :
    AA KC II IB AT TA AT HH AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA SS

default empty = 0xAA
    
- K: (4 bit) Kind of device, = A if Temp/Hum Sensor or = 0 if Weather Rain/Wind station
- C: (4 bit) channel ( = 4 for Weather Rain/wind station)
- I: (12 bit) ID
- B: (4 bit) BP01: battery low, pairing button, 0, 1
- T: (12 bit) temperature in F, offset 900, scale 10
- H: (8 bit) humidity %
- A: (4 bit) fixed values of 0xA
- S: (8 bit) checksum

Raw data:

    FF FF AA AA AA AA AA CA CA 54
    AA A1 6E 95 A6 BA A5 3B AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA AA D4
    AA 00 0

Format string:

    12h CH:4h ID:12h FLAGS:4b TEMP:4x4h4h4x4x4h HUM:8d 184h CHKSUM:8h 8x

Decoded example:

    aaa CH:1 ID:6e9 FLAGS:0101 TEMP:6b5 HUM:059 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa CHKSUM:d4 000


Emax EM3390W6 Rain / Wind speed / Wind Direction / Temp / Hum / UV / Lux

Weather Rain/Wind station : humidity not at same byte position !
    AA 04 II IB 0T TT HH 0W WW 0D DD RR RR 0U LL LL 04 05 06 07 08 09 10 11 12 13 14 15 16 17 xx SS yy

default empty/null = 0x01 => value = 0
  
- K: (4 bit) Kind of device, = A if Temp/Hum Sensor or = 0 if Weather Rain/Wind station
- C: (4 bit) channel ( = 4 for Weather Rain/wind station)
- I: (12 bit) ID
- B: (4 bit) BP01: battery low, pairing button, 0, 1
- T: (12 bit) temperature in F, offset 900, scale 10
- H: (8 bit) humidity %
- R: (16) Rain
- W: (12) Wind speed
- D: (9 bit) Wind Direction
- U: (4 bit) UV index
- L: (1 + 15 bit) Lux value, if first bit = 1 , then x 10 the rest.
- A: (4 bit) fixed values of 0xA
- 0: (4 bit) fixed values of 0x0
- xx: incremental value each tx
- yy: incremental value each tx yy = xx + 1
- S: (8 bit) checksum

Raw Data: the beginning of the Preamble is not exactly the same,

    ff ff 80 00 aa aa aa aa aa ca ca 54
    aa 04 59 41 06 1f 42 01 01 01 81 01 16 01 01 01 04 05 06 07 08 09 10 11 12 13 14 15 16 17 9d ad 9e
    0000

Format string:

    8h K:4h CH:4h ID:12h Flags:4b 4h Temp:12h Hum:8h 4h Wind:12h 4h Direction: 12h Rain: 16h 4h UV:4h Lux:16h  112h xx:8d CHKSUM:8h

Decoded example:

    aa KD:0 CH:4 ID:594 FLAGS:0001 0 TEMP:61f (66.7F) HUM:42 (66%) Wind: 101 ( = 000 * 0.2 = 0 kmh) 0 Direction: 181 ( = 080 = 128°) Rain: 0116 ( 0015 * 0.2  = 4.2 mm) 0 UV: 1 (0 UV) Lux: 0101 (0 Lux) 04 05 ...16 17 xx:9d CHKSUM:ad yy:9e

So I rewrite the decoder in order to get these information, notice that the gap needed to be changed from 900 to 1200.
Because I get the both sensors, Temp/Hum + Rain/Wind, I was able to test the decoding correctly.


