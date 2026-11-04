# Hanwell ML/RL4000-series Radiologger temperature/humidity sensor

See https://github.com/merbanan/rtl_433/issues/2942 -- a long-stalled
thread (over a year with no resolution) where zuckschwerdt and ProfBoc75
made partial progress on framing/timing but never landed on a working
byte layout or checksum. Identified as a Hanwell ML/RL4000-series
Radiologger (likely ML4106/RL4106) using its 12-bit radio mode, with a
byte-reversed layout and an 8-bit additive checksum -- confirmed
independently against this capture: all 4 decoded frames match the
issue's own worked-out reference table for captures #1, #2, #3 and #5
of the "15xID1" 15-packet recording (byte-for-byte, including the raw
temperature/humidity counts).

`01/g001_434.052M_1000k.cs8` is that same "15xID1" capture (renamed to
rtl_433's `.cs8`/`complex16s:` convention). It only decodes with extra
demod-assist flags -- the signal is narrow-deviation FSK and needs help
locking on:

    rtl_433 -r g001_434.052M_1000k.cs8 -R 371 -Y minmax -Y magest -Y filter=100

A `demod` file carries those extra `-Y` flags (alongside the `protocol`
file pointing at 371), so `run_test.py` passes them through and this
fixture runs as a normal regression test.

Of the 15 packets in the original recording, only 5 are complete 40-bit
frames (the rest are truncated mid-transmission, likely due to marginal
signal); only 4 of those 5 land within this specific capture slice, all
matching the reference table exactly. The engineering-unit conversion
(raw counts to actual temperature/humidity) is intentionally not
implemented -- Hanwell calibration is transmitter-specific and lives in
the base station, not the radio protocol.
