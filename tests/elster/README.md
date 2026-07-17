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
