099603a2

Nibble 0 = CC??
CC = Channel - 1
?? = ??

Nibble 1 = Power On ID

Nibble 4 = B?S?
B = Low Battery
? = 
S = Temperature Sign 0=+ 1=-
? =

Nibble 5 Nibble 2 . Nibble 3 = BCD Temperature in Celsius

Nibble 6 Nibble 7 = Byte 3 = Checksum
Checksum equals Sum of Bytes 0 1 2

So this transmission is:
Channel 1
Power On ID 9
Low Battery 0=OK
Sign 0=+
Temperature +39.6C
