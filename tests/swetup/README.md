# SWETUP garage door opener
Like other users, I don't have a lot of experience/knowledge concerning modulation and data coding techniques.  
Please let me know, if more data is needed or information/conclusions are wrong or can be added.
## Source
Built in China and available at [AMAZON](https://www.amazon.de/dp/B09HWY1KH7), primarily for the german market.    
The PCB shows the code `DK302A`.
## Compatibility
according to Amazon, the device is able to be trained by following devices:
```
2260, 2262, PT2264, 5326, SC5262, HT600, HT680, HT6207, HT6010, HT6012, HT6014, SMC918, 527, 1527, 2240, HCS101, HCS200/HCS201 (partially), HCS300/HCS301 (partially)
```
## Samples
find four sample-files in the directory   
- `g001_433.92M_250k.cu8` (Button A pressed)
- `g002_433.92M_250k.cu8` (Button B pressed)
- `g003_433.92M_250k.cu8` (Button C pressed)
- `g004_433.92M_250k.cu8` (Button D pressed)

### Analysis
#### Running `-A g00*.cu8`
I ran `-A` for all files and noticed, that the output is similar for all four files. The following out put is an example for signal detected when analysing `g001_433.92M_250k.cu8`
```
Analyzing pulses...
Total count:   25,  width: 25.62 ms		( 6405 S)
Pulse width distribution:
 [ 0] count:   10,  width:  748 us [728;764]	( 187 S)
 [ 1] count:   15,  width:  236 us [232;248]	(  59 S)
Gap width distribution:
 [ 0] count:   10,  width:  304 us [292;328]	(  76 S)
 [ 1] count:   14,  width:  816 us [808;828]	( 204 S)
Pulse period distribution:
 [ 0] count:   24,  width: 1056 us [1036;1080]	( 264 S)
Pulse timing distribution:
 [ 0] count:   24,  width:  788 us [728;828]	( 197 S)
 [ 1] count:   17,  width:  244 us [232;296]	(  61 S)
 [ 2] count:    8,  width:  308 us [300;328]	(  77 S)
 [ 3] count:    1,  width: 10004 us [10004;10004]	(2501 S)
Level estimates [high, low]:  14512,   2046
RSSI: -0.5 dB SNR: 8.5 dB Noise: -9.0 dB
Frequency offsets [F1, F2]:    9371,      0	(+35.7 kHz, +0.0 kHz)
Guessing modulation: Pulse Width Modulation with fixed period
view at https://triq.org/pdv/#AAB104031400F4013427148290829082909090908290909082908282828190819090909355
Attempting demodulation... short_width: 236, long_width: 748, reset_limit: 832, sync_width: 0
Use a flex decoder with -X 'n=name,m=OOK_PWM,s=236,l=748,r=832,g=0,t=205,y=0'
```
#### Running `-X`
running the flex decoder (with the parameters from above) through all 4 files suggests, that the device sends a 25-bit code:
- `{25}57ba178`   (button A)
- `{25}57ba1e8`   (button B)
- `{25}57ba1b8`   (button C)
- `{25}57ba1d8`   (button D)
#### Decoding
Check [BitBench](https://triq.net/bitbench#c=5%207b%20a1%2078&c=5%207b%20a1%20e8&c=5%207b%20a1%20b8&c=5%207b%20a1%20d8&f=%20BUTTON%3A%20h%20xxxx&a=Preamble&m=57ba1) for a proposal

### further findings
As the package came with two devices of the same brand, I ran the tests with the second transmitter, as well. Interestingly (maybe not, though...), the decoded data is exactly the same as on the first device. My conclusion is, that all devices are indistinguishable as long as they haven't inherited a code from a parent device...    
