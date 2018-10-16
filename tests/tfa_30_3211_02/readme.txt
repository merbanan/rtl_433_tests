
 TFA 30.3211.02 
 
 1970us pulse with variable gap (third pulse 3920 us)
 
 Above 79% humidity, gap after third pulse is 5848 us (see sample 008)
 
 Bit 1 : 1970us pulse with 3888 us gap
 Bit 0 : 1970us pulse with 1936 us gap
 
 Demoding with -X "tfa_test:OOK_PPM_RAW:2900:5000:36500"
 
 74 bit (2 bit preamble and 72 bit data => 9 bytes => 18 nibbles)
 
 Nibble       1   2    3   4    5   6    7   8    9   10   11  12   13  14   15  16   17  18
           PP ?HHHhhhh ??CCNIII IIIITTTT ttttuuuu ???????? ???????? ???????? ???????? ??????
 
     P = Preamble
     H = First digit humidity 7-bit 0=8,1=9 (Range from 20 - 99%)
     h = Second digit humidity
     C = Channel
     T = First digit temperatur
     t = Second digit temperatur
     u = Third digit temperatur
     N = Negative temperatur
     
