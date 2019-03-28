These signals are from a Neptune ECoder R900i water meter (using the r900 protocol).

Much of this information comes from https://github.com/bemasher/rtlamr but I have compared it to the captured signal.


The signal starts with a 32-bit preamble using manchester coding.  THe preamble can be decoded by rtl_433 using -X 'n=name,m=OOK_MC_ZEROBIT,s=30,r=320'

Preamble binary - 0000 0000 0000 0000 1110 0101 0110 0100
Preamble hex - 00 00 e5 64

For a group of bits that are the same, the gaps are approximately 17us and the pulses are approximately 44us, however, when two pulses are together (as in a '0' followed by a '1'), the combined pulse duration is approximatly 74us, and when two gaps are together (as in a '1' followed by a '0'), the combined gap duration is approximately 48us.


The payload afterwards not using manchester coding.  The signal is present for a '1' and absent for a '0'.  The timings for the '1' and '0' are not uniform.  These are the approximate durations of the '1' pulses and '0' gaps, both individually and grouped:

'0' is 17us
'1' is 44us
'00' is 48us
'11' is 74us
'000' is 79us
'111' is 104us
'0000' is 109us
'1111' is 134us

Each group of four of these chips must be interpretted as a digit in base 6 according to the following mapping:
0011 -> 0
0101 -> 1
0110 -> 2
1100 -> 3
1010 -> 4
1001 -> 5

Each pair of base 6 digits must be converted to 5 binary bits, e.g. 0101 1001 0110 1010 from the signal becomes 15 24 in base six which becomes 01011 10000.

All these new bits must be put together to understand the payload.

Once the payload is decoded, the message is as follows (from https://github.com/bemasher/rtlamr/wiki/Protocol#r900-consumption-message)
ID - 32 bits
Unkn1 - 8 bits
NoUse - 6 bits
BackFlow - 6 bits
Consumption - 24 bits
Unkn3 - 2 bits
Leak - 4 bits
LeakNow - 2 bits

These is more data after this, likely a checksum of some kind.


Here is what the signal file (g018_912.6M_1000k.cu8) contains:

If the preamble were to be read from the signal in the same way as the payload (instead of using manchester coding) it is
From the signal: 0101 0101 0101 0101 0101 0101 0101 0101 1010 1001 0110 0110 0110 1001 0110 0101
In base 6: 11 11 11 11 45 22 25 21
In binary: 00111 00111 00111 00111 11101 01110 10001 01101
In hex: 39 ce 7e ba 2d

ID and Unkn1:
From the signal: 0101 1001 0110 1010 1100 0011 0101 1001 1100 1010 0110 1001 1100 1100 0011 1100
In base 6: 15 24 30 15 34 25 33 03
In binary: 01011 10000 10010 01011 10110 10001 10101 00011
In hex: 5c 24 bb 46 a3
ID: 5c24bb46(hex) - 1545911110(dec) [printed on the meter]
Unkn1: a3(hex) - 163(dec)

NoUse, BackFlow, Consumption, Unkn3, Leak, and LeakNow:
From the signal: 0110 1010 0110 1010 0011 1100 0011 0110 1010 1100 1001 0011 0110 1010 0011 0011
In base 6: 24 24 03 02 43 50 24 00
In binary: 10000 10000 00011 00010 11011 11110 10000 00000
In hex: 84 06 2d fa 00
NoUse: 100001(bin) - 33(dec) [Days]
BackFlow: 00(bin) - 0(dec) [2 for High, 1 for Low, 0 for None]
Consumption: 062dfa(hex) - 404986(dec) [Cubic Feet x100, meter reads 4049.86]
Leak: 0000(bin) - 0(dec) [Days]
LeakNow: 00(bin) - 0(dec) [2 for Continuous, 1 for Intermittent, 0 for None]

The remaining signal appears to be:
From the signal: 0101 0011 1100 1010 1010 1010 1100 1010 1010 1001
In base 6: 10 34 44 34 45
In binary: 00110 10110 11100 10110 11101
In hex: 35 b9 6e (followed by an extra 1 bit)


As far as I can tell, R900 is a Neptune specific protocol.

My meter is labeled:
Neptune E-Coder)R900i
Neptune R900 v4
Model R900M
Part No. RW2F13
FCCID P2SR900M
IC 4171B-R900M
IFT RCPNER914-116
Internal Software 2008

Here are some relevant links:
Product Page: 
https://www.neptunetg.com/products/endpointsmius/e-coderr900i/
Information PDF (page 2): 
https://www.neptunetg.com/globalassets/products/literature/19-003084-ps-e-coderr900i-01.19.pdf
https://www.neptunetg.com/globalassets/products/literature/19-003084-ps-e-coder-r900i-v5-01.19.pdf
Installation and Maintenance (pages 16, 17, 21, 45-46):
https://www.neptunetg.com/globalassets/products/literature/publication_e-coderr900i-10.15.pdf
Installation and maintenance (pages 14, 15, 24, 41, 42):
https://www.neptunetg.com/globalassets/products/literature/publication_im-e-coder-r900i-12.18.pdf
RTLAMR r900 source: 
https://github.com/bemasher/rtlamr/blob/master/r900/r900.go
RTLAMR r900 message description: 
https://github.com/bemasher/rtlamr/wiki/Protocol#r900-consumption-message
RTLAMR r900 flag description comment: 
https://github.com/bemasher/rtlamr/issues/29#issuecomment-97622287














