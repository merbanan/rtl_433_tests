Addon TPMS for RV's. This data comes from the model 618E with 10 tire pressure sensors purchased form Amazon
https://www.amazon.com/gp/product/B009BF9S4E/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&th=1

Recordings made with RTL-SDR.COM Blog V3 dongle 2-8-23 to 2-10-23. Tried using SDR# with the RTL_433 plugin running on a laptop running Windows 10 Pro but could not get repeatable results. I could not find a compiled version of RTL_433 that would run on my windows machine to be able to run RTL_433 from the command line so I switched to URH and was able to get good recordings. 

Signals were broadcast on 433.92 MHz. When the sensors are under pressure they broadcast a signal every 5 minutes. Both Temperature and Pressure data are transmitted. The goal of this project is to be able to monitor the tire pressures of my RV while in storage. I have another RTL-SDR connected to a Home Assistant server running on my RV where I can monitor critical sensors while I'm away from it. I cannot find any FCC identifying marks anywhere. Not on any of the hardware and it is not listed in the manuals.

I ended up running 9 tests on 2 sensors using an e-bike in an isolated warehouse so my noise levels were very low. I had the antenna approximately 12" from the tire and did notice the signal was affected by the position of the valve stem to the antenna. I varied the pressure by letting air out of the tire and used a heat gun on the sensor to change the temp. I read and recorded the sensor date from the display unit that came with the product.  The sensor transmits 3 packets of data with ASK modulation. One long 116 bit and then 2 short 20 bit (repeating)  bursts. I have not been able to make sense of the first packet in total and used NRZ decoding. The other two packets can be decoded with Manchester and I was able to pick out the sensor ID (bits 6-12) but I have not been able workout out the pressure and temperature bits.

| Test | Packet | Decoder | Sender ID | PSI | Temp F | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Tire 1-2 | 1 | NRZ | 0x0D177E | 55 | 68 | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a |
  | 2 | Manchester |  |  |  | 0 | 0 | 0 | 0 | 8 | 1 | 0 | d | 1 | 7 | 7 | e | 9 | 9 | 4 | 6 | 0 | 0 | 0 | 0 |
  | 3 | Manchester |  |  |  | 0 | 0 | 0 | 0 | 8 | 1 | 0 | d | 1 | 7 | 7 | e | 9 | 9 | 4 | 6 | 0 | 0 | 0 | 0 |
| Tire 1-3 | 1 | NRZ | 0x0D177E | 55 | 68 | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a |
  | 2 | Manchester |  |  |  | 0 | 0 | 0 | 0 | 8 | 1 | 0 | d | 1 | 7 | 7 | e | 9 | 9 | 4 | 6 | 0 | 0 | 0 | 0 |
  | 3 | Manchester |  |  |  | 0 | 0 | 0 | 0 | 8 | 1 | 0 | d | 1 | 7 | 7 | e | 9 | 9 | 4 | 6 | 0 | 0 | 0 | 0 |
| Tire 1-4 | 1 | NRZ | 0x0D177E | 55 | 114 | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a |
  | 2 | Manchester |  |  |  | 0 | 0 | 0 | 0 | 9 | c | 0 | d | 1 | 7 | 7 | e | 9 | a | 6 | 0 | 0 | 0 | 0 | 0 |
  | 3 | Manchester |  |  |  | 0 | 0 | 0 | 0 | 9 | c | 0 | d | 1 | 7 | 7 | e | 9 | a | 6 | 0 | 0 | 0 | 0 | 0 |
| Tire 2-3 | 1 | NRZ | 0x54E328 | 56 | 66 | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a |
  | 2 | Manchester |  | 56 | 66 | 0 | 0 | 0 | 0 | b | f | 5 | 4 | e | 3 | 2 | 8 | 9 | b | 4 | 5 | 0 | 0 | 0 | 0 |
  | 3 | Manchester |  | 56 | 66 | 0 | 0 | 0 | 0 | b | f | 5 | 4 | e | 3 | 2 | 8 | 9 | b | 4 | 5 | 0 | 0 | 0 | 0 |
