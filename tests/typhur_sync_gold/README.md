# Typhur Sync Gold meat thermometer probe

See https://github.com/merbanan/rtl_433/issues/3138. Reverse engineered
by @hakong and @kevin-david, with guidance from @zuckschwerdt, on an
unmerged fork (https://github.com/hakong/rtl_433/tree/feat-typhur) --
this decoder is a from-scratch port re-verified against the fork's own
claims rather than a straight copy.

`01/` (probe id `6402304`) and `02/` (probe id `2211328`) are one real
capture each; `codes_test.txt`/`codes_test.json` cover all 19 real
captures across both probes found in the issue's attached zip (out of
34 total files -- the rest are either a different sender at 914.6 MHz
or unrelated interference, not this device).

Everything here was independently re-derived rather than trusted from
the fork: the sync word (`0x5754`) and payload location were found by
raw bit search against the .cs16 captures, not copied from the fork's
code. CRC-16 (poly 0x8005, init 0x0000) is valid on all 19 real frames.
The field layout and scaling (T1-T5 centi-C, ambient deci-C, battery
centi-V) were confirmed physically sane: temperatures cluster tightly
per probe and match the issue reporter's own noted ranges (~140-165 F
probe, ~210-230 F ambient), battery voltage is stable per probe, and
the counter increments monotonically per probe ID across the capture
sequence.
