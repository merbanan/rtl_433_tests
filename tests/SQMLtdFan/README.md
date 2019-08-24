# SQM Co Ltd fan controllers

S.Q.M. Co Ltd of Taipei makes remote controls for ceiling fans by
manufacturers including Minka-Aire and Hampton Bay. These samples
were acquired using an Airspy R2 in 10Msps mode, observing a
DL41111T remote (FCC ID Y7ZDL4111T) in conjunction with a Minka-Aire F844-DRF
fan. The remote works at 303.866MHz. Commands are sent while a given button is
held down. Once released, an end-of-command message is sent. The
antenna is permanently attached to the PCB.

Both the 8-bit pairing code (the same 4-bit sequence repeated twice)
and the 4-bit command are decoded. The pairing code is selected using
the dipswitches in the remote. Both of the 4-switch blocks must have
the same setting, or the transmission will not succeed. A switch at
the high position translates to a 0; the low position is a 1.

This protocol can be decoded using a flex decoder (-X):

`n=SQMfan,m=OOK_PPM,short=330,long=660,reset=7000,gap=1000,bits=12,tolerance=50`

A user manual and FCC testing document are included. The user manual
was taken from a Minka-Aire fan insert; no generic manual could be
found. The FCC document was downloaded from fcc.gov.

## Commands

The command makes up the trailing 4 bits of each 12-bit row. Rows will be
sent so long as the button is held. Once released, one to four rows of the
EOM nibble will be sent.

| Nibble | Command     |
|--------|-------------|
| 5      | Stop fan    |
| 6      | Light down  |
| 7      | Fan speed 3 |
| A      | Light up    |
| B      | Fan speed 2 |
| D      | Fan speed 1 |
| F      | EOM         |

## Credit

This protocol was decoded by Nick Black (dankamongmen@gmail.com) on
assignment from Dirty South Supercomputing of Atlanta. A
[Youtube video](https://www.youtube.com/watch?v=PhBs0OIJ6ww) was
made featuring this decode.

## Research

URH suggests a different interpretation, but I've been unable to make it
completely work, while the protocol above makes complete sense. Here are
my notes from a URH session:

```
bitlen: 3300
ASK error tolerance 33

row: ~12.5ms, 38 "bits" demodulated, 13 long or short pulses
(11) Active_L = ~640--670us
(1) Active_s = ~303--323us
(00) Inactive_L == 680us
(0) Inactive_s == 340us

Inactive_s always and only precedes Active_L
Inactive_L always and only precedes Active_s

claims no traffic == 0, short == 1, long == 11
seems more likely no traffic == nothing, short = 0, long = 1?
on-off keying using NRZ

------------REMOTE 1-----------DDDD DDDD--------
924924b258 -- sssssssssLssL
10010010010--0100100100100--10-1100-1001-011
9249249248 -- sssssssssssss
10010010010--0100100100100--10-0100-1001-001 (EOM)

9249249658 -- ssssssssssLsL
10010010010--0100100100100--10-0101-1001-011
followed by EOMs

924924b2c8 -- sssssssssLsLs
10010010010--0100100100100--10-1100-1011-001

9249249648 -- ssssssssssLss
10010010010--0100100100100--10-0101-1001-001

92492492c8 -- sssssssssssLs
10010010010--0100100100100--10-0100-1011-001

924924b248 -- sssssssssLsss
10010010010--0100100100100--10-1100-1001-001


------------REMOTE 2-----------DDDU DDDU--------
R1B1(D): 10010010010--0100100100100--10-1100-1001-011
R2B1(D): 10010010010--1100100100101--10-1100-1001-011

R1B2(U): 10010010010--0100100100100--10-0101-1001-011
R2B2(U): 10010010010--1100100100101--10-0101-1001-011

11 bit fixed preamble: 10010010010, common to all remote configurations
13 bit identifier, different per 16 configs:
 R1: 0100100100100 DDDD (0924)
 R2: 1100100100101 DDDU (1925)
2 bit fixed 10
11 bits for command word:
 D: 110-0100-1011 (64b)
 U: 010-1100-1011 (2cb)
 L: 110-0101-1001 (659)
 T: 010-1100-1001 (2c9)
 R: 010-0101-1001 (259)
 C: 110-0100-1001 (649)
EM: 010-0100-1001 (249)
```