| Tire 2-5 | 1 | NRZ | 0x54E328 | 53 | 66 | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a |
  | 2 | Manchester |  | 53 | 66 | 0 | 0 | 0 | 0 | b | 7 | 5 | 4 | e | 3 | 2 | 8 | 9 | 3 | 4 | 5 | 0 | 0 | 0 | 0 |
  | 3 | Manchester |  | 53 | 66 | 0 | 0 | 0 | 0 | b | 7 | 5 | 4 | e | 3 | 2 | 8 | 9 | 3 | 4 | 5 | 0 | 0 | 0 | 0 |
| Tire 2-6 | 1 | NRZ | 0x54E328 | 53 | 68 | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a | a |
  | 2 | Manchester |  | 53 | 68 | 0 | 0 | 0 | 0 | b | 8 | 5 | 4 | e | 3 | 2 | 8 | 9 | 3 | 4 | 6 | 0 | 0 | 0 | 0 |
  | 3 | Manchester |  | 53 | 68 | 0 | 0 | 0 | 0 | b | 8 | 5 | 4 | e | 3 | 2 | 8 | 9 | 3 | 4 | 6 | 0 | 0 | 0 | 0 |

  This is the data from the 1st signal. Edited for repeating data.

   Test | Packet | Decoder | Sender ID | PSI | Temp F | 1-55 | 56 | 57-76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 | 101 | 102 | 103 | 104 | 105 | 106 | 107 | 108 | 109 | 110 | 111 | 112 | 113 | 114 | 115 | 116 
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
 Tire 1-2 | 1 | NRZ | 0x0D177E | 55 | 68 | a | a | a | b | 2 | c | d | 3 | 5 | 2 | d | 3 | 5 | 3 | 4 | d | 4 | d | 3 | 3 | 4 | b | 3 | 4 | b | 4 | c | c | d | 2 | b | 4 | c | b | 4 | d | 4 | d | 3 | 4 | d | 5 | 4 
 Tire 1-3 | 1 | NRZ | 0x0D177E | 55 | 68 | a | a | a | b | 2 | c | d | 3 | 5 | 2 | d | 3 | 5 | 3 | 4 | d | 4 | d | 3 | 3 | 4 | b | 3 | 4 | b | 4 | c | c | d | 4 | b | 4 | c | b | 4 | d | 4 | d | 3 | 4 | d | 5 | 4 
 Tire 1-4 | 1 | NRZ | 0x0D177E | 55 | 114 | a | a | a | b | 2 | a | d | 3 | 5 | 2 | d | 3 | 5 | 3 | 3 | 5 | 4 | d | 3 | 3 | 4 | b | 2 | c | b | 4 | c | c | d | 2 | b | 4 | c | d | 4 | d | 4 | d | 3 | 4 | d | 5 | 4 
 Tire 2-3 | 1 | NRZ | 0x54E328 | 56 | 66 | a | 8 | a | c | b | 5 | 4 | b | 4 | b | 2 | b | 5 | 3 | 3 | 3 | 2 | d | 4 | b | 3 | 3 | 4 | d | 5 | 5 | 4 | b | 2 | c | b | 5 | 5 | 2 | d | 5 | 3 | 3 | 3 | 3 | 5 | 3 | 5 
 Tire 2-5 | 1 | NRZ | 0x54E328 | 53 | 66 | a | 8 | a | c | b | 5 | 4 | b | 4 | b | 2 | d | 5 | 3 | 3 | 3 | 2 | c | d | 3 | 3 | 3 | 4 | c | d | 5 | 4 | b | 2 | c | b | 5 | 5 | 2 | d | 5 | 3 | 3 | 3 | 3 | 5 | 2 | d 
 Tire 2-6 | 1 | NRZ | 0x54E328 | 53 | 68 | a | 8 | a | c | b | 5 | 4 | b | 4 | b | 2 | b | 5 | 3 | 3 | 3 | 2 | c | c | b | 3 | 3 | 4 | d | 5 | 5 | 4 | b | 2 | c | b | 5 | 5 | 2 | d | 5 | 3 | 3 | 3 | 3 | 5 | 3 | 5 

