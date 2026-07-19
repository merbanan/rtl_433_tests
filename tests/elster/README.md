# Elster/Honeywell R2S/REXU power meters

See https://github.com/merbanan/rtl_433/issues/1196 for the multi-year
issue thread this decoder is based on, and
https://github.com/argilo/gr-elster for the reference protocol analysis
(Clayton Smith).

## Why there's no `.cu8` sample here

A companion PR (https://github.com/merbanan/rtl_433_tests/pull/323,
closed/unmerged) uploaded 427 real `.cs16` captures. None of them decode
with the new decoder (`src/devices/elster_power_meter.c`): most show no
usable FSK/Manchester pulse structure at all, matching the original
uploader's own note ("checked up to 37 so far, nothing obvious").

The only clean, decodable data found anywhere in the issue thread was
posted as RfRaw pulse-timing text (triq.org/pdv links), not as `.cu8`
files. `codes_test.txt` contains the Manchester-decoded bitstream
extracted from two of those posts, verified against the reference
gr-elster decode logic (CRC-16/X-25 valid, plausible meter/collector
addresses). No synthetic `.cu8` was generated from this data.

The decoder ships `.disabled = 1` until it can be verified against a
real, cleanly-received capture.

## Update: further findings, still no `.cu8`

@ther3zz reported (issue #1196) live CRC-valid decodes across ~15 meters,
confirming a rigid "beacon" frame template (LEN=40, FLAG=0x08, DST=0),
now detected as `frame_type: "beacon"` -- the second known-good code
below is one. Also reported: a second message type selected by a byte at
payload offset 14 (0x56 = AES-encrypted, 0x57 = cleartext mesh neighbour
table, not yet decoded here), and real CRC-valid frames up to LEN=189,
which the decoder's old `ELSTER_MAX_LEN` bound (64) was silently
rejecting before the CRC was ever checked -- fixed by raising it to 200.
Still no `.cu8`/`.cs16` capture was posted, so the decoder remains
`.disabled = 1`.

## Update: type-2 frames and real `.cu8` captures (issue #3618)

@ther3zz followed up with `elster_report.zip`: 32 real type-2 `.cu8`
captures plus a manifest listing each one's independently-computed frame
hex. This is a genuinely different physical layer from type-1 above (not
Manchester, whitened with 0xaa not 0x55, 16 bit length, ~4x the bit rate
-- confirmed at 7 us/bit by brute-force testing bit alignments against the
manifest's own frame hex until the CRC validated), decoded by a new
second device in the same file, `elster_power_meter2`.

`01/`-`04/` are one real capture each of the four frame classes in the
bundle (neighbour table, cleartext status, AES-encrypted, mesh/collector),
all `ignore`d for the same `-Y minmax` reason as above. `codes_test.txt`'s
type-2 section covers 29 of the 32 real captures (demodulated by rtl_433
itself, not hand-derived) -- the other 3 didn't produce a CRC-valid decode
here even though the reporter's own tool decoded 2 of them, likely a gap
between rtl_433's plain FSK_PCM demod and their more elaborate
self-centering analyzer on marginal signal.

Only the neighbour table's 4-byte-per-record neighbour address is decoded
(as `nbr_ids`); the remaining 16 bytes of each 20-byte record, and the
handful of varying bytes in the cleartext status frame, don't have a
confidently-attributable meaning from 8 samples each and are left in
`data_raw`. No cmd 0x23/0xce usage frame -- encrypted or clear -- has
ever been observed on this deployment (~900 captures/~30 meters/4 days),
so type-1's speculative `reading_kWh` remains just that.

## Update: a second neighbour table message class, 0x7f (issue #3618)

@ther3zz later reported a message byte of 0x7f producing a CRC-valid
neighbour table that the `msg == 0x57` check didn't recognize. `05/` is
a real capture of one, and `codes_test.txt` has its trimmed bitbuffer
code alongside the rest of the type-2 section. Confirmed against both
this and the existing `01/` capture: 0x7f records start one byte
earlier than 0x57's (offset 29 vs. 30 from the frame start), everything
else about the table layout is the same. The record start offset now
depends on which of the two message classes is seen; the meaning of the
header bytes that otherwise differ between the two classes is still
unknown.

Only one clean 0x7f capture has been posted so far; a second came in
too weak for rtl_433's demod to lock onto (per the reporter, their own
re-centering analyzer could still decode it) and wasn't attached.
