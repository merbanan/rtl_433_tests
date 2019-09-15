# Alecto WS 1200 - Version 2.0

A Thermometer with clock and wireless rain unit with temperature sensor.

Manual available at
https://www.alecto.nl/media/blfa_files/WS-1200_manual_NL-FR-DE-GB_V2.2_8712412532964.pdf

## Format notes

The rain unit counts in 0.3 mm steps. The sensor counter increases from 
0 to 65536(R, little endian), the display keeps the difference. Temperatue is transmitted as 
a number (t), to get Celsius substract 400 and divide by 10. The (i) section seems
to be a sensor ID, it changes at battery change. A status is ahead (s). While training for the station
connection the (d) part is 0, it is a part of the last time stamp and changes afterwards daily.
The (c + m) part changes on message change. Starting at bit 7 (after 7 bits of 1) there 
is a CRC-8 poly 0x31 init 0 for 7 bytes (c). Then another checksum and the trailing 3 bytes. 
(B) indicates low battery.

PRE: 7b Type: 4b ID: 8b BATTERY: 1b ?:1b T: 10d R:<16d ?: 8h CRC: 8h MAC: 8h DATE: 35b

Example:  
111111100111100010000100110110100000000000000001111111111101010110101000011010011101001100010000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  

## Flex decoder

A transmission is two packets (repeats) 36 ms apart.
Encoding is PWM with fixed gap length.
Short pulse of 500 us with 950 us gap (1500 us period),
Long pulse of 1500 us with 950 us gap (2500 us period).

`rtl_433 -X 'n=Alecto-WS-1200-v2.0,m=OOK_PWM,s=500,l=1500,r=37000,g=1100,t=400'`

The gap limit (g) here is slightly longer than the expected gap (950 us).
The reset limit (r) should be slightly longer than the packet distance, but 37 ms is too long.

## Training of station to the sensor

The sensor sends first a normal signal with d set 0 (maybe because DCF77 signal is not yet decoded?)

g000_433.92M_250k.cu8  
g001_433.92M_250k.cu8  
Bitbuffer: [00] {95} fe 69 e4 ac 00 01 ff 9e 94 00 00 00  
Binary:  
11111110011010011110010010101100000000000000000111111111100111101001010000000000000000000000000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  

Then a couple of signals with the time pattern and a longer status are send. They are required 
to fix the station to the reciver.

PRE: 7b Type: 8b ID: 8b BATT: 1b ?: 1b ?: ??: 6b YY: 4d YY:4d MM: 4d MM: 4d DD: 4d DD: 4d HH: 4d HH: 4d MM: 4d MM: 4d SS: 4d SS: 4d ? 16b

g002_433.92M_250k.cu8  
Bitbuffer: [00] {95} fe a4 9e 20 32 02 48 0a 80 68 47 16  
Binary:  
11111110101001001001111000100000001100100000001001001000000010101000000001101000010001110001011  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS   ?   ?   ?   ?  
                                  1   9   0   1   2   4   0   5   4   0   3   4  
                               (20)19      01.     24.     05  :   40  :   34  

g003_433.92M_250k.cu8  
Bitbuffer: [00] {95} fe a4 9e 20 32 02 48 0a 82 44 65 12  
Binary:  
11111110101001001001111000100000001100100000001001001000000010101000001001000100011001010001001  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS   ?   ?   ?   ?  
                                  1   9   0   1   2   4   0   5   4   1   2   2  
                               (20)19      01.     24.     05  :   41  :   22  

g004_433.92M_250k.cu8  
Bitbuffer: [00] {95} fe a4 9e 20 32 02 48 0a 84 21 71 fc  
Binary:  
11111110101001001001111000100000001100100000001001001000000010101000010000100001011100011111110  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS   ?   ?   ?   ?  
                                  1   9   0   1   2   4   0   5   4   2   1   0  
                               (20)19      01.     24.     05  :   42  :   10  

g005_433.92M_250k.cu8  
Bitbuffer: [00] {95} fe a4 9e 20 32 02 48 0a 84 b0 79 94  
Binary:  
11111110101001001001111000100000001100100000001001001000000010101000010010110000011110011001010  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS  A?  B?  C?  D?  
                                  1   9   0   1   2   4   0   5   4   2   5   8  
                               (20)19      01.     24.     05  :   42  :   58  

Then the regular signal is send every 45 sec  

