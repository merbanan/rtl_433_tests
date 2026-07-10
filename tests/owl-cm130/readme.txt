OWL CM130 energy monitor

See https://github.com/merbanan/rtl_433/issues/1493.

Sister device to the CM160/CM180, Oregon-Scientific v3 family, OOK
Manchester, 97-bit message, preamble 00 00 00 60.

Contents:
- 01/       three raw .cu8 captures (reset-button presses, no reading)
- codes.txt all known raw messages with their reference readings:
            @mzealey's 15 rflink cross-referenced codes and @synx508's
            32 webcam-logged display readings

No CM130 decoder is merged into rtl_433 yet (there is an unmerged
feat-cm130 branch with partial, power-only decoding). The data here is
kept for whoever finishes the decoder. What is known so far, from
analysing codes.txt:

- power_W = ((b[3] << 8) | (b[5] >> 4)) / 16 after nibble reflection;
  confirmed against the display (the feat-cm130 branch is missing the
  /16 and so reads 16x too high, as reported in the issue)
- energy is a 36-bit little-endian counter in bytes 6..9 (plus the low
  nibble of byte 5), incrementing ~256 J per count; the absolute kWh
  offset/scale is still unknown
- byte 11 is a checksum: it is provably linear over GF(2) (rank 31, no
  contradictions over 50 messages) but does not match any standard CRC-8
  or Oregon/LFSR digest, so the exact formula is still open

To finish this, more captures with matching meter readings across a
wider power/energy range are needed (as the maintainer noted in the
issue).
