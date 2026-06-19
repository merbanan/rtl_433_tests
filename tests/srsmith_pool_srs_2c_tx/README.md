# SRSmith SRS-2C-TX

FCC ID: 2AI6L-SRSTX1

It operates on 915MHz band using GFSK.

This remote is sold (as part of a system) by SR Smith (www.srsmith.com) to control pool lighting. It has 4 dip switches that can be used to set different codes.

There is another device who's packet structure is similar enough to ALSO be set off by this remote: "RojaFlex shutter and remote devices" in `rojaflex.c`

## Settings
- Frequency: 915MHz
- Modulation: GFSK (or FSK_PCM)
- Data Rate: 10,000 bit/s

Flex decoder: (output here will be shifted. use bitbench and shift until you see A's in the preamble)
 
`-f 915000000 -X n=SRSmith,m=FSK_PCM,s=100,l=100,r=4096,match=d391d391`

## See Also
- [Page at FCCID.io](https://fccid.io/2AI6L-SRSTX1)
- [User Manual at FCCID.io](https://fccid.io/2AI6L-SRSTX1/Users-Manual/User-Manual-3110033)
