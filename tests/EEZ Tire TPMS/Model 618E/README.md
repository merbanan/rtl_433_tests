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


Unfortuntely I don't yet understand how to use the tools to disect this data. However FSK demodulation makes sense this time.
## Setup After Feedback from Smart People
Updated again 02/17/23. After horsing around with the gain settings and antenna positions for about an hour, I was able to capture signals that I could drop into https://triq.org/spectrogram-next/ and look at the analogue signal that had rounded peaks and not clipped. the manual gain was between 26 and 30 so I settled on g 27. It would be nice if the file save output in the terminal window had a time stamp on it along with the file name, sample size, etc! Here are the new files and the captured data as recorded on the head unit using the command rtl_433 -f 433.88M -S unknown -s 1024k -g 27. Reducing the gain also help that stary signal that was being picked up so the data below is from the tire pressure sensor. Below is a subset of the data that was collected.

File | Sensor ID | PSI | Temp | Antenna Dist | Notes |
:---:|:---:|:---:|:---:|:---:|:---:|
g071_433.88M_1024k.cu8 | 0d177e | 55 | 68 | 13' | 2/17/23|
g077_433.88M_1024k.cu8 | 0d177e | 55 | 114 | 13' | 2/17/23|
g078_433.88M_1024k.cu8 | 0d177e | 55 | 93 | 13' | 2/17/23|
g108_433.88M_1024k.cu8 | 0d177e | 49 | 75 | 13' | Alarm |
g121_433.88M_1024k.cu8 | 0d177e | 0 | 75 | 13' | Alarm |
g200_433.88M_1024k.cu8 | 54e328 | 59 | 111 | 13' | 2/17/23|
g203_433.88M_1024k.cu8 | 54e328 | 56 | 6 | 13' | 2/17/23|
g204_433.88M_1024k.cu8 | 54e328 | 56 | 50 | 13' | 2/17/23|
g205_433.88M_1024k.cu8 | 0d177e | 54 | -4 | 13' | 2/17/23|
g207_433.88M_1024k.cu8 | 0d177e | 52 | 46 | 13' | 2/17/23|

## CR1632 Coin Cell Adapter for use with Power Supply
Things are moving along thanks to great people that are a whole lot smarter than I that jumped in to do the heavy lifting. One question came up with an unknown bit that might be for a low battery alert on the sensor. I modeled up and 3-D printed a CR1632 sized holder to be able to hook up a power supply to the sensor and then adjust the voltage down until the sensor quits sending data. This is the setup and I will post the data after collected on 2/20/23.

