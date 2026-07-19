# Watchman Sonic Advanced/Plus -- CRC-shift bug captures

From @steve-burke's `book.zip` attachment to
https://github.com/merbanan/rtl_433/issues/3525, the reporter's own
evidence for a real CRC-validation bug: `oil_watchman_advanced.c` had
`BODY_LENGTH_BITS` wrong (144 instead of the correct 128), which shifted
the CRC check by up to a few bits and caused widespread false CRC
failures even on otherwise-good frames. Fixed by @ProfBoc75 in
merbanan/rtl_433 PR #3526 (also added a fallback check for one extra
stray bit that this particular signal occasionally inserts near the CRC
field).

**Requires `-Y minmax`.** Default classic pulse detection produces no
decode at all on these captures (this GFSK signal is a known-difficult
case for the classic detector, unrelated to the CRC bug above; see also
`../../oil_watchman/`, the sibling standard-FSK Watchman decoder, which
shows the same classic-vs-minmax sensitivity).

The original `book.zip` had 3 files (`g002`, `g003`, `g006`) capturing the
same real transmission repeatedly under different gain settings (`-Y
autolevel`, `-g 15`, `-g 30` respectively -- see the issue comments); all
3 decoded identically, so only `g002` is kept here:

```
rtl_433 -r g002_433.92M_250k.cu8 -R 234 -Y minmax -F json
{"model":"Oil-SonicAdv","id":5486027,"version":"1.7.3.0","temperature_C":13.0,"depth_cm":103,"status":144,"mic":"CRC"}
```

A `demod` file supplies `-Y minmax` to `bin/run_test.py`, so this
directory runs as a normal regression test.
