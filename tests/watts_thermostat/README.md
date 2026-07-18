# Watts WFHT-RF Thermostat

Underfloor heating system with wireless thermostats, each with a wheel for
setting temperature and a thermistor for sensing the current temperature.
See https://github.com/merbanan/rtl_433/issues/2230.

Modulation is PWM with a long (~6.2ms) sync gap, then a fixed 8-bit preamble
(`0x5a`), 16-bit reflected ID, 4-bit reflected flags, 9-bit reflected
temperature, 9-bit reflected setpoint, 8-bit checksum.

These fixtures come from https://github.com/merbanan/rtl_433_tests/pull/458
(never merged), by Ådne Hovda, the decoder's original author. `01/` holds
2 of the original 6 real captures as raw `.cu8` (different IDs, pairing
states, and setpoints); `codes_test.txt`/`codes_test.json` cover the
remaining 4 as demodulated codes. `pulseview.png`, `221439.png`,
`252063.png`, `manual-wfht_rf_basic.pdf`, and `MASTER-RAIL.NY.PDF` are the
PR's original pulse capture screenshot, board photos, and product manuals.

All 6 frames were re-verified against the current decoder after refactoring
it to check the preamble at a fixed bit offset (position 0, right after the
sync gap) instead of searching for it, and to reject multi-row buffers
up front instead of looping over rows -- both are no-op changes in
behavior, confirmed identical output before and after against every frame
here.
