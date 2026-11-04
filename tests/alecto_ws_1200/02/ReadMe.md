# Alecto WS 1200 - Version 2.0

A Thermometer with clock and wireless rain unit with temperature sensor.

Manual available at
https://www.alecto.nl/media/blfa_files/WS-1200_manual_NL-FR-DE-GB_V2.2_8712412532964.pdf

## Format notes

The rain unit counts in 0.3 mm steps. The sensor counter increases from 
0 to 65536(R, little endian), the display keeps the difference. Temperatue is transmitted as 
a number (t), to get Celsius substract 400 and divide by 10. The (i) section seems
to be a sensor ID, it changes at battery change. A status is ahead (s). While training for the station
connection the (d) part is 0, it a part of the last time stamp and changes afterwards daily.
The (c + m) part changes on message change. Starting at bit 7 (after 7 bits of 1) there 
is a CRC-8 poly 0x31 init 0 for 7 bytes (c). Then another checksum and the trailing 3 bytes. 
(B) indicates low battery.

PRE: 7b Type: 4b ID: 8b BATTERY: 1b ?:1b T: 10d R:<16d ?: 8h CRC: 8h MAC: 8h DATE: 35b

Example:  
11111110011110001000010011011010000000000000000111111111110101011010100001101001110100110001000  
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

Bitbuffer: [00] {95} fe 78 84 dc 00 01 fe ec c2 00 00 00  
Binary:  
11111110011110001000010011011100000000000000000111111110111011001100001000000000000000000000000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  

Then a couple of signals with the time pattern and a longer status are send. They are required 
to fix the station to the reciver. See folder 03 for the time signals.

PRE: 7b Type: 8b ID: 8b BATT: 1b ?: 1b ?: ??: 6b YY: 4d YY:4d MM: 4d MM: 4d DD: 4d DD: 4d HH: 4d HH: 4d MM: 4d MM: 4d SS: 4d SS: 4d ? 16b

Bitbuffer: [00] {95} fe a5 88 20 32 02 02 0c 44 21 e2 d4  
Bitbuffer: [00] {95} fe a5 88 20 32 02 02 0c 44 b0 ea 6c  
Bitbuffer: [00] {95} fe a5 88 20 32 02 02 0c 46 8d bb 1a  
Bitbuffer: [00] {95} fe a5 88 20 32 02 02 0c 48 69 d3 10  
Binary:  
11111110101001011000100000100000001100100000001000000010000011000100010000100001111000101101010  
11111110101001011000100000100000001100100000001000000010000011000100010010110000111010100110110  
11111110101001011000100000100000001100100000001000000010000011000100011010001101101110110001101  
11111110101001011000100000100000001100100000001000000010000011000100100001101001110100110001000  
  1   1ssssssssiiiiiiiiB  ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   

Then the regular signal is send

Bitbuffer: [00] {95} fe 78 84 da 00 01 ff d5 a8 69 d3 10  
Binary:  
11111110011110001000010011011010000000000000000111111111110101011010100001101001110100110001000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  

See folder 03 for a pairing procedure with signals.


## File comments

g001_433.92M_250k.cu8	Temp: 30.9 Celsius	Rain: 80.4 mm  
Bitbuffer: [00] {95} fe 65 a5 8a 24 03 fe fa b0 a6 18 8c  
Binary:  
11111110011001011010010110001010001001000000001111111110111110101011000010100110000110001000110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
                        709       18  
                     -400 / 10   * 0.3  
                        30.9      5.4  
  
g002_433.92M_250k.cu8   Temp: 30.8 Celsius      Rain: 80.4 mm  
Bitbuffer: [00] {95} fe 65 a5 88 24 03 ff cd 80 a6 18 8c  
Binary:  
11111110011001011010010110001000001001000000001111111111110011011000000010100110000110001000110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
                        708       18  
                     -400 / 10   * 0.3  
                        30.8      5.4  
  
g003_433.92M_250k.cu8   Temp: 23.7 Celsius      Rain: 81.9 mm  
Bitbuffer: [00] {95} fe 65 a4 fa 2e 03 ff 6e 9e a6 18 8c  
Binary:  
11111110011001011010010011111010001011100000001111111111011011101001111010100110000110001000110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
                        637       23  
                     -400 / 10   * 0.3  
                        23.7      6.9  
  
--- Now battery exchange on sensor and display ---  
  
g004_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm  
Bitbuffer: [00] {95} fe 6a 24 f4 00 01 fe e0 60 00 00 00  
Binary:  
11111110011010100010010011110100000000000000000111111110111000000110000000000000000000000000000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
  
g005_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm  
Bitbuffer: [00] {95} fe 6a 24 f2 00 01 ff d9 56 00 00 00  
Binary:  
11111110011010100010010011110010000000000000000111111111110110010101011000000000000000000000000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
  
--- Now battery exchange on sensor and display ---  
  
