# Holman WS5029 (older PWM), OOK variant / BIOWIN 270208

Samples from https://github.com/merbanan/rtl_433/issues/1476, where the
device is a BIOWIN / 2measure / Bioterm No. 270208 weather station. It
turned out to be a rebrand of the Holman WS5029 (older PWM variant, see
`../02`) transmitting the identical frame -- same 0xAAA598 preamble, same
field layout, same `xor_shift_bytes(b, 10, 0x18)` checksum, same 0.79 mm
per count rain scale (confirmed by the issue's console deltas: 2 counts
between total readings 111.3 mm and 112.9 mm) -- but OOK modulated
instead of FSK, so it needs its own OOK protocol registration.

The wind direction field, unresolved in the 2020 issue thread, was
recovered by testing every 4-bit window of the then-unassigned tail bits
against the reporter's E/SE/SSE/S compass annotations; it sits directly
after the wind speed byte, matching the Holman layout exactly. The
checksum was independently recovered by GF(2) linear analysis of XOR
differences between the 28 known-good messages before it was recognized
as the already-known Holman `xor_shift_bytes` algorithm.

Barometric pressure (shown by the reporter's console) could not be
located anywhere in the frame; it is likely measured locally by the
console's own barometer rather than transmitted.

- `g001`/`g002` - the two raw captures attached to the issue (~433 MHz,
  250 kS/s), one transmission burst each
- `codes_test.txt`/`codes_test.json` - the 26 console-annotated codes
  from the reporter's BitBench analysis
