# FAN-11T Fan Remote

## Test Files

* 01:
   * g001_302.55M_250k.cu8
     * Fan Off
   * g002_302.55M_250k.cu8
     * Fan Low

* 02:
    * g003_302.3M_250k.cu8
      * Fan Hi
    * g004_302.55M_250k.cu8
      * Light (Toggle)
      

## Description 

Remote Control for many Harbor Breeze

(Model # KUJCE9103 FAN-11T FAN-53T 2AAZPFAN-53T)

FCC ID:  [L3HFAN11T](https://fccid.io/L3HFAN11T)

Available  on [Amazon](https://www.amazon.com/s?k=Fan-11T)


###  Manufacturer Info 

Based on the Holtek the [HT12E](https://www.holtek.com/productdetail/-/vg/2_12e) & [HT12F](https://www.holtek.com/productdetail/-/vg/2_12d) chipsets

[HT12E 2/12 Series Encoder DataSheet ](https://www.holtek.com/documents/10179/116711/2_12ev120.pdf)

[HT12F 2/12 Series Decoder DataSheet ](https://www.holtek.com/documents/10179/116711/2_12dv120.pdf)

### Protocol Specs



##### Timing


Datarate is approximately 1Kbaud ( 1ms per bit )

Short pulse =.0.36ms  

Long pulse = 0.71ms

(Bits are transmitted with varing pause before the pulse)



##### Command Codes

(interpreting Long pulse as one)


Command  | Bit Pattern | Decimal | Hex
---------|-------------|---------|----
Hi   |  `0 1 0 0 0 0 0` | 32 | 0x20
Med  |  `0 0 1 0 0 0 0` | 16 | 0x10
Low  |  `0 0 0 1 0 0 0` | 08 | 0x08
*unused* | `0 0 0 0 1 0 0` | 04 | 0x04
Off  |  `0 0 0 0 0 1 0` | 02 | 0x02
Lit  |  `0 0 0 0 0 0 1` | 01 | 0x01
End? |  `0 0 0 0 0 0 0` | 00 | 0x80

##### Packet Format
Each transmission contains 13 bits  with 12bits of info (13 bits Transmitted)

packets can be described  as

**short** + **long** + **4 bit ID** + **short** + **6 bit command code**

Given an 4 but ID code of `1001` the command to turn the fan on "Hi' the packet will be formated as follows

   `0` + `1` + `1001`+ `0` +`0 1 0 0 0 0 0`  -> 0 1 1 0 0 1 0`0 1 0 0 0 0 0
   

The HT12F receiver requires three matching transmissions optionally followed by one all packet with all shorts thus a minimal full transmission is:

`01100100100000` `01100100100000` `01100100100000` `01100100000000`

with an approximately a 12ms pause separating 


