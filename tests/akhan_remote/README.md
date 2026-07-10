# Akhan 100F14 (HS1527 OTP encoder)

`01/` contains the original single-button remote captures (see `01/README.md`).

`codes_test.txt`/`codes_test.json` cover
https://github.com/merbanan/rtl_433/issues/1458 ("Akhan 100F14 three-button
variant is not decoded"). The three-button wall switch variant transmits the
same frame as the one/two-button units, just with slightly longer pulses
(~1092-1108 us vs ~1060-1064 us for "long"), which pushed some pulses past
the decoder's old `long_width + tolerance` cutoff and caused the pulse
slicer to intermittently mis-frame the message. Fixed by raising
`tolerance` from 80 to 100 us in `akhan_100F14.c`. The codes cover the
single-button unit, both buttons of the two-button unit, and all three
buttons of the three-button unit, extracted from the six `.cu8` samples
attached to the issue.
