# Vauno additional sensor for EN8822C-1

https://www.amazon.co.uk/VAUNO-Additional-EN8822C-1-Hygrometer-Temperature/dp/B08ZCGYVHJ

* Manufacturer: Vauno
* Model No.: Additional sensor for EN8822C-1
* Measurable range: -40 °C ~ +70 °C
* 2 x 1.5V AAA battery
* Frequency 433.92 MHz
* 3 Channels
* LED is blinking on every TX
* TX-button (force send)

42-bit data packet format, repeated 6 times  
  IIIIIIII 00CCTTTT TTTTTTTT HHHHHHH0 0000???? ??  

  T = signed temperature * 10 in Celsius   
  C = channel 00=0, 01=1, 10=2
  I = sensor ID
  0 = unknown (always 0)  
  H = humidity
  ? = unknown (checksum?)

## Sample data 1 (g1148):
```
[00] {42} 85 10 f9 74 0c 40 : 10000101 00010000 11111001 01110100 00001100 01

Sensor ID	= 133 = 0x85
Channel		= 2
temp		= 249 = 0x000011111001
TemperatureC	= 24.9
hum    = 58% = 0x0111010
```

```
Analyzing pulses...
Total count:  269,  width: 1005.40 ms           (251349 S)
Pulse width distribution:
 [ 0] count:  269,  width:  604 us [592;620]    ( 151 S)
Gap width distribution:
 [ 0] count:  102,  width: 4108 us [4080;4236]  (1027 S)
 [ 1] count:  154,  width: 2052 us [2028;2152]  ( 513 S)
 [ 2] count:   12,  width: 8916 us [7568;9144]  (2229 S)
Pulse period distribution:
 [ 0] count:  102,  width: 4712 us [4684;4836]  (1178 S)
 [ 1] count:  154,  width: 2656 us [2632;2760]  ( 664 S)
 [ 2] count:   12,  width: 9520 us [8164;9752]  (2380 S)
Pulse timing distribution:
 [ 0] count:  269,  width:  604 us [592;620]    ( 151 S)
 [ 1] count:  102,  width: 4108 us [4080;4236]  (1027 S)
 [ 2] count:  154,  width: 2052 us [2028;2152]  ( 513 S)
 [ 3] count:   13,  width: 9000 us [7568;10004] (2250 S)
Level estimates [high, low]:  15945,    972
RSSI: -0.1 dB SNR: 12.1 dB Noise: -12.3 dB
Frequency offsets [F1, F2]:   -2157,      0     (-8.2 kHz, +0.0 kHz)
```

## Sample data 2 (g358):
```
[00] {42} af 0f a2 7c 01 c0 : 10101111 00001111 10100010 01111100 00000001 11

Sensor ID	= 175 = 0xaf
Channel		= 0
temp		= -93 = 0x111110100010
TemperatureC	= -9.3
hum    = 62% = 0x0111110
```

```
Analyzing pulses...
Total count:  269,  width: 1040.81 ms           (260203 S)
Pulse width distribution:
 [ 0] count:  269,  width:  584 us [572;596]    ( 146 S)
Gap width distribution:
 [ 0] count:  126,  width: 4092 us [4056;4208]  (1023 S)
 [ 1] count:  131,  width: 2044 us [2020;2204]  ( 511 S)
 [ 2] count:   11,  width: 9028 us [8996;9136]  (2257 S)
Pulse period distribution:
 [ 0] count:  126,  width: 4676 us [4644;4796]  (1169 S)
 [ 1] count:  131,  width: 2632 us [2600;2784]  ( 658 S)
 [ 2] count:   11,  width: 9616 us [9584;9724]  (2404 S)
Pulse timing distribution:
 [ 0] count:  269,  width:  584 us [572;596]    ( 146 S)
 [ 1] count:  126,  width: 4092 us [4056;4208]  (1023 S)
 [ 2] count:  131,  width: 2044 us [2020;2204]  ( 511 S)
 [ 3] count:   12,  width: 9108 us [8996;10004] (2277 S)
Level estimates [high, low]:  15972,   1228
RSSI: -0.1 dB SNR: 11.1 dB Noise: -11.3 dB
Frequency offsets [F1, F2]:    -423,      0     (-1.6 kHz, +0.0 kHz)
```