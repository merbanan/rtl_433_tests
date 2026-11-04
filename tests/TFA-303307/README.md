# TFA 30.3307.02 wind sensor

From https://github.com/merbanan/rtl_433/issues/2453. Part of TFA's
"WeatherHub" product line. An unusual OOK "Return-to-Zero unary run-length"
coding, see `pulse_slicer_rz_count()` and the decoder's doc comment for the
full protocol (frame sync, CRC-32, wind speed/direction/gust layout),
reverse engineered in the issue down to raw framing, then completed using
the protocol documented by the independent GPLv2 "tfrec" project
(https://github.com/baycom/tfrec/blob/master/whb.cpp), which targets a
different (FSK/PSK) receiver chip for the same sensor family but uses the
same underlying bit-recovery algorithm and documents the full frame/CRC/
field layout.

- 01/ - 3 real captures (2 exact-duplicate repeats dropped), all from the
  same physical sensor (same device ID). CRC-32 valid on all 3. Wind
  direction differs between captures (180 vs 292.5 degrees) matching the
  reporter's own description of rotating the wind vane between test
  captures; speed/gust are 0.0 m/s in all 3, consistent with an indoor,
  stationary test transmission (button press, not real wind).
