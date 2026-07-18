# McPower Kinetic battery-less wall switch

See https://github.com/merbanan/rtl_433/issues/3102. @Sola85 reverse
engineered the frame layout and @ProfBoc75 cracked the CRC-16 (poly
0x1021, init 0xaa55) with reveng, both directly in the issue thread.

No raw IQ capture was ever attached to the issue -- only demodulated hex
pasted in the comments, from a single physical unit. `codes_test.txt`/
`codes_test.json` hold the 9 codes posted there (independently
reconfirmed against the CRC here before writing the decoder), split
across left-button and right-button presses; a third set of "no button,
harvested energy only" codes was also mentioned in the thread but not
posted as hex, so it isn't covered here. The 16 bit "id" field is
unconfirmed as a real per-device identifier since only one unit was ever
tested -- enabled by default anyway since the 16 bit CRC gives strong
protection against false positives. See the file's docstring.
