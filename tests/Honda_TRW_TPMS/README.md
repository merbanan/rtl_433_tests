# Honda (TRW PPA-GF33) TPMS

FCC-ID GQ4-36T, part number 42753-SNA-A830-M1. Seen on a 2010 Honda
Insight, likely shared with other Honda models 2009-2016. See
https://github.com/merbanan/rtl_433/issues/3447.

`g001_315M_250k.cu8` is the reporter's own capture (sensor unmounted,
0 PSI). Decoded ID (`8d3f6d67`) matches the value printed on the
physical sensor and read independently by a commercial TPMS tool.

Pressure formula (`raw * 0.2` PSI) and temperature (`raw - 50` C) were
derived from a 7-point pressure sweep the reporter ran with a known-good
TPMS tool for ground truth; 6 of 7 points fit to within 0.1 PSI. One
very-low-pressure point (0.7 PSI actual) didn't fit the linear model
(computed ~14.6 PSI) -- cause not confirmed, so treat pressure readings
below ~10 PSI with some caution.

The `flags` byte (always `0xe1`, parked/stationary) is exposed raw;
no capture with the vehicle in motion has been reported yet, so its
bits aren't decoded.

`codes_test.txt`/`codes_test.json` cover all codes posted in the issue:
the 3 raw captures from the issue body (redundant with the `.cu8` above,
all 0 PSI) and the 7-point pressure sweep. Only the already-decoded 8
bytes were posted for the pressure sweep, not a raw capture, so those 7
are reconstructed by re-encoding those bytes (marker + IEEE 802.3
Manchester) rather than hand-transcribed -- verified this round-trips
exactly against the real capture's own raw bits (`codes_test.txt` has
the details). One of the 10 is the low-pressure outlier mentioned above
(0.7 PSI actual, decodes to 14.6 PSI); it's kept in as a known,
documented mismatch, not silently dropped.