Updated 02-16-23 with 11 tests files captured with rtl_433 -f 433.88M -S unknown. Removed old test files and replaced with new test files recorded with an offset frequency and varied distance from sensor to Antenna as the initial tests were clipped based on suggestion received.
File | Sensor ID | PSI | Temp | Antenna Dist | Recorded |
:---:|:---:|:---:|:---:|:---:|:---:|
g001_433.88M_250k_ID_0D177E_39psi_48F.cu8 | 0d177e | 39 | 48 | 6' | 2/16/23|
g004_433.88M_250k_ID_0D177E_39psi_64F.cu8 | 0d177e | 39 | 64 | 6' | 2/16/23|
g006_433.88M_250k_ID_0D177E_39psi_66F.cu8 | 0d177e | 39 | 66 | 6' | 2/16/23|
g008_433.88M_250k_ID_0D177E_40psi_68F.cu8 | 0d177e | 40 | 68 | 6' | 2/16/23|
g013_433.88M_250k_ID_0D177E_39psi_68F.cu8 | 0d177e | 39 | 86 | 6' | 2/16/23|
g018_433.88M_250k_ID_0D177E_39psi_48F.cu8 | 0d177e | 39 | 48 | 6' | 2/16/23|
g020_433.88M_250k_ID_54E328_63psi_53F.cu8 | 54e328 | 63 | 53 | 6' | 2/16/23|
g043_433.88M_250k_ID_54E328_63psi_68F.cu8 | 54e328 | 63 | 68 | 6' | 2/16/23|
g060_433.88M_250k_ID_54E328_63psi_68F.cu8 | 54e328 | 63 | 68 | 12' | 2/16/23|
g165_433.88M_250k_ID_54E328_58psi_132F.cu8 | 54e328 | 58 |132 | 12' |  2/16/23|
g185_433.88M_250k_ID_54E328_58psi_95F.cu8 | 54e328 | 58 |95 | 12' | 2/16/23|


Unfortuntely I don't yet understand how to use the tools to disect this data. However FSK demodulation makes sense this time.

Updated again 02/17/23. After horsing around with the gain settings and antenna positions for about an hour, I was able to capture signals that I could drop into https://triq.org/spectrogram-next/ and look at the analogue signal that had rounded peaks and not clipped. the manual gain was between 26 and 30 so I settled on g 27. It would be nice if the file save output in the terminal window had a time stamp on it along with the file name, sample size, etc! Here are the new files and the captured data as recorded on the head unit using the command rtl_433 -4 433.88M -S unknown 1024k -g 27. Below is a subset of the data that was collected.

File | Sensor ID | PSI | Temp | Antenna Dist | Notes |
:---:|:---:|:---:|:---:|:---:|:---:|
g071_433.88M_1024k.cu8 | 0d177e | 55 | 68 | 13' | 2/17/23|
g077_433.88M_1024k.cu8 | 0d177e | 55 | 114 | 13' | 2/17/23|
g078_433.88M_1024k.cu8 | 0d177e | 55 | 93 | 13' | 2/17/23|
g108_433.88M_1024k.cu8 | 0d177e | 49 | 75 | 13' | Alarm |
g121_433.88M_1024k.cu8 | 0d177e | 0 | 675 | 13' | Alarm |
g200_433.88M_1024k.cu8 | 54e328 | 59 | 111 | 13' | 2/17/23|
g203_433.88M_1024k.cu8 | 54e328 | 56 | 6 | 13' | 2/17/23|
g204_433.88M_1024k.cu8 | 54e328 | 56 | 50 | 13' | 2/17/23|
g205_433.88M_1024k.cu8 | 0d177e | 54 | -4 | 13' | 2/17/23|
g207_433.88M_1024k.cu8 | 0d177e | 52 | 46 | 13' | 2/17/23|

