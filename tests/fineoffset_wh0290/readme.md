***[Fine Offset WH0290](http://www.foshk.com/Other_sensors/WH0290.html)***

***[Ambient Weather PM25](https://www.ambientweather.com/ampm25.html)***

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
-  9: cc 40 5a 40 64 15 61 9
- 10: cc 40 64 40 6e e4 44 1
- 11: cc 40 6e 40 78 df 53 9
- 12: cc 40 78 40 82 87 0f 9
- 14: cc 40 8c 40 96 d3 83 9

Based on other fine offset devices:

2D D4 DD II PP ?? ?? ?? ?? ?

DD: Device ID CC?
II: Device Identifier?
PP: PM2.5 reading.

I haven't been able to capture any readings higher than 14, the readings I have collected correspond to 5th and 6th bytes after the preamble, but I'm not sure yet how values higher than 25 are handled.
