# Fine Offset WH0290 / Ambient Weather PM25 Wireless Air Quality Monitor

- [Fine Offset WH0290](http://www.foshk.com/Other_sensors/WH0290.html)
- [Ambient Weather PM25](https://www.ambientweather.com/ampm25.html)

- Wireless Air Quality Monitor
- PM 2.5 measure range: 0~999ug/m3

Sample files:
- 10.cua Capture for a reading of 10ug/m3
- 11.cua Capture for a reading of 11ug/m3
- 12.cua Capture for a reading of 12ug/m3

Analysis:
```
rtl_433 -F json -R 0 -X 'n=PM25,m=FSK_PCM,s=58,l=58,r=1500,preamble=aaaa2dd4' -r 10.cu8
{"time" : "@0.304040s", "model" : "PM25", "count" : 1, "num_rows" : 1, "rows" : [{"len" : 68, "data" : "42cc4064406ee4441"}], "codes" : ["{68}42cc4064406ee4441"]}
{"time" : "@0.342584s", "model" : "PM25", "count" : 1, "num_rows" : 1, "rows" : [{"len" : 68, "data" : "42cc4064406ee4441"}], "codes" : ["{68}42cc4064406ee4441"]}
```

Has the usual fine offset padding a preamble aa aa followed by 2d d4, samples with the padding and preamble removed:
-  9: 42 cc 40 5a 40 64 15 61 9
- 10: 42 cc 40 64 40 6e e4 44 1
- 11: 42 cc 40 6e 40 78 df 53 9
- 12: 42 cc 40 78 40 82 87 0f 9
- 14: 42 cc 40 8c 40 96 d3 83 9
- 41: 42 cc 41 9a 41 ae c1 99 9

Data layout:
```
      aa 2d d4 42 cc 41 9a 41 ae c1 99 9
               FF DD ?P PP ?A AA ?? CC
```
  - F: 8 bit Family Code?
  - D: 8 bit device id?
  - ?: 2 bits ?
  - P: 14 bit PM2.5 reading in ug/m3
  - ?: 2 bits ?
  - A: 14 bit PM10 reading in ug/m3
  - ?: 8 bits ?
  - C: 8 bit Checksum of previous 7 bytes (binary sum truncated to 8 bit)

This is advertised as a 2.5u monitor, but the [Honeywell HPM](https://sensing.honeywell.com/sensors/particle-sensors/HPM-series) sensor appears to have 10u capability as well, it looks like it may be sending the 10u reading as well.  I haven't been able to capture any readings higher than 45, the readings I have collected correspond to 3rd and 4th bytes. The advertised maximum range is 999u, so I'm guessing 14 bits are used (0000.0 - 9999.0, 0x0000 - 0x2706). In all of my sample the first two bits in byte 3 are always 01 (01.. ....), maybe one of those is the battery indicator, but they seem to repeat on the 10u reading.
