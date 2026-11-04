# Cotech 36-7900 rain gauge

See https://github.com/merbanan/rtl_433/issues/3537.

`g004_433.92M_250k.cu8` is one of the reporter's real captures.

`codes_test.txt`/`codes_test.json` cover all 169 codes posted across
the whole issue thread (2026-06-03 to 2026-06-07), demodulated by
rtl_433 itself via a flex decoder, not hand-transcribed. This spans a
full day's smooth diurnal temperature swing (confirming the
temperature formula) and a controlled multi-tip rain gauge test
(confirming the rain field is a monotonic counter, not a rate --
jumped from 0 by ~39-42 per confirmed bucket tip and stayed flat
otherwise). Uses a `repeat` file (8) since the decoder requires that
many matching repeated rows in lieu of a real CRC.

No computed checksum was found, but bit-level analysis across all 66
unique codes here showed a 24 bit span that's exactly zero in every
one (see the decoder's doc comment) -- checked as a plausibility gate,
which also narrowed the rain field from an assumed 36 bits down to the
12 that actually vary. This incidentally used to also satisfy
`UniFan-24V`'s much weaker checksum (a 4-bit XOR fold, ~1-in-16 odds)
when a row was repeated byte-for-byte via `-y`; that's resolved now
that the reserved-bits check is in place.
