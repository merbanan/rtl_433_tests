# Alecto WS 1200 - Version 1.0

A Thermometer with clock and wireless rain unit with temperature sensor.

Manual available at
https://www.alecto.nl/media/blfa_files/WS-1200_manual_NL-FR-DE-GB_V2.2_8712412532964.pdf

## Format notes

The rain unit counts in 0.3 mm steps. The sensor counter increases from 
0 to 65536(R, little endian), the display keeps the difference. Temperatue is transmitted as 
a number (t), to get Celsius substract 400 and divide by 10. The (i) section seems
to be a sensor ID, it changes at battery change. A status is ahead (s).
The (c) part changes on message change. Starting at bit 7 (after 7 bits of 1) there 
is a CRC-8 poly 0x31 init 0 for 7 bytes (c).  
(B) indicates low battery.

PRE: 7b Type: 4b ID: 8b BATTERY: 1b ?:1b T: 10d R:<16d ?: 8h CRC: 8h ?: 1b

Example:  
1111111001110010001001010000101000000000000000011111111000100000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1cccccccc  


## Flex decoder

A transmission is two packets (repeats) 36 ms apart.
Encoding is PWM with fixed gap length.
Short pulse of 450 us with 950 us gap (1500 us period),
Long pulse of 1450 us with 950 us gap (2500 us period).

`rtl_433 -X 'n=Alecto-WS-1200-v1.0,m=OOK_PWM,s=450,l=1450,r=37000,g=1100,t=400'`

The gap limit (g) here is slightly longer than the expected gap (950 us).
The reset limit (r) should be slightly longer than the packet distance, but 37 ms is too long.


## File comments

```
g001_433.92M_250k.cu8	Temp: 24.5 Celsius	Rain: 0.0 mm  
Bitbuffer: [00] {63} fe 72 25 0a 00 01 fe 20  
Binary:  
1111111001110010001001010000101000000000000000011111111000100000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1cccccccc  
                        645        0  
                     -400 / 10   * 0.3  
                        24.5      0.0  
  
g002_433.92M_250k.cu8   Temp: 24.6 Celsius      Rain: 0.0 mm  
Bitbuffer: [00] {63} fe 72 25 0c 00 01 ff 18  
Binary:  
1111111001110010001001010000110000000000000000011111111100011000  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1cccccccc  
                        646        0  
                     -400 / 10   * 0.3  
                        24.6      0.0  

g003_433.92M_250k.cu8   Temp: 24.7 Celsius      Rain: 0.0 mm  
Bitbuffer: [00] {63} fe 72 25 0e 00 01 fe 2e  
Binary:  
1111111001110010001001010000111000000000000000011111111000101110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1cccccccc  
                        647        0  
                     -400 / 10   * 0.3  
                        24.7      0.0  
  
g004_433.92M_250k.cu8   Temp: 24.7 Celsius      Rain: 0.0 mm  
Bitbuffer: [00] {63} fe 72 25 0e 00 01 fe 2e  
Binary:  
1111111001110010001001010000111000000000000000011111111000101110  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1cccccccc  
                        647        0  
                     -400 / 10   * 0.3  
                        24.7      0.0  
  
g005_433.92M_250k.cu8   Temp: 24.7 Celsius      Rain: 0.9 mm  
Bitbuffer: [00] {63} fe 72 25 0e 06 01 ff ba  
Binary:  
1111111001110010001001010000111000000110000000011111111110111010  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1cccccccc  
                        647        3  
                     -400 / 10   * 0.3  
                        24.7      0.9  
  
g006_433.92M_250k.cu8   Temp: 29.2 Celsius      Rain: 3.0 mm
Bitbuffer: [00] {63} fe 72 25 68 14 01 fe 3a  
Binary:  
1111111001110010001001010110100000010100000000011111111000111010  
  1   1ssssiiiiiiiiB?ttttttttttrrrrrrrrrrrrrrrr   1   1cccccccc  
                        692       10  
                     -400 / 10   * 0.3  
                        29.2      3.0  

```
