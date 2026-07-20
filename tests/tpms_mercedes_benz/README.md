# Mercedes Benz Sprinter 4500 TPMS sensor

See https://github.com/merbanan/rtl_433/issues/3539.

## Bug found and fixed: wrong modulation type

The decoder as merged (PR #3553) declared `.modulation =
FSK_PULSE_MANCHESTER_ZEROBIT` at 25 us, per the file's own doc comment
("Signal is FSK MC and pulse width 25us"). This never decoded a single
real capture -- confirmed when the reporter did a real drive test with
the dash TPMS correctly showing all 6 tire pressures, yet decoder 365
produced nothing. Re-analyzing 9 fresh real `.cu8` captures the
reporter posted (stationary front driver's tire, released air,
g030-g038) with `-A` and a flex decoder showed the real signal is
plain `FSK_PULSE_PCM` at 52 us -- matching the *reporter's own*
original flex command from the very first issue comment
(`m=FSK_PCM,s=52,l=52,r=53248`), which the merged decoder's modulation
fields never actually matched. Fixing `.modulation`/`.short_width`/
`.long_width`/`.reset_limit` to PCM/52/52/53248 makes all 9 real
captures decode cleanly with valid CRC-8, `id 247e80b6`, ~65 PSI
(matching the reporter's stated cold pressure) and a steadily
incrementing counter (9, 10, 11, 14, 15, 16, 17, 19, 20 -- gaps are
frames the reporter's own capture missed, not decoder drops).

No test fixture existed for this decoder before (the original PR was
apparently never checked against real IQ, which is how the wrong
modulation type went unnoticed).

`01/` holds 2 of the 9 real captures (g030, g038 -- first and last by
counter). `codes_test.txt`/`codes_test.json` cover all 9 as raw on-air
bitstreams extracted via the corrected flex decoder.