g006_433.92M_250k.cu8  
g007_433.92M_250k.cu8  
Bitbuffer: [00] {95} fe 69 e4 b6 00 01 fe 8d 8c b0 79 94  
Binary:  
11111110011010011110010010110110000000000000000111111110100011011000110010110000011110011001010  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm  SS  SS  A?  B?  C?  D?  
See folder 02 for a the signal decoding.  


## Once at night the time signal is send again to resync:  

At 2:00 the sensor stops sending signals (probably to decode DCF77 
signals) and sends out for time signals to resync once ready.

Bitbuffer: [00] {95} fe a4 9e 20 32 02 4a 04 08 6c 66 be  
Binary:  
11111110101001001001111000100000001100100000001001001010000001000000100001101100011001101011111  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS  A?  B?  C?  D?  
                                  1   9   0   1   2   5   0   2   0   4   3   6  
                               (20)19      01.     25.     02  :   04  :   36  

Bitbuffer: [00] {95} fe a4 9e 20 32 02 4a 04 0a 49 cc 02  
Binary:  
11111110101001001001111000100000001100100000001001001010000001000000101001001001110011000000001  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS  A?  B?  C?  D?  
                                  1   9   0   1   2   5   0   2   0   5   2   4  
                               (20)19      01.     25.     02  :   05  :   24  

Bitbuffer: [00] {95} fe a4 9e 20 32 02 4a 04 0c 25 51 64  
Binary:  
11111110101001001001111000100000001100100000001001001010000001000000110000100101010100010110010  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS  A?  B?  C?  D?  
                                  1   9   0   1   2   5   0   2   0   6   1   2  
                               (20)19      01.     25.     02  :   06  :   12  

Bitbuffer: [00] {95} fe a4 9e 20 32 02 4a 04 0e 00 fa ec  
Binary:  
11111110101001001001111000100000001100100000001001001010000001000000111000000000111110101110110  
  1   1ssssssssiiiiiiiiB? ?   ?  YY  YY  MM  MM  DD  DD  HH  HH  MM  MM  SS  SS  A?  B?  C?  D?  
                                  1   9   0   1   2   5   0   2   0   7   0   0  
                               (20)19      01.     25.     02  :   07  :   00  

Then the regular signal is send every 45 sec  

Bitbuffer: [00] {95} fe 69 e4 cc 00 01 ff 0e 24 00 fa ec  
Binary:  
11111110011010011110010011001100000000000000000111111111000011100010010000000000111110101110110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm  SS  SS  A?  B?  C?  D?  
See folder 02 for a the signal decoding.  


----------------------------------------------------------------------------------------  

More training data of the station to the sensor:

Cycling the battery (x):
{95}fe7d05000001ffbc3a000000  
x  
{95}fe7b04e60001ffc426000000  
x  
{95}fe7884dc0001feecc2000000  
{95}fea588203202020c4421e2d4  
{95}fea588203202020c4421e2d4  
{95}fea588203202020c44b0ea6c  
{95}fea588203202020c468dbb1a  
{95}fea588203202020c4869d310  
{95}fe7884da0001ffd5a869d310  
x  
{95}fe6b44da0001ffda60000000  
{95}fea4b4203202020c6c82d178  
{95}fea4b4203202020c6e533db6  
{95}fea4b4203202020c702fba12  
{95}fea4b4203202020c720a1046  
{95}fe6b44da0001ffda600a1046  
x  
{95}fe7f64da0001ffca84000000  
{95}fea5f6203202020ca2100bb8  
{95}fea5f6203202020ca488d0f8  
{95}fea5f6203202020ca665858a  
{95}fe7f64da0001ffca8465858a  
x  
{95}fe6744dc0001ff65e8000000  
{95}fea474203202020e0253f3c2  
{95}fea474203202020e042e1dca  
{95}fea474203202020e060bb742  
{95}fea474203202020e06a6062e  
{95}fe6744dc0001ff65e8a6062e  
x  
{95}fe7864dc0001fe661c000000  
{95}fea586203202020e680f3236  
{95}fea586203202020e68ab0aaa  
{95}fea586203202020e6a8728a6  
{95}fea586203202020e6c6247a2  
{95}fe7864dc0001fe661c6247a2  
  
x with Low batt @ 2.25 V  
  
{95}fe6094de0001fec898000000  
{95}fea4092032020210068dd276  
{95}fea40920320202100869ba3c  
{95}fea40920320202100a4599f8  
{95}fea40920320202100c208cca  
{95}fe6094de0001fec898208cca  
{95}fe6094dc0001ffffcc208cca  


