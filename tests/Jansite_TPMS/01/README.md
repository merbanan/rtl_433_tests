# Jansite Solar TPMS (Internal/External) Model TY02S

Working Temperature:-40 °C to 125 °C
Working Frequency: 433.92MHz+-38KHz
Tire monitoring range value: 0kPa-350kPa+-7kPa

Data format: ID:28h S:4b P:8d T:8d CHK:8h

Data layout (nibbles):

    II II II IS PP TT CC

- I: 28 bit ID
- S: 4 bit Status (deflation alarm, battery low etc)
- P: 8 bit Pressure (best guess quarter PSI, i.e. ~0.58 kPa)
- T: 8 bit Temperature (deg. C offset by 50)
- C: 8 bit Checksum
- The preamble is 0xaa..aa9 (or 0x55..556 depending on polarity)

The checksum is currently unknown.
