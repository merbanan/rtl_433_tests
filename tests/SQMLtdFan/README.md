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
