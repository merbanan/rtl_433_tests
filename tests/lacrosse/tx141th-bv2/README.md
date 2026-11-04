# LaCrosse TX141TH-Bv2 / TFA 30.3221

codes_test.txt/json cover a decoder fix from
https://github.com/merbanan/rtl_433/issues/2206: `lacrosse_tx141x_decode()`
required at least 3 exactly-matching repeated rows before accepting a
message, even though the TX141TH-Bv2 variant already carries its own
per-row CRC (`lfsr_digest8_reflect`). Real-world reports in that issue
showed messages with only one intact row (the other repeats corrupted by
noise/collisions) being silently dropped, despite the intact row being
independently verifiable via its CRC.

Fix (from knarrff's https://github.com/merbanan/rtl_433/commit/081de0ba,
applied to master): if the repeated-row search fails, scan individual
rows and accept the first one that is 40 or 41 bits and passes the CRC on
its own.

- codes_test.txt/json: a synthetic-but-realistic 4-row capture with only
  one CRC-valid row (the other 3 mutually distinct, i.e. no repeats at
  all) -- decodes only with the fix applied. Manually verified: a
  4-row capture with no CRC-valid row at all (id byte corrupted in all
  4) is still correctly rejected.
