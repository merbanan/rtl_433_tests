# Oregon Scientific WMR500 weather station

From https://github.com/merbanan/rtl_433/issues/2407. FSK PCM, ~26 us bit
width, inverted levels. Two message kinds share a 14 byte header; only the
"long" (LEN=25) kind is decoded here (temperature + humidity); the "short"
(LEN=14) kind's extra payload (suspected wind data) is not decoded.

Both message kinds' CRC-16 (poly 0x8005, differing fixed init per kind) are
confirmed against real messages from the issue.

Humidity is confirmed exactly against the real reference readings posted in
the issue (start and end of a slow measurement session): `59%` and `49%`,
matched exactly (not approximately) by `208 - b[16]`.

Temperature is *not* independently confirmed the same way -- only those same
2 reference points (7.1 C / 9.9 C) are available, the bare minimum to fit a
2 parameter linear model with no slack to check it against a third point.
`(b[14] - 169) * 0.7` fits both ends within 0.1-0.2 C (plausible display
rounding), but the scale isn't a clean constant, so treat this field as a
rough estimate. See the decoder's doc comment for the full derivation.

- 01/ - one real capture (from a *different*, undated real session posted
  earlier in the same issue than the reference session above, so its
  humidity/temperature aren't independently checkable against a known
  display reading -- but its CRC is valid and its values are physically
  plausible). **Needs `-Y minmax`** for the classic pulse detector to lock
  onto this FSK signal at all; a `demod` file supplies that flag to
  `bin/run_test.py` (same situation as `../oil_watchman_sonic_advanced/03/`).
- codes_test.txt/json - 7 real messages from the reference session
  mentioned above, spread from its start (7.1 C/59%) to its end (9.9 C/49%),
  confirming the humidity formula and testing the temperature formula's
  plausible range. The last message's `id` differs from the rest by one low
  bit; cause not confirmed (see the decoder's doc comment).
