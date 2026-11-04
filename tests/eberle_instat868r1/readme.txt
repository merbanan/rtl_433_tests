Eberle Instat 868r1 floor heating thermostat remote

See https://github.com/merbanan/rtl_433/issues/1951 for the original request, and
https://github.com/dottoreD/rtl_433_tests (tests/Eberle/Instat 868r1/) for the real
captures and reverse-engineering notes this decoder is based on: readme.md (device
overview, real capture example), protocol.txt (draft nibble layout, checksum unsolved
at the time), on_off.txt (36 real "on"/"off" captures for one sender), learn.txt /
learn_Bitstream.txt (927 real "learn" events, each with a known random ID, plus their
raw bitstreams).

868 MHz 2-FSK, 3 identical repeats per button press. 82 raw (chip) bits per repeat:
a 30 bit fixed preamble/"beginning", then a 52 bit differential-Manchester-encoded
"code part" (bitbuffer_differential_manchester_decode()) that decodes to 25 bits: a
fixed leading bit, then 24 data bits as 6 nibbles.

Those 24 bits are read two different ways:

- Checksum: 6 nibbles of 4 raw bits, each nibble read LSB-first (first-received bit
  is the lowest-order bit). Sum of the 6 nibbles is always 0xb (mod 16). This is the
  part protocol.txt's author never solved (his hex nibbles are Gray-decoded and
  complemented, see below, which is a bitwise-linear transform that does not preserve
  an arithmetic sum with carries -- so the checksum that's a plain sum in the raw
  representation looks like noise once Gray-decoded, matching his own "XOR works for
  part of the data, not all" note). Confirmed against all 963 real examples below.
- ID/action/data: the same 24 bits, Gray-decoded (cumulative XOR from the first bit)
  then complemented, then split into 6 nibbles MSB-first: 12 bit ID, then a 4 bit
  action code, then a 4 bit action-dependent data nibble, then the checksum nibble
  (already covered above). This matches protocol.txt's hex nibbles and his stated
  action codes exactly for Learn (confirmed against all 927 real learn.txt IDs) and
  for the On/Off rolling code (confirmed against all 36 real on_off.txt captures,
  for the one ID-odd sender in that data). The full action code table, including
  the ID-even On/Off codes and Reset (neither directly present in dottoreD's real
  captures), is independently confirmed by a second, unrelated reverse engineering
  effort: crasu's GNU Radio based decoder, https://github.com/crasu/gnu-heating --
  parser/parser.py's cmd_dict, with its binary keys converted to hex, is exactly
  the same table as protocol.txt's.

Modulation timing (short_width/long_width in the decoder) is 400 us, taken from
crasu's GNU Radio flowgraph (packet_decoder.py in the repo above): it resamples a
2 Msps capture down to 12500 Hz (decimation=160) then averages every 5 of those
into one output bit (gr-bitslice's slicer(omega=5)), i.e. 2500 bps. This is
consistent with a ~30 ms elevated-power window found in one of dottoreD's real
VN0101 captures while analyzing it directly in the frequency domain (82 bits *
400 us = 32.8 ms for one repeat) -- rtl_433's own OOK-oriented pulse analyzer
(-A) and FSK squelch (-Y ...) could not lock onto that capture at any short_width
tried, because its envelope is constant (being FSK) and there's no amplitude edge
for the analyzer's squelch to trigger on. So this has still not been confirmed
end-to-end against a live receiver or raw capture with this decoder, only the
bit-level protocol logic has (via the -y test vectors below, which inject the
already-known-correct 82 raw bits directly, bypassing pulse detection). reset_limit
is a guess pending real hardware/capture confirmation.

- codes_test.txt/json - all 963 real examples available in dottoreD's data (36 real
  On/Off captures for one physical sender, from on_off.txt, plus 927 real Learn
  events each with a distinct random ID, from learn.txt/learn_Bitstream.txt) as -y
  test vectors, in that order, with 4 exact duplicates removed (on_off.txt's 16 step
  rolling code wrapped around within the recorded sample window) -- 959 unique codes.
  All match the decoder's output exactly.
