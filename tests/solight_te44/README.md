# Solight TE44

Generic wireless thermometer of chinese provenience, which might be sold as part of different kits.

 So far these were identified (mostly sold in central/eastern europe)
 - Solight TE44
 - Solight TE66
 - EMOS E0107T

Rated -50 C to 70 C, frequency 433,92 MHz, three selectable channels.

## Data structure:

12 repetitions of the same 36 bit payload, 1bit zero as a separator between each repetition.

36 bit payload format: `xxxxxxxx 10ccmmmm tttttttt 1111hhhh hhhh`

`x` - random key - changes after device reset - 8 bits
`c` - channel (0-2) - 2 bits
`m` - multiplier - signed integer, two's complement - 4 bits
`t` - temperature in celsius - unsigned integer - 8 bits
`h` - checksum - 8 bits

Temperature in C = `((256 * m) + t) / 10`