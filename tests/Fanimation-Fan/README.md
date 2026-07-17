# Fanimation ceiling fan/light remote control

See https://github.com/merbanan/rtl_433/issues/3033. FCC ID KUJCE10711.

This is a flex decoder, not a compiled-in protocol:
`conf/Fanimation-Fan.conf`.

The reporter (roblandry) and zuckschwerdt worked out the general shape in
the issue (EV1527-style OOK_PWM, dip switch id, 8 bit command byte) but got
stuck on flex.c's 16-values-per-getter / 12-getters limit trying to name
every one of the ~70 command byte meanings (16 fan speeds, 44 brightness
levels, timers, modes...). This decoder reports the raw `id` (dip switch)
and `cmd` (command byte) instead of trying to enumerate every meaning as a
flex value mapping -- see the comment block in the `.conf` file for the
full table of what each `cmd` value means.

`01` (`g001`, Fan On/Off) is one of the 14 real captures attached to the
issue (`fanimation_fan.zip`), all from the same remote (dip switch `00011`,
i.e. `id: 3`). Independently re-derived the bit offsets from the full set of
14 captures (the `12b 5b 8b` layout in the issue's own draft `.conf` was off
by 3 bits -- verified the correct split is preamble(12) + dip(5) + cmd(8)
with the last 3 bits of the printed code being print-padding, not signal)
and confirmed every command byte value against the reporter's own
decimal-annotated list in the issue.

`codes_test.txt`/`codes_test.json` cover all 14 button/dial codes from the
issue (the other 13 captures aren't kept as separate raw IQ fixtures, only
as these already-verified codes) plus 3 dip-switch calibration codes (all
off / all on) taken directly from the issue's worked example, run through
`rtl_433 -y "<code>" -c conf/Fanimation-Fan.conf`.

No means to test sending commands back was investigated here -- that's a
separate feature request (bidirectional/TX support) outside rtl_433's scope
as a receiver.
