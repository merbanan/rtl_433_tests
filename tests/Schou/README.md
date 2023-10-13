# Schou 72543 Rain gauge

## General info
* Brand: Schou
* Model: 72543
* Data:
  * Rain: 0.1 mm resolution, tilting cup mechanism
  * Temperature: 0.1 °F resolution with a range of -40 °F to 158 °F
* Manual: https://damcache.harald-nyborg.dk/v-637714538838373967/eb/48/ba16-4d51-493f-91cf-76383d70d3b0/18910_478016.pdf
or https://api.p-lindberg.dk/Perfion/File.aspx?id=193bb670-4d74-4b9f-bf49-e0adeb53e85f

### Radio signal
* Frequency:  433.95 Mhz
* Modulaiton: ASK
* Interval:   45 seconds (almost) between transmissions
* Num rows:   3
  * Row 1: 66 bit
  * Row 1: 66 bit
  * Row 1: 70 or 71 bit

Codes example:
{66}50fc467b7f9a832a8, {65}a1f88cf6ff3506550, {70}a1f88cf6ff3506557c

### Decoding
The actual data is 64 bit + 1 zero stop bit (see row 2). In addition, Row 1 has one zero start bit, and Row 3 has 5 additional stop bits.
```
{66}: [ 0 ] [ 1010 0001 1111 1000 ] [ 1000 ] [ 1100 ] [ 1111 0110 ] [ 1111 1111 ] [ 0011 0101 ] [ 0000 0110 ] [ 0101 0101 ] [ 0       ]
{65}: [   ] [ 1010 0001 1111 1000 ] [ 1000 ] [ 1100 ] [ 1111 0110 ] [ 1111 1111 ] [ 0011 0101 ] [ 0000 0110 ] [ 0101 0101 ] [ 0       ]
{70}: [   ] [ 1010 0001 1111 1000 ] [ 1000 ] [ 1100 ] [ 1111 0110 ] [ 1111 1111 ] [ 0011 0101 ] [ 0000 0110 ] [ 0101 0101 ] [ 0111 11 ]
KEY:  [ 0 ] [ IIII IIII IIII IIII ] [ SSSS ] [ NNNN ] [ rrrr rrrr ] [ RRRR RRRR ] [ tttt tttt ] [ TTTT TTTT ] [ CCCC CCCC ] [ 0??? ?? ]
* 0:  Always zero
* ?:  Either 1 or 0
* I:  16 bit random ID. Resets to new value after every battery change
* S:  Status bits
      [ X--- ]: Battery status:  0: OK,  1: Low battery
      [ -X-- ]: Repeated signal: 0: New, 1: Repeat of last message (4 repeats will happen after battery replacement)
      [ --XX ]: Assumed always to be 0
* N:  4 bit running count. Increased by 2 every value incremented by 2 every message, i.e. 0, 2, 4, 6, 8, a, c, e, 0, 2...
* Rr: 16 bit Rainfall in 1/10 millimeters per count. Initial value fff6 = 6552.6 mm rain
      r: lower 8 bit, initializes to f6
      R: Upper 8 bit, initializes to ff
* Tt: 16 bit temperature.
      t: lower 8 bit
      T: Upper 8 bit
* C:  Checksum. Running 8 bit sum of the data left of the checksum.
      E.g. {65}a1f88cf6ff3506'55'0 Checksum is 55 obtained as ( a1 + f8 + 8c + f6 + ff + 35 + 06 ) = 455 i.e. 55
```

