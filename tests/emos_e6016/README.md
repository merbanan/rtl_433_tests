# EMOS E6016 weatherstation with DCF77, EMOS E6018 temperature/humidity sensor

See https://github.com/merbanan/rtl_433/issues/1692.

The E6018 turned out to be decodable by the exact same protocol/frame as
the E6016 (protocol 214) -- it's a simpler variant of the same family
without a wind sensor or DCF77 radio clock receiver. It's distinguished by
byte 4's top 2 bits (post-invert): 0 for E6018, 2 for E6016 (only these
two values have been observed). When 0, wind_avg_m_s/wind_dir_deg/
radio_clock are suppressed since the E6018 always reports 0 wind and a
fake fixed-date clock (2015-01-01, only the time-of-day advances).

`codes_test.txt`/`codes_test.json` contain all 13 codes from the issue:
5 real E6018 readings, plus 3 real E6016 readings (2 different physical
units) and the decoder's own pre-existing doc-comment example, used as
cross-reference to confirm the discriminator. No raw `.cu8` captures were
posted in the issue, only these hex codes (via `rtl_433 -R 214:v`).
