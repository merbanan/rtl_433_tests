# TR-502MSV remote socket controller

The controller uses 433.92MHz frequency, OOK modulation and PWM encoding.
It can control 4 sockets with 4 pairs of on/off buttons. There are 2 additional
pairs of buttons - all on/off and brightness button dim/bright. Reset button
in the battery compartment can be used to change device id. For further
details see [the manual](tr502msv_rc710_manual.pdf).

Flex decoder:  
`-X 'n=tr502msv,m=OOK_PWM,s=740,l=1400,t=70,r=84000'`

## Data structure
The data packet is repeated up to 4 times and comprises 21 bits:  
`PIIIIIII IIIIISSS OCRUU`
  - P: 1-bit preamble
  - I: 12-bit device id
  - S: 3-bit socket id
  - O: 1-bit on/off
  - C: 1-bit command - brightness/switch
  - R: 1 reserved bit (always 0)
  - U: 2 unknown bits, most likely a checksum

Sockets map to the socket ids as follows:
| Socket | Socket id |
| ------ | --------- |
|   1    |    000    |
|   2    |    100    |
|   3    |    010    |
|   4    |    110    |
|  all   |    111    |

## Samples
Directory `samples` contains captured samples whose names describe the
corresponding action (e.g. socket2 off/on/dim/bright).
