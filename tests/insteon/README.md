# Insteon

> Insteon is a home automation (domotics) technology that enables light switches, lights, thermostats, leak sensors, remote controls, motion sensors, and other electrically powered devices to interoperate through power lines, radio frequency (RF) communications, or both.
> It employs a dual-mesh networking topology in which all devices are peers and each device independently transmits, receives, and repeats messages.
> Like other home automation systems, it has been associated with the Internet of Things
[wikipedia](https://en.wikipedia.org/wiki/Insteon)

## Test Files

* 01:
   * g001_915M_1024k.cu8
     * `45 : 132580 : 2AFF9B : 11 01  AD`
   * g002_915M_1024k.cu
     * `45 : 226B3F : 2B7811 : 13 01  93`
   * g008_915M_1024k.json
     * `45 : 226B3F : 2B7811 : 13 01  93`
     * '41 : 226B3F : 2B7811 : 13 01  57`



* 02:
    * g003_915M_1024k.cu8
      * `4A : 132580 : 2AFF9B : 11 01  B2`
      * `46 : 132580 : 2AFF9B : 11 01  FE`
      * `42 : 132580 : 2AFF9B : 11 01  3A`
    * g004_915M_1024k.cu8
      * `4F : 226B3F : 2B7811 : 13 01  79`
      * `4B : 226B3F : 2B7811 : 13 01  BD`
      * `47 : 226B3F : 2B7811 : 13 01  F1`
      * `43 : 226B3F : 2B7811 : 13 01  35`

* 03:
    * g005_915M_1024k.cu8
      * `17 : 34F837 : 132580 : 2F 00 00 02 0F D7 08 E2 01 16 3F E5 02 00 01  C1`
    * g006_915M_1024k.cu8
      * `15 : 132580 : 247864 : 2F 00 00 01 0F FF 00 A2 00 13 25 80 FF 1F 00  4A`

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