g006_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm  
Bitbuffer: [00] {95} fe 6c e4 f0 00 01 ff 6f ac 00 00 00  
Binary:  
11111110011011001110010011110000000000000000000111111111011011111010110000000000000000000000000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
  
g007_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm  
Bitbuffer: [00] {95} fe 6c e4 ec 00 01 ff 45 7e 69 c8 ec  
Binary:  
11111110011011001110010011101100000000000000000111111111010001010111111001101001110010001110110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
  
g008_433.92M_250k.cu8   Temp: 22.8 Celsius      Rain: 0.9 mm  
Bitbuffer: [00] {95} fe 6c e4 e8 06 01 fe df 1a 69 c8 ec  
Binary:  
11111110011011001110010011101000000001100000000111111110110111110001101001101001110010001110110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
                        628        3  
                     -400 / 10   * 0.3  
                        22.8      0.9  
  
g009_433.92M_250k.cu8   Temp: -2.5 Celsius      Rain: 0.9 mm  
Bitbuffer: [00] {95} fe 6c e2 ee 06 01 ff 6f ae 8f 92 64  
Binary:  
11111110011011001110001011101110000001100000000111111111011011111010111010001111100100100110010  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  
                        375        3  
                     -400 / 10   * 0.3  
                        -2.5      0.9  
  
g010_433.92M_250k.cu8   Temp: -2.5 Celsius      Rain: 0.9 mm  
Bitbuffer: [00] {95} fe 6c e2 ee 06 01 ff 6f ae 8f 92 64  
identical to g009_433.92M_250k.cu8  
  
  
--- Startup Binaries from g004 and g006 ---  
11111110011010100010010011110100000000000000000111111110111000000110000000000000000000000000000  
11111110011011001110010011110000000000000000000111111111011011111010110000000000000000000000000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1ccccccccmmmmmmmm   d   d   d   d   d   d  


## More bitbuffer results

[00] {95} fe 65 a2 b7 92 01 fe 14 60 a3 e4 52  
[00] {95} fe 65 a2 b9 92 01 ff 31 7e a3 e4 52  
[00] {95} fe 65 a2 b7 92 01 fe 14 60 a3 e4 52  
[00] {95} fe 65 a2 fd 92 01 ff de 70 a3 e4 52  
[00] {95} fe 65 a2 f3 92 01 fe fb 82 a3 e4 52  
[00] {95} fe 65 a3 1b 98 01 fe 8b 40 a3 e4 52  
[00] {95} fe 65 a3 2f 98 01 fe cd 96 a3 e4 52  
[00] {95} fe 65 a3 45 98 01 ff 76 56 a3 e4 52  
[00] {95} fe 65 a3 59 98 01 ff 5c 50 a3 e4 52  
[00] {95} fe 65 a4 ab 9a 01 fe e5 2e a3 e4 52  
[00] {95} fe 65 a4 ad 9c 01 fe 48 96 a3 e4 52  
[00] {95} fe 65 a4 af 9e 01 ff f2 44 a3 e4 52  
[00] {95} fe 65 a4 af a0 01 ff d8 2c a3 e4 52  
[00] {95} fe 65 a5 9d a0 01 ff 44 86 a6 18 8c  
[00] {95} fe 65 a5 9b a0 01 fe 7d bc a6 18 8c  
[00] {95} fe 65 a5 63 dc 01 ff 5c a0 a6 18 8c  
[00] {95} fe 65 a5 4d fa 01 fe d4 20 a6 18 8c  
[00] {95} fe 65 a5 30 00 03 fe 09 40 a6 18 8c  
[00] {95} fe 65 a5 16 02 03 ff cc ec a6 18 8c  

I also recorded readings with one bit changed (except nr. 3, with two changed bits):

[00] {95}fe6ce4dc0601fe98c890d3a8  
[00] {95}fe6ce4dc0801ff5f9090d3a8  
[00] {95}fe6ce4da0a01feeb1c90d3a8  
[00] {95}fe6ce4dc0a01ffd20690d3a8  
[00] {95}fe6ce4dc0c01fe467c90d3a8  
[00] {95}fe6ce4dc0e01fecb0290d3a8  
[00] {95}fe6ce4dc1001ffa9e290d3a8  
[00] {95}fe6ce4dc1201ff256090d3a8  
[00] {95}fe6ce4dc1401feb0ee90d3a8  
[00] {95}fe6ce4dc1601fe3c7c90d3a8  
[00] {95}fe6ce4dc1801fffa3c90d3a8  
[00] {95}fe6ce4dc1a01ff77ba90d3a8  
[00] {95}fe6ce4dc1c01fee32890d3a8  
[00] {95}fe6ce4dc1e01fe6eb690d3a8  
[00] {95}fe6ce4dc2001fe448e90d3a8  
[00] {95}fe6ce4dc2201fec91490d3a8  
[00] {95}fe6ce4dc2401ff5daa90d3a8  
[00] {95}fe6ce4dc2601ffd02090d3a8  

And of the training of station to the sensor:

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


