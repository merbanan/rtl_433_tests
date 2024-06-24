
# ARAD / Master Meter Dialog3G Water utility  meter


![image](https://github.com/avicarmeli/rtl_433_tests/assets/32562196/f8b5d2ca-9960-4d50-87aa-c5e46b024c86)

Arad/Master Meter Dialog3G water utility meter.
FCC-Id: TKCET-733

Massage is being sent once every 30 second.

The massage look like that:

00000000FFFFFFFFFFFFFFSSSSSSSSXXCCCCCCXXXF?????????XFF

where:

00000000 is preamble.

FFFFFFFFFFFFFF  is fixed in time and the same for other meters in the neighborhood. Probably gearing ratio. The payload is 3e690aec7ac84b.

SSSSSSSS  is Meter serial number.  for instance fa1c9073 =>  fa1c90 = 09444602, little endian 73= 'S'

XX no idea.

CCCCCC is the counter reading little endian for instance a80600= 1704

XXX no idea.

F  is fixed in time and the same for other meters in the neighborhood. With payload of 5.

????????? probably some kind of CRC or checksum - here is where I need help.

X is getting either 8 or 0 same for other meters in the neighborhood.

FF is fixed in time and the same for other meters in the neighborhood.With payload f8.
