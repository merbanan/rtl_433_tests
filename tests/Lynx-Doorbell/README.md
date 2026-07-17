# GN Resound / AB Transistor Lynx Door Transmitter (wireless doorbell)

See https://github.com/merbanan/rtl_433/issues/3042. FCC/product manual:
https://cdn.abicart.com/shop/ws15/43915/art55/28693455-c3a9ad-Lynx_Door_Transmitter_Manual_En_De_Fr_It_Ne_No_Sv_2014-06.pdf

This is a flex decoder, not a compiled-in protocol: `conf/Lynx-Doorbell.conf`.
Worked out by @zuckschwerdt and @klohner in the issue thread; the maintainer
asked for it to be stored as a file so the issue could close.

The reporter's own capture repo has real IQ for all 16 possible 4-bit button
codes (0-9, A-F):
https://github.com/kimballen/rtl_433-Recorded-Signals/tree/main/GN%20Resound%20-%20AB%20Transistor%20Lynx%20Doorbell%20(433MHz)

Verified the decoder against every file in all 16 of the reporter's
directories (not just one sample each). 14 of 16 directories decode to
exactly one consistent `(id, button)` pair matching the directory's own
label. Two apparent mismatches, both explained by artifacts in the raw
data rather than a decoder bug:

- `Code 0`: every file also contains a second, spurious decode
  `id=36, button=9` alongside the expected `id=26, button=0` -- consistent
  with a second nearby Lynx transmitter being active during that recording
  session, not a decoding error on the reporter's own remote.
- `Code C`: the first two files (by sequence number) decode as `button=B`;
  the remaining 12 decode as `button=C`. Reads as two leftover captures
  from a previous "Code B" session that ended up filed in the wrong
  folder -- the overwhelming majority, and every file with a higher
  sequence number, agrees with the folder label.

The `match={24}24b659` value (a static product-wide code per the manual,
not a per-remote ID) was confirmed against two independent physical
remotes: the reporter's (this issue) and @klohner's own (used to derive
the original decoder). A deliberately wrong match value decodes nothing,
confirming it's actually enforced rather than a no-op.

Only one real capture (`01/`, button "1") is kept as a fixture; the other
15 button codes were all independently verified above but aren't each
worth a committed multi-hundred-KB `.cu8` file.
