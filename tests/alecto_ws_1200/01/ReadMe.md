Alecto WS 1200
--------------

A Thermometer with clock and wireless rain unit with temperature sensor.


Format notes
------------

The rain unit counts in 0.3 mm steps. The sensor counter increases from 
0 to 256 (r), the display keeps the difference. Temperatue is transmitted as 
a number (t), to get Celsius substract 40 and divide by 10. The (i) section seems
to be a sensor ID, it changes at battery change. While training for the station
connection the (d) part is 0, it seems to change after 10 min and afterwards daily.
The (m) part changes on message change, so it could be a checksum.


Flex decoder
------------

`rtl_433 -X 'n=name,m=OOK_PWM,s=500,l=1500,r=1000,g=10000,t=400,repeats=1,y=0'`
This command works, but I set g to 10000 without knowing what it does.

File comments
-------------

g001_433.92M_250k.cu8	Temp: 30.9 Celsius	Rain: 80.4 mm
Bitbuffer: [00] {95} fe 65 a5 8a 24 03 fe fa b0 a6 18 8c
Binary:
111111100110010110100101100010100010010000000011111111101111101010110000101001100001100010001100
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d
                        709       18
                      -40 / 10   * 0.3
                        30.9      5.4

g002_433.92M_250k.cu8   Temp: 30.8 Celsius      Rain: 80.4 mm
Bitbuffer: [00] {95} fe 65 a5 88 24 03 ff cd 80 a6 18 8c
Binary:
111111100110010110100101100010000010010000000011111111111100110110000000101001100001100010001100
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d
                        708       18
                      -40 / 10   * 0.3
                        30.8      5.4

g003_433.92M_250k.cu8   Temp: 23.7 Celsius      Rain: 81.9 mm
Bitbuffer: [00] {95} fe 65 a4 fa 2e 03 ff 6e 9e a6 18 8c
Binary:
111111100110010110100100111110100010111000000011111111110110111010011110101001100001100010001100
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d
                        637       23
                      -40 / 10   * 0.3
                        23.7      6.9

--- Now battery exchange on sensor and display ---

g004_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm
Bitbuffer: [00] {95} fe 6a 24 f4 00 01 fe e0 60 00 00 00
Binary:
111111100110101000100100111101000000000000000001111111101110000001100000000000000000000000000000
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d

g005_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm
Bitbuffer: [00] {95} fe 6a 24 f2 00 01 ff d9 56 00 00 00
Binary:
111111100110101000100100111100100000000000000001111111111101100101010110000000000000000000000000
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d

--- Now battery exchange on sensor and display ---

g006_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm
Bitbuffer: [00] {95} fe 6c e4 f0 00 01 ff 6f ac 00 00 00
Binary:
111111100110110011100100111100000000000000000001111111110110111110101100000000000000000000000000
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d

g007_433.92M_250k.cu8   Temp: --.- Celsius      Rain: --.- mm
Bitbuffer: [00] {95} fe 6c e4 ec 00 01 ff 45 7e 69 c8 ec
Binary:
111111100110110011100100111011000000000000000001111111110100010101111110011010011100100011101100
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d

g008_433.92M_250k.cu8   Temp: 22.8 Celsius      Rain: 0.9 mm
Bitbuffer: [00] {95} fe 6c e4 e8 06 01 fe df 1a 69 c8 ec
Binary:
111111100110110011100100111010000000011000000001111111101101111100011010011010011100100011101100
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d
                        628        3
                      -40 / 10   * 0.3
                        22.8      0.9

g009_433.92M_250k.cu8   Temp: -2.5 Celsius      Rain: 0.9 mm
Bitbuffer: [00] {95} fe 6c e2 ee 06 01 ff 6f ae 8f 92 64
Binary:
111111100110110011100010111011100000011000000001111111110110111110101110100011111001001001100100
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d
                        375        3
                      -40 / 10   * 0.3
                        -2.5      0.9

g010_433.92M_250k.cu8   Temp: -2.5 Celsius      Rain: 0.9 mm
Bitbuffer: [00] {95} fe 6c e2 ee 06 01 ff 6f ae 8f 92 64
identical to g009_433.92M_250k.cu8


--- Startup Binaries from g004 and g006 ---
111111100110101000100100111101000000000000000001111111101110000001100000000000000000000000000000
111111100110110011100100111100000000000000000001111111110110111110101100000000000000000000000000
  .   .   .   i   i ?ttttttttttrrrrrrrr   .   .   .   .   m   m   m   m   d   d   d   d   d   d


More bitbuffer results
----------------------

In case somebody tries to figure out the (m) and (d) parts, this could be usefull.

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





