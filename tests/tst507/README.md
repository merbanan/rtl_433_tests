TST (Truck Systems Technologies) 507 Series TPMS
Aftermarket TPMS system for trucks & RV's.  Uses 2 types of valve stem screw-on sensors, one a "cap" type and the other a "flow-thru" type.  I use 6 flow-thrus on my RV and 4 on my Jeep.  The sensors are read via a small dash mounted receiver. 

https://tsttruck.com/507-series-4-flow-thru-sensor-tpms-system-with-color-displatst-507-ft-4-c.html

From manual:
Temp range = 40F-176F / -40C-80C
Pres range = 0-198psi / 0-13.5bar
Temp accuracy = +/- 3F
Pres accuracy = +/- 3psi, 0.2bar

Info gathered so far: Uses 433.92Mhz (nominally).  Each sensor has a 6 character ID, known to the user and needed to setup the receiver.  Sensors seem to transmit at varying intervals, and do transmit when not moving.  

Had some success with:
rtl_433 -S all -s 1024k -X 'n=tst,m=OOK_MC_ZEROBIT,s=50,l=50,r=1000,invert'

Data stream:  "ffffc259f5fd2a4c0001"

Preamble:    FFFF

checksum:    C2

ID:          59F5FD

Data:        2A4C0001

Pres:        108.1 psi

Temp:        78.8 F

TST reports: 108 psi / 79 F

Checksum seems to be mod 256 of ID and Data bytes.

Data bytes are 2 byte little-endian, so above is "00 01 2A 4C"

Nibbles 0-2 are unknown. Haven't seen them change.

Nibbles 3-5 (12 bits) are pressure (kPa * 0.4)

Nibbles 6-7 (8 bits) are temperature with offset (C + 50)

I have seen a fair amount of lines with seemingly good data, but bad checksum.  Maybe I need a different rtl_433 option?
