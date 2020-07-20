# ecowitt WH41 - PM2.5 sensor

- This sensor comes in several frequency variations, I have the 915Mhz model. It was purchased from Amazon.com in the US in June of 2020.
- The default behavior is to send a data packet every 10 minutes, these two files g001 and g002 are this standard update packet 10 minutes apart.
- On startup (ie remove the battery and re-insert), the unit sends a large pattern that appears truncated, so I did not include that.
- Signals captured on rtl_433 debian package version 20.02 with RTLSDR v3, and `rtl_433 -S unknown -f 915M -s 2400000`

log of capture:

```
Sample rate set to 2400000 S/s.
Tuner gain set to Auto.
Tuned to 915.000MHz.
*** Saving signal to file g001_915M_2400k.cu8 (122804 samples, 262144 bytes)
*** Saving signal to file g002_915M_2400k.cu8 (127421 samples, 262144 bytes)
Signal bigger than buffer, signal = 8388608 > buffer 3145728 !!
*** Saving signal to file g003_915M_2400k.cu8 (4136926 samples, 3145728 bytes)
```

![exterior and dimensions](wh41_1.jpg?raw=true)
![base](wh41_2.jpg?raw=true)

