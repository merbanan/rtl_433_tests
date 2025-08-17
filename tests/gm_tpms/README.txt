General Motors Aftermarket TPMS.

130 bit OOK_PULSE_MANCHESTER_ZEROBIT

Data was detected and initially captured using:

    rtl_433 -X 'n=name,m=OOK_MC_ZEROBIT,s=120,l=0,r=15600'


    130 bits
AAAAAAAAAAAAFFFFDDDDIIIIIIPPTTCCX
0000000000004c90007849176600536d0

Data layout:

   AAAAAAAAAAAAFFFFDDDDIIIIIIPPTTCCX

- A: preamble 0x000000000000
- F: Flags
- D: Device type or prefix
- I: Device uniquie identifier
- P: Pressure
- T: Temperature
- C: CheckSum, modulo 256

Format string:

    ID:10h FLAGS:4h KPA:2h TEMP:2h CHECKSUM:2h

