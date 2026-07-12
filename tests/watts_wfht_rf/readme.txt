Watts WFHT-RF / WFHC-MASTERH&C-RF underfloor heating thermostat (LCD-display
generation)

See https://github.com/merbanan/rtl_433/pull/3561 (decoder by Steven Bontius),
https://github.com/merbanan/rtl_433_tests/pull/502 (these captures, same
author), and the protocol writeup at
https://github.com/StevenBontius/watts-wfht-ha/blob/main/docs/WATTS_WFHT_RF_PROTOCOL.md.

This is a different, newer hardware generation from the existing
watts_thermostat.c decoder (model "Watts-WFHTRF"): OOK Manchester instead of
PWM, a completely different frame layout, and CRC-8 + CRC-16/CMS instead of
an 8-bit sum. The model string here is "Watts-WFHTLCDRF" rather than the
PR's original "Watts-WFHT-RF", to avoid colliding with "Watts-WFHTRF" once
dashes are stripped for the project's model-name convention (both would
otherwise reduce to "WattsWFHTRF") -- see the decoder's own doc-comment.

- 01/ - all 3 real captures from rtl_433_tests#502:
  - pairing_thermostat_433.92M_250k.cu8: thermostat in pairing mode
    (pairing=true, ~2 Hz broadcast rate)
  - turning_thermostat_off_433.92M_250k.cu8: setpoint set to 0.0 C (off)
  - turning_thermostat_on_433.92M_250k.cu8: setpoint set to 17.5/17.6 C,
    showing the documented "A-B-A" burst jitter around a setpoint change
- codes_test.txt/json - one frame extracted from each of the 3 captures above,
  independently verified (both CRC-8 and CRC-16/CMS recomputed in Python
  against the documented algorithms) before adding