### Test data
The five datasets pressent is taken out of a longer log, of which some is shown below:
```
File                    Row 1,                 Row 2,                 Row 3,                  ID,   BAT, Repeat N  Rain      Temp_F  CHECKSUM
                        {66}2f7ac27bffc182aa8, {65}5ef584f7ff8305550, {71}5ef584f7ff83055502, 5ef5, LOW, No,    4, 6552.7mm, 51.1°F, 55 (OK)
 g764_433.89M_250k.cu8  {66}2f7ac37bffc182ab8, {65}5ef586f7ff8305570, {71}5ef586f7ff83055702, 5ef5, LOW, No,    6, 6552.7mm, 51.1°F, 57 (OK)
 g765_433.89M_250k.cu8  {66}18f7007b7fc102cd8, {65}31ee00f6ff82059b0, {71}31ee00f6ff82059b02, 31ee, OK,  No,    0, 6552.6mm, 51.0°F, 9b (OK)
 g766_433.89M_250k.cu8  {66}18f7207b7fc102ed8, {65}31ee40f6ff8205db0, {71}31ee40f6ff8205db02, 31ee, OK,  Yes,   0, 6552.6mm, 51.0°F, db (OK)
                        {66}18f7207b7fc102ed8, {65}31ee40f6ff8205db0, {71}31ee40f6ff8205db02, 31ee, OK,  Yes,   0, 6552.6mm, 51.0°F, db (OK)
                        {66}18f7207b7fc102ed8, {65}31ee40f6ff8205db0, {71}31ee40f6ff8205db02, 31ee, OK,  Yes,   0, 6552.6mm, 51.0°F, db (OK)
                        {66}18f7207b7fc102ed8, {65}31ee40f6ff8205db0, {71}31ee40f6ff8205db02, 31ee, OK,  Yes,   0, 6552.6mm, 51.0°F, db (OK)
                        {66}18f7207b7fc102ed8, {65}31ee40f6ff8205db0, {71}31ee40f6ff8205db02, 31ee, OK,  Yes,   0, 6552.6mm, 51.0°F, db (OK)
                        {66}18f7017b7fc282d00, {65}31ee02f6ff8505a00, {71}31ee02f6ff8505a002, 31ee, OK,  No,    2, 6552.6mm, 51.3°F, a0 (OK)
                        {66}18f7027b7fc802d68, {65}31ee04f6ff9005ad0, {71}31ee04f6ff9005ad02, 31ee, OK,  No,    4, 6552.6mm, 52.4°F, ad (OK)
                        {66}18f7037b7fca02d98, {65}31ee06f6ff9405b30, {71}31ee06f6ff9405b302, 31ee, OK,  No,    6, 6552.6mm, 52.8°F, b3 (OK)
                        {66}18f7047b7fcd82de0, {65}31ee08f6ff9b05bc0, {71}31ee08f6ff9b05bc02, 31ee, OK,  No,    8, 6552.6mm, 53.5°F, bc (OK)
                        {66}18f7057b7fcf02e08, {65}31ee0af6ff9e05c10, {71}31ee0af6ff9e05c102, 31ee, OK,  No,   10, 6552.6mm, 53.8°F, c1 (OK)
                        {66}18f7067b7fd082e30, {65}31ee0cf6ffa105c60, {71}31ee0cf6ffa105c602, 31ee, OK,  No,   12, 6552.6mm, 54.1°F, c6 (OK)
                        {66}18f7077b7fd182e50, {65}31ee0ef6ffa305ca0, {71}31ee0ef6ffa305ca02, 31ee, OK,  No,   14, 6552.6mm, 54.3°F, ca (OK)
                        {66}18f7007b7fd282df0, {65}31ee00f6ffa505be0, {71}31ee00f6ffa505be02, 31ee, OK,  No,    0, 6552.6mm, 54.5°F, be (OK)
                        {66}18f7017b7fd302e08, {65}31ee02f6ffa605c10, {71}31ee02f6ffa605c102, 31ee, OK,  No,    2, 6552.6mm, 54.6°F, c1 (OK)
                        {66}18f7027b7fd382e20, {65}31ee04f6ffa705c40, {71}31ee04f6ffa705c402, 31ee, OK,  No,    4, 6552.6mm, 54.7°F, c4 (OK)
...                     ...                    ...                    ...                     ...   ...  ...   ... ...       ...     ...
g1083_433.89M_250k.cu8  {66}18f7037fffe902fd0, {65}31ee06ffffd205fa0, {71}31ee06ffffd205fa02, 31ee, OK,  No,    6, 6553.5mm, 59.0°F, fa (OK)
g1084_433.89M_250k.cu8  {66}18f70400006902ff0, {65}31ee080000d205fe0, {71}31ee080000d205fe02, 31ee, OK,  No,    8,    0.0mm, 59.0°F, fe (OK)
                        {66}18f70500006902800, {65}31ee0a0000d205000, {71}31ee0a0000d2050002, 31ee, OK,  No,   10,    0.0mm, 59.0°F, 00 (OK)
                        {66}18f70600006902810, {65}31ee0c0000d205020, {71}31ee0c0000d2050202, 31ee, OK,  No,   12,    0.0mm, 59.0°F, 02 (OK)
                        {66}18f70700806902828, {65}31ee0e0100d205050, {71}31ee0e0100d2050502, 31ee, OK,  No,   14,    0.1mm, 59.0°F, 05 (OK)
                        {66}18f70000806982fc0, {65}31ee000100d305f80, {71}31ee000100d305f802, 31ee, OK,  No,    0,    0.1mm, 59.1°F, f8 (OK)
                        {66}18f70101006982fd8, {65}31ee020200d305fb0, {71}31ee020200d305fb02, 31ee, OK,  No,    2,    0.2mm, 59.1°F, fb (OK)
                        {66}18f70201006982fe8, {65}31ee040200d305fd0, {71}31ee040200d305fd02, 31ee, OK,  No,    4,    0.2mm, 59.1°F, fd (OK)
                        {66}18f70301006982ff8, {65}31ee060200d305ff0, {71}31ee060200d305ff02, 31ee, OK,  No,    6,    0.2mm, 59.1°F, ff (OK)
```


