# Mercedes Benz Sprinter 4500 TPMS sensor

See https://github.com/merbanan/rtl_433/issues/3539.

## Not a decoder bug: default FSK pulse detector struggles on this signal

The decoder as merged (PR #3553), `.modulation = FSK_PULSE_MANCHESTER_ZEROBIT`
at 25 us, is correct -- confirmed independently by the device's own
datasheet (Huf Baolong TSSSG4G6B) and by a real maintainer discussion on
the issue. A reporter's real drive test found decoder 365 registered but
producing nothing despite the dash TPMS correctly showing all 6 tire
pressures. An earlier analysis pass here mistakenly "fixed" this by
switching the decoder to `FSK_PULSE_PCM` at 52 us, since that happened to
decode the reporter's 9 posted real `.cu8` captures (g030-g038) -- but per
https://github.com/merbanan/rtl_433/issues/3539#issuecomment-4586440223,
that's a known artifact: naively reading Manchester at double the bit
period reconstructs the same data bits by coincidence of Manchester's
own structure, it is not the real protocol. That "fix" was reverted.

The real fix is demodulation, not decoding: the default FSK pulse
detector (classic/auto) fails on all 9 real captures (RSSI -2 to -11.6 dB),
but `-Y minmax` with tuned levels (`-Y minlevel=-40 -Y level=-18`) decodes
all 9 correctly with the *original, unmodified* Manchester decoder --
valid CRC-8, `id 247e80b6`, ~65 PSI (matching the reporter's stated cold
pressure), and a steadily incrementing counter (9, 10, 11, 14, 15, 16,
17, 19, 20 -- gaps are frames the reporter's own capture missed, not
decoder drops). See the `demod` file in `01/` for the flags this test
fixture applies.

No test fixture existed for this decoder before (the original PR was
apparently never checked against real IQ, which is how this demod
sensitivity went unnoticed).

`01/` holds 2 of the 9 real captures (g030, g038 -- first and last by
counter). `codes_test.txt`/`codes_test.json` cover all 9 as raw on-air
bitstreams (bypassing demodulation entirely via `-y`, so they don't need
the `demod` file's flags).
