Jansite Solar TPMS Solar Model.
￼
￼http://www.jansite.cn/P_view.asp?pid=229
￼
￼- Frequency: 433.92 +/- 20.00 MHz
￼- Pressure: +/- 0.1 bar from 0 bar to 6.6 bar
￼- Temperature: +/- 3 C from -40 C to 75 C
￼
￼Signal is manchester encoded, and a 11 byte large message
￼
￼Data layout (nibbles):
￼
￼    SS SS II II II 00 TT PP 00 CC CC
￼
￼- S: 16 bits sync word, 0xdd33
￼- I: 24 bits ID
￼- 0: 8 bits Unknown data 1, one bit should be battery level
￼- T: 8 bit Temperature (deg. C offset by 55)
￼- P: 8 bit Pressure (best guess quarter PSI, i.e. ~0.58 kPa)
￼- 0: 8 bits Unknown data 2, one bit should be battery level
￼- C: 16 bit CRC (CRC-16/BUYPASS)
￼- The preamble is 0xa6, 0xa6, 0x5a