![CR1632 v2](https://user-images.githubusercontent.com/35844174/219988834-acae5164-466b-43da-be14-cbf32a90c2f2.png)
![PS_Adapter_1_320](https://user-images.githubusercontent.com/35844174/219988841-a4e016dc-a629-451b-97ce-bd59819d143b.jpg)
![PS Adapter_320](https://user-images.githubusercontent.com/35844174/219988854-4ab2b13c-3110-477a-8f2a-9bc33162387b.jpg)

## Table of tests Varying Voltage of TPMS Sensor

I was able to successfully change the voltage of the TPMS sensor while on a tire in the same office. The table of test results appears below:

|Sample|File|ID	|PSI|F|V|DATA| |		
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|g001|_433.88M_1024k.cu8|54e328|49|73|3.00|{80}ffffa054e32888497000|[g001: 54e328 49 PSI 73 F 3.00 V] |
|g002|_433.88M_1024k.cu8|54e328|49|71|2.99|{80}ffffb054e32889480000|[g002: 54e328 49 PSI 71 F 2.99 V] |
|g003|_433.88M_1024k.cu8|54e328|49|69|2.95|{80}ffffaf54e32889470000|[g003: 54e328 49 PSI 69 F 2.95 V] |
|g004|_433.88M_1024k.cu8|54e328|49|69|2.90|{80}ffffaf54e32889470000|[g004: 54e328 49 PSI 69 F 2.90 V] |
|g005|_433.88M_1024k.cu8|54e328|49|69|2.88|{80}ffffdf54e32889473000|[g005: 54e328 49 PSI 69 F 2.88 V] |
|g006|_433.88M_1024k.cu8|54e328|49|69|2.87|{80}ffffdf54e32889473000|[g006: 54e328 49 PSI 69 F 2.87 V] |
|g007|_433.88M_1024k.cu8|54e328|49|69|2.86|{80}ffff9f54e32889477000|[g007: 54e328 49 PSI 69 F 2.86 V] |
|g008|_433.88M_1024k.cu8|54e328|49|69|2.85|{80}ffffdf54e32889473000|[g008: 54e328 49 PSI 69 F 2.85 V] |
|g009|_433.88M_1024k.cu8|54e328|49|69|2.84|{80}ffff9f54e32889477000|[g009: 54e328 49 PSI 69 F 2.84 V] |
|g010|_433.88M_1024k.cu8|54e328|49|69|2.83|{80}ffffe054e32889483000|[g010: 54e328 49 PSI 69 F 2.83 V] |
|g011|_433.88M_1024k.cu8|54e328|49|69|2.82|{80}ffff9f54e32889477000|[g011: 54e328 49 PSI 69 F 2.82 V] |
|g012|_433.88M_1024k.cu8|54e328|49|69|2.81|{80}ffffdf54e32889473000|[g012: 54e328 49 PSI 69 F 2.81 V] |
|g013|_433.88M_1024k.cu8|54e328|49|71|2.80|{80}ffffe054e32889483000|[g013: 54e328 49 PSI 71 F 2.80 V] |
|g014|_433.88M_1024k.cu8|54e328|49|69|2.79|{80}ffff9f54e32889477000|[g014: 54e328 49 PSI 69 F 2.79 V] |
|g015|_433.88M_1024k.cu8|54e328|49|69|2.78|{80}ffffdf54e32889473000|[g015: 54e328 49 PSI 69 F 2.78 V] |
|g016|_433.88M_1024k.cu8|54e328|49|69|2.77|{80}ffffdf54e32889473000|[g016: 54e328 49 PSI 69 F 2.77 V] |
|g017|_433.88M_1024k.cu8|54e328|49|69|2.76|{80}ffffdf54e32889473000|[g017: 54e328 49 PSI 69 F 2.76 V] |
|g018|_433.88M_1024k.cu8|54e328|49|69|2.75|{80}ffffdf54e32889473000|[g018: 54e328 49 PSI 69 F 2.75 V] |
|g019|_433.88M_1024k.cu8|54e328|49|71|2.74|{80}ffffe054e32889483000|[g019: 54e328 49 PSI 71 F 2.74 V] |
|g020|_433.88M_1024k.cu8|54e328|49|69|2.73|{80}ffffdf54e32889473000|[g020: 54e328 49 PSI 69 F 2.73 V] |
|g021|_433.88M_1024k.cu8|54e328|49|71|2.72|{80}ffffe054e32889483000|[g021: 54e328 49 PSI 71 F 2.72 V] |
|g022|_433.88M_1024k.cu8|54e328|49|71|2.71|{80}ffffe054e32889483000|[g022: 54e328 49 PSI 71 F 2.71 V] |
|g023|_433.88M_1024k.cu8|54e328|49|71|2.70|{80}ffffe054e32889483000|[g023: 54e328 49 PSI 71 F 2.70 V] |
|g024|_433.88M_1024k.cu8|54e328|49|69|2.69|{80}ffffdf54e32889473000|[g024: 54e328 49 PSI 69 F 2.69 V] |
|g025|_433.88M_1024k.cu8|54e328|49|69|2.68|{80}ffffdf54e32889473000|[g025: 54e328 49 PSI 69 F 2.68 V] |
|g026|_433.88M_1024k.cu8|54e328|49|71|2.67|{80}ffffa054e32889487000|[g026: 54e328 49 PSI 71 F 2.67 V] |
|g027|_433.88M_1024k.cu8|54e328|49|71|2.66|{80}ffffa054e32889487000|[g027: 54e328 49 PSI 71 F 2.66 V] |
|g028|_433.88M_1024k.cu8|54e328|49|71|2.65|{80}ffffe054e32889483000|[g028: 54e328 49 PSI 71 F 2.65 V] |
|g029|_433.88M_1024k.cu8|54e328|49|71|2.64|{80}ffffe054e32889483000|[g029: 54e328 49 PSI 71 F 2.64 V] |
|g030|_433.88M_1024k.cu8|54e328|49|71|2.63|{80}ffffe054e32889483000|[g030: 54e328 49 PSI 71 F 2.63 V] |
|g031|_433.88M_1024k.cu8|54e328|49|69|2.62|{80}ffff9f54e32889477000|[g031: 54e328 49 PSI 69 F 2.62 V] |
|g032|_433.88M_1024k.cu8|54e328|49|69|2.61|{80}ffffdf54e32889473000|[g032: 54e328 49 PSI 69 F 2.61 V] |
|g033|_433.88M_1024k.cu8|54e328|49|71|2.60|{80}ffffe054e32889483000|[g033: 54e328 49 PSI 71 F 2.60 V] |
|g034|_433.88M_1024k.cu8|54e328|49|69|2.59|{80}ffffdf54e32889473000|[g034: 54e328 49 PSI 69 F 2.59 V] |
|g035|_433.88M_1024k.cu8|54e328|49|71|2.58|{80}ffffe054e32889483000|[g035: 54e328 49 PSI 71 F 2.58 V] |
|g036|_433.88M_1024k.cu8|54e328|49|71|2.57|{80}ffffe054e32889483000|[g036: 54e328 49 PSI 71 F 2.57 V] |
|g037|_433.88M_1024k.cu8|54e328|49|71|2.56|{80}ffffe054e32889483000|[g037: 54e328 49 PSI 71 F 2.56 V] |
|g038|_433.88M_1024k.cu8|54e328|49|71|2.55|{80}ffffe054e32889483000|[g038: 54e328 49 PSI 71 F 2.55 V] |
|g039|_433.88M_1024k.cu8|54e328|49|71|2.54|{80}ffffe054e32889483000|[g039: 54e328 49 PSI 71 F 2.54 V] |
|g040|_433.88M_1024k.cu8|54e328|  |  |2.53|No Signal| |		

My hopes this data will help identify the missing information.
