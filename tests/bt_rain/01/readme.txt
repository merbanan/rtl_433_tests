Sample for the rain gauge from Biltema.se Art.No: 84-0861.
It sometimes triggers the springfield.c device but not always.
Just like springfield it has six sets of 37 bits and a last set of 36 bits.

Nibble[0] and nibble[1] is the id, changes with every reset.
Nibble[2] first bit is battery (0=OK).
Nibble[3] bit 1 is tx button pressed.
Nibble[3] bit 2 = below zero, subtract temperature with 1024.
Nibble[3](bit 3 and 4) + nibble[4] + nibble[5] is the temperature in Celsius with one decimal.
Nibble[2](bit 2-4) + nibble[6] + nibble[7] is the rain rate, increases 25!? with every tilt of the teeter (1.3 mm rain) after 82 tilts it starts over but carries the rest to the next round e.g tilt 82 = 2 divide by 19.23 to get mm.
Nibble[8] is checksum, have not figured it out yet. Last bit is sync? or included in checksum?.

