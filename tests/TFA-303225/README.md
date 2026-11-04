# TFA Dostmann 30.3225.10 outdoor temperature sensor

The outdoor temperature sensor of the TFA "Rainman" rain gauge kit
(30.3004), sold alongside a separate rain gauge (30.3226.10). See
https://www.tfa-dostmann.de/en/product/digital-wireless-rain-gauge-rainman-47-3004/.

Reverse-engineered by @Crabat and @zuckschwerdt in
https://github.com/merbanan/rtl_433/issues/1759 (solved in 2021, decoder
added in 2026).

- `codes_test.txt`/`codes_test.json` - all 100 messages from the capture
  attached to the issue (`100_30.3225.10.zip`), covering 7 different
  sensor IDs and both battery states.

## Protocol

Decoded by `fineoffset_WH2_callback()` in `src/devices/fineoffset.c`. This
sensor shares the exact same 55-bit, `0xFE`-preamble wire format as
Fineoffset-WH2A (already supported), which is why it was originally
misidentified as WH2A with the temperature off by a consistent 40.0 C.

The two are told apart by the humidity byte: real WH2A units always
report a plausible 0-100% humidity there, while this (temperature-only)
sensor always sets it to a fixed `0xFF`. Confirmed against all 100
messages here plus the 5 real WH2A captures in
`../fineoffset/fineoffset_wh2A/01/` (0/100 and 0/5 counterexamples,
respectively).

Temperature is unsigned, offset by 40 C, scaled by 10 (Fineoffset-WH5
style) -- not WH2A's signed-magnitude encoding. The top bit of the 12-bit
temperature field is a low-battery indicator rather than a sign bit
(confirmed against the issue's own annotated "low battery"/"no low
battery" examples); it must be masked out before applying the offset,
or the temperature comes out ~205 C too high.

There is an additional 8-bit checksum after the CRC byte:
`b[5] == (b[0]+b[1]+b[2]+b[3]+b[4]) & 0xff`, holding on all 100 messages
here and all 5 real WH2A captures (so it's a leftover TODO in the WH2A
code, not unique to this sensor -- left unenforced there to avoid
regressing WH2A hardware variants not covered by the small sample here).
