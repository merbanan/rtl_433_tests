# Schou 72543 Rain ngauge

## General info
### Radio signal
* Frequency: 433.9 Mhz
* Modulaiton: ASK
* Period: ~45 seconds between messages
* Num rows: 3

Codes example:
{66}50fc467b7f9a832a8, {65}a1f88cf6ff3506550, {70}a1f88cf6ff3506557c

### Decoding
The actual data is 64 bit + 1 zero stop bit (see row 2). In addition, Row 1 has one zero start bit, and Row 3 has 5 additional stop bits.
```
{66}: [ 0 ] [ 1010 0001 1111 1000 ] [ 1000 ] [ 1100 ] [ 1111 0110 ] [ 1111 1111 ] [ 0011 0101 ] [ 0000 0110 ] [ 0101 0101 ] [ 0       ]
{65}: [   ] [ 1010 0001 1111 1000 ] [ 1000 ] [ 1100 ] [ 1111 0110 ] [ 1111 1111 ] [ 0011 0101 ] [ 0000 0110 ] [ 0101 0101 ] [ 0       ]
{70}: [   ] [ 1010 0001 1111 1000 ] [ 1000 ] [ 1100 ] [ 1111 0110 ] [ 1111 1111 ] [ 0011 0101 ] [ 0000 0110 ] [ 0101 0101 ] [ 0111 11 ]
KEY:  [ 0 ] [ IIII IIII IIII IIII ] [ SSSS ] [ NNNN ] [ rrrr rrrr ] [ RRRR RRRR ] [ tttt tttt ] [ TTTT TTTT ] [ CCCC CCCC ] [ 0??? ?? ]
* 0: Always zero
* I: 16 bit random ID. Resets to new value after every battery change
* S: Status bits
    [ X--- ]: Battery status:  0: OK, 1: Low battery
    [ -X-- ]: Repeated signal:  0: New, 1: Repeat of last message (4 repeats will happen after battery replacement)
    [ --XX ]: Assumed always to be 0
* N: 4 bit running count. Increased by 2 every value incremented by 2 every message, i.e. 0, 2, 4, 6, 8, a, c, e, 0, 2...
* Rr: 16 bit Rainfall in 1/10 millimeters per count. Initial value fff6 = 6552.6 mm rain
    r: lower 8 bit, initializes to f6
    R: Upper 8 bit, initializes to ff
* Tt: 16 bit temperature.
```
