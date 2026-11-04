Arad/Master Meter Dialog3G water utility meter

See https://github.com/merbanan/rtl_433/issues/1992,
https://github.com/merbanan/rtl_433/issues/3459, and
https://github.com/merbanan/rtl_433/pull/3489.

FSK Manchester-zerobit, 4-byte sync match, 88-entry XOR checksum table over
11 payload bytes with up to 3-bit error correction (see arad_ms_meter.c).

codes_test.txt/json contain 40 raw codes extracted from -R 260:v verbose
logs posted in issue #3459 by Lantryy, AkaBoing, and ProfBoc75/assafms
during the several-month crowd-sourced reverse-engineering of the checksum
(the same effort that produced the XOR mask table now in the decoder).
They cover 14 distinct real meters across three known hardware variants
(standard, "Sonata"/0x40, and an older 3D0C model) and all validate with a
clean checksum (corrections: 0).

The logged codes needed inverting (bitwise NOT of every byte) relative to
what -y expects; both polarities were tried against all extracted codes,
and only the correct polarity is included here.

Known issue, not caused by this decoder: two of these meters report a
volume that doesn't match their physical register reading, confirmed
against the ground truth in issue #3459:
- id 09750998-27: decodes to 362.0 gal, but the meter's actual reading is
  3620 gallons -- exactly 10x off, consistent with a wrong gear/scale
  auto-detection for this meter's flag combination. Can be worked around
  today with the decoder's "gear=1" option.
- id 13461653-27: decodes to 7310.3 gal, but the meter face reads 136,984
  gallons -- not a clean scale factor, cause unconfirmed (possibly a
  genuinely different field encoding for this meter, possibly a hardware
  defect on this specific unit, as speculated in the issue).

No raw .cu8 captures are included: the two IQ capture sets posted in the
issue (111 files total) turned out to need real demodulator retuning to
decode (measured ~245kHz/-130kHz FSK deviation, wider than the decoder's
configured short_width expects) -- a separate investigation from the
checksum work landed in PR #3489.
