Quigg BBQ GT-TMBBQ-05

BBQ thermometer sold at Aldi (germany)
Simple device, no possibility to select channel. Single temperature measurement.

The temperature is transmitted in Fahrenheit with an addon of 90. Accurycity is 10 bit. No decimals.
One data row contains 33 bits and is repeated 8 times. Each followed by a 0-row. So we have 16 rows in total.
First 9 bits seem to be a static header, I assume for sync purposes (001001001).
Next 8 bits contain the lower 8 bits of the temperature.
Next 8 bits are static. Purpose unknown. Maybe hard wired channel inside device? 
Next 2 bits contain the upper 2 bits of the temperature
Next 6 bits vary, but purpose is unknown. I assume a kind of CRC as they are the same for same temperatures.

Here's the data I used to reverse engineer
001001001100010000111100110010110  HI
001001001010101010111100110010000  507
001001001010011010111100110010111  499
001001001110101110111100101010110  381
001001001110000000111100101011110  358
001001001001011010111100101010001  211
001001001001000000111100101000011  198
001001001111010110111100100000110  145
001001001101100010111100100001001  89
001001001101011010111100100010101  83
001001001101011010111100100010101  83
001001001101010110111100100010011  81
001001001101010010111100100000000  79
001001001101010000111100100010000  78
001001001101001110111100100011111  77
001001001101001100111100100001101  76
001001001101001010111100100001100  75
001001001101001010111100100001100  75
001001001101000110111100100001010  73
001001001100010100111100100010000  48
001001001011011110111100100000010  21
001001001011001110111100100011011  13
001001001010010010111100100011011  LO


Frame structure:
    Byte:             1        2        3
    Type:   001001001 tttttttt ssssssss TTcccccc 

tt = temperature+90 F lower 8 bits
TT = temperature+90 F upper 2 bits
ss = unknown, static -> maybe channel?
cc = unknown, changes -> maybe CRC?
