# Esun EN2053 two-channel BBQ thermometer

Generic-brand two-probe wireless BBQ/meat thermometer, FCC ID
2APN2-EN2053 (Fuzhou Esun Electronic Co.), sold under various names,
e.g. "Feelle Digital Thermometer" (X0028WROHL).

See https://github.com/merbanan/rtl_433/issues/1478.

- `01/` - the four raw `.cu8` captures attached to the issue
  (`ch1_around_72-to-73F.tar.gz`; probe 1 at 72-73 F, probe 2
  disconnected)
- `codes_test.txt`/`codes_test.json` - all 37 known-good messages: the
  annotated table from the issue body, the messages recovered from the
  40 s AM audio recording attached to the issue (decoded from the .wav
  envelope), and the `01/` captures

The 8-bit checksum, unsolved in the 2020 issue thread, packs four
even-parity flags and a modulo-8 byte sum (bits 0-2: sum of the four
message bytes mod 8; bit 3: always 0; bits 4-7: even parity of bytes
0-3). It was recovered by bit-plane analysis against the machine-decoded
messages after CRC/LFSR/additive model searches all failed, and matches
all 37 known-good messages (the issue's hand-transcribed table proved to
be 100% accurate).
