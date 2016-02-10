CONRAD Ersatz-/Zusatzsensor S014 (EUR 6.64EUR)
* http://www.conrad.de/ce/de/product/672868/ErsatzZusatzsensor-S014
* Nr. 67 28 68
* Model: S3318P outdoor sensor
* 2 x 1.5V AAA
* IPX3
* 43/2012
* For weatherstation S3318P (Best.Nr: 67 28 59)
* 3 Channels, LED is blinking on every TX, dipswitch to select temperature units °C/°F, TX-button (force send)


Transmit Interval: every ~50s
Message Format: 40 bits (10 nibbles)

Nibble:    1   2    3   4    5   6    7   8    9   10
Type:   PP IIIIIIII ??CCTTTT TTTTTTTT HHHHHHHH XB?????? PP
BIT/8   00 01234567 01234567 01234567 01234567 01234567 00
BIT/A   00 01234567 89012345 57890123 45678901 23456789 00
           0          1          2          3
I = sensor ID (changes on battery change)
C = channel number
T = temperature
H = humidity
X = tx-button pressed
B = low battery
P = Pre-/Postamble
? = unknown meaning


[01] {42} 04 15 66 e2 a1 00 : 00000100 00010101 01100110 11100010 10100001 00 ---> Temp/Hum/Ch:23.2/46/1

Temperature:
Sensor sends data in °F, lowest supported value is 90°F
12 bit uingned and scaled by 10 (Nibbles: 6,5,4)
in this case "011001100101" =  1637/10 - 90 = 73.7 °F (23.17 °C)

Humidity:
8 bit unsigned (Nibbles 8,7)
in this case "00101110" = 46

Channel number: (Bits 10,11) + 1
in this case "00" --> "00" +1 = Channel1

Battery status: (Bit 33) (0 normal, 1 voltage is below ~2.7 V)
TX-Button: (Bit 32) (0 indicates regular transmission, 1 indicates requested by pushbutton)

Rolling Code / Device ID: (Nibble 1)
changes on every battery change

Unknown1: (Bits 8,9) changes not so often
Unknown2: (Bits 36-39) changes with every packet, probably checksum
Unknown3: (Bits 34,35) changes not so often, mayby also part of the checksum



Sample data:
                              0        1        2        3        4        5
[01] {42} 40 82 76 d2 99 00 : 01000000 10000010 01110110 11010010 10011001 00		23.9	45	ch1 (tx button)
[01] {42} 40 82 76 e2 1e 00 : 01000000 10000010 01110110 11100010 00011110 00		23.9	46	ch1
[01] {42} 40 44 76 f4 17 00 : 01000000 01000100 01110110 11110100 00010111 00		23.9	79	ch1
[01] {42} 40 82 76 94 94 00 : 01000000 10000010 01110110 10010100 10010100 00		23.9	73	ch1 (tx button)
[01] {42} 40 87 76 e3 98 00 : 01000000 10000111 01110110 11100011 10011000 00		24.2	62	ch1 (tx button)
[01] {42} c7 0a 76 33 09 00 : 11000111 00001010 01110110 00110011 00001001 00		24.3	51	ch1
[01] {42} c7 0a 76 13 03 00 : 11000111 00001010 01110110 00010011 00000011 00		24.3	49	ch1
[01] {42} c7 89 76 d2 0c 00 : 11000111 10001001 01110110 11010010 00001100 00		24.3	45	ch1
[01] {42} c7 89 76 d2 84 00 : 11000111 10001001 01110110 11010010 10000100 00		24.3	45	ch1 (tx button)
[01] {42} 04 0b 76 e2 01 00 : 00000100 00001011 01110110 11100010 00000001 00		24.4	46	ch1
[01] {42} 04 1a 76 e2 85 00 : 00000100 00011010 01110110 11100010 10000101 00		24.3	46	ch2 (tx button)
[01] {42} 04 1b 76 d2 04 00 : 00000100 00011011 01110110 11010010 00000100 00		24.4	45	ch2
[01] {42} 04 1b 76 c2 01 00 : 00000100 00011011 01110110 11000010 00000001 00		24.4	44	ch2
[01] {42} 04 2a 76 d2 87 00 : 00000100 00101010 01110110 11010010 10000111 00		24.3	45	ch3 (tx button)
[01] {42} 04 2d 76 e2 01 00 : 00000100 00101101 01110110 11100010 00000001 00		24.5	46	ch3
[01] {42} 04 15 66 e2 a1 00 : 00000100 00010101 01100110 11100010 10100001 00		23.2	46	ch2
[01] {42} 50 60 76 d2 86 00 : 01010000 01100000 01110110 11010010 10000110 00		23.8	45	ch3 (tx button)
[01] {42} a9 8d 56 e2 85 00 : 10101001 10001101 01010110 11100010 10000101 00		22.7	46	ch1 (tx button)
[01] {42} a9 8d 56 d2 8a 00 : 10101001 10001101 01010110 11010010 10001010 00		22.7	45	ch1 (tx button)
[01] {42} a9 8e 56 d2 80 00 : 10101001 10001110 01010110 11010010 10000000 00		22.8	45	ch1 (tx button)
[01] {42} b9 41 76 23 c4 00 : 10111001 01000001 01110110 00100011 11000100 00		23.8	50	ch1 (tx button) + (battery low)



