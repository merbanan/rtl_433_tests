# Insteon

> Insteon is a home automation (domotics) technology that enables light switches, lights, thermostats, leak sensors, remote controls, motion sensors, and other electrically powered devices to interoperate through power lines, radio frequency (RF) communications, or both.
> It employs a dual-mesh networking topology in which all devices are peers and each device independently transmits, receives, and repeats messages.
> Like other home automation systems, it has been associated with the Internet of Things
[wikipedia](https://en.wikipedia.org/wiki/Insteon)

## Test Files

* 01:
    * 01/g001_915M_1024k.cu8
        * `45 : 132580 : 2AFF9B : 11 01  AD`
    * 01/g002_915M_1024k.cu8
        * `45 : 226B3F : 2B7811 : 13 01  93`
    * 01/g003_915M_1024k.cu8
        * `4A : 132580 : 2AFF9B : 11 01  B2`
        * `46 : 132580 : 2AFF9B : 11 01  FE`
        * `42 : 132580 : 2AFF9B : 11 01  3A`
    * 01/g008_915M_1024k.cu8
        * `45 : 226B3F : 2B7811 : 13 01  93`
        * `41 : 226B3F : 2B7811 : 13 01  57`


* 02:
    * 02/g020_915M_1000k.cu8
        * `0B : 175469 : 132580 : 11 FF  29`
        * `07 : 175469 : 132580 : 11 FF  65`
        * `03 : 175469 : 132580 : 11 FF  A1`
    * 02/g021_915M_1000k.cu8
        * `2B : 132580 : 175469 : 11 FF  49`
        * `27 : 132580 : 175469 : 11 FF  05`
        * `23 : 132580 : 175469 : 11 FF  C1`


* 03:
    * 03/g005_915M_1024k.cu8
        * `17 : 34F837 : 132580 : 2F 00 00 02 0F D7 08 E2 01 16 3F E5 02 00 01  C1`
    * 03/g006_915M_1024k.cu8
        * `15 : 132580 : 247864 : 2F 00 00 01 0F FF 00 A2 00 13 25 80 FF 1F 00  4A`


* 04:
    * 04/g001_915M_1000k.cu8
        * CF : 2AFF9B : 000001 : 11 01  90`
        * CB : 2AFF9B : 000001 : 11 01  54`
        * C7 : 2AFF9B : 000001 : 11 01  18`
        * C3 : 2AFF9B : 000001 : 11 01  DC`
        * 45 : 132580 : 2AFF9B : 11 01  AD`
        * 41 : 132580 : 2AFF9B : 11 01  69`
    * 04/g002_915M_1000k.cu8
        * `4A : 132580 : 2AFF9B : 11 01  B2`
        * `46 : 132580 : 2AFF9B : 11 01  FE`
        * `42 : 132580 : 2AFF9B : 11 01  3A`
    * 04/g003_915M_1000k.cu8
        * `4F : 132580 : 2AFF9B : 11 01  47`
        * `4B : 132580 : 2AFF9B : 11 01  83`
        * `47 : 132580 : 2AFF9B : 11 01  CF`
        * `43 : 132580 : 2AFF9B : 11 01  0B`
    * 04/g004_915M_1000k.cu8
        * `4A : 132580 : 2AFF9B : 13 01  B0`
        * `46 : 132580 : 2AFF9B : 13 01  FC`
        * `42 : 132580 : 2AFF9B : 13 01  38`

## Protocol / Encoding

See [pkt_format.md](pkt_format.md)


## Printed packet format notation

   *flag* **:** *to_address* **:** *from_address* : command_data crc

`43 : 226B3F : 2B7811 : 13 01  35`



## Settings

- Frequency: 915MHz
- Modulation: FSK
- Symbol Rate: 9125 sym/s
- Data Rate: 2600 bit/s (approx)

Flex decoder:  (for Raw bits)
    `n=Insteon_F16,m=FSK_PCM,s=110,l=110,t=15,g=20000,r=20000,invert,match={16}0x6666`


### See Also

[Insteon RF Toolkit](https://github.com/evilpete/insteonrf)
[YouTube](https://www.youtube.com/watch?v=dy1LTQLmPtM)


