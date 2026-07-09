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
