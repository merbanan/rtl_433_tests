IKEA Sparsnäs is a wireless energy display. A battery powered sender is attach do your house's utility meter. These have an impulse LED which is read by the Sparsnäs sender. The sender then sends the pulse count to the display unit every 15 seconds.

The protocol has been extensively documented at:

https://github.com/kodarn/Sparsnas

It is unnecessary to repeat everything here. In short the data is sent over 868MHz, FSK. 

There is a CRC checksum, and some XOR encryption (or obfuscation rather). Each sender has a 6 digit number printed in the battery compartment. This serves as a decryption key.

A working decryption and CRC check is implemented here:

https://github.com/strigeus/sparsnas_decoder/blob/master/sparsnas_decode.cpp

Samples are in the ./samples/ folder here. These are for a sender with the number 617633.
As I have very little experience with rtl_433 and radio data, my only way to identify packets is their 15 sec time spaceing. It is very possible that there are some false positives in here.

Additional samples are available at kodarns github repository at:

https://github.com/kodarn/Sparsnas/tree/master/Samples

The sender numbers are the last 6 digits in the directory name.
