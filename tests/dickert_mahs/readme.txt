# Dickert MAHS433-01 garage door remote control

See https://github.com/merbanan/rtl_433/issues/2983 and
https://github.com/merbanan/rtl_433/pull/3321.

10 tristate DIP switches (`-`/`0`/`+`) plus an 8-symbol factory code, PWM-over-OOK-gap
encoded, no CRC (hence disabled by default, protocol 344 in this build).

Contents:
- `01/g024_433.92M_1000k.cu8` / `.json` / `protocol` - one real capture (dipswitch
  `++0-++--0+`, the exact example device from the issue thread).
- `codes_test.txt` / `codes_test.json` - 12 synthetic codes covering every switch
  position and the all-`-`/all-`0`/all-`+` extremes, taken from the BitBench in the
  issue. 11 of the 12 match the issue author's own hand-typed expectation exactly;
  `400305515` decodes to `0------+--` rather than the issue's typo'd `0---------`
  (verified independently against the decoder logic, byte by byte). Also uses a
  top-level `protocol` file (344) since the decoder is disabled by default.
