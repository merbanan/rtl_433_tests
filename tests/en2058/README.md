EN2058 four probe temperature sensor

See https://github.com/merbanan/rtl_433/pull/3498 (decoder by Steven Walter)
and https://github.com/merbanan/rtl_433_tests/pull/400 (real captures and
ground truth posted by nitrag).

FSK-PCM, 100 us bit width, fixed sync/preamble, 24 bit ID, 4x 16 bit
temperature (offset 900, scale 10, degrees F, disconnected probes read a
fixed sentinel), 8 bit checksum. The checksum formula was reverse engineered
and confirmed against these captures after the decoder's original PR shipped
with an incorrect, disabled checksum.

- device.jpg - photo of the device from PR #400.
- 01/ - 2 of the 6 raw .cu8 captures posted in PR #400 (g004, g021; chosen to
  cover both a single-probe and a four-probe reading).
- codes_test.txt/json - one repeat extracted from each of the 6 available
  captures (including the 2 in 01/), all matching the physical readout
  reported in PR #400 exactly.

Original ground truth from PR #400, for reference:

## Veken BBQ Meat Thermometer EN2053 (listing title; device is 4-probe, EN2058)

- g004_433.92M_250k: probe1=259F probe2=NA probe3=104F probe4=NA
- g007_433.92M_250k: probe1=261F probe2=NA probe3=111F probe4=NA
- g021_433.92M_250k: probe1=259F probe2=87F probe3=112F probe4=173F
- g023_433.92M_250k: probe1=258F probe2=95F probe3=113F probe4=178F
- g020_433.88M_250k: probe1=287F probe2=NA probe3=172F probe4=NA (433.88MHz)
- g014_433.96M_250k: probe1=288F probe2=NA probe3=172F probe4=NA (433.96MHz)
