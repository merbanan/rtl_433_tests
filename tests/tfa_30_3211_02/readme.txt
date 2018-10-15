
 TFA 30.3211.02 
 
 1970us pulse with variable gap (third pulse 3920 us)
 
 Bit 1 : 1970us pulse with 3888 us gap
 Bit 0 : 1970us pulse with 1936 us gap
 
 74 bit (2 bit preamble and 72 bit data => 9 bytes => 18 nibbles)
 
 Nibble    1   2    3   4    5   6    7   8    9   10   11  12   13  14   15  16   17  18
          PP ?HHHhhhh ???????? II??TTTT ttttuuuu ???????? ???????? ???????? ???????? ??????
 
     P = Preamble
     H = first digit (only to 7?) humidity
     h = second digit humidity
     I = Channel
     T = first digit temperatur
     t = second digit temperatur
     u = third digit temperatur
 
