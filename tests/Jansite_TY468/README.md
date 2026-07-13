# Jansite TPMS TY-468-eu2 / KKMOON TPMS

From https://github.com/merbanan/rtl_433/issues/2025. Same SP372-chip-family
OOK/Manchester encoding as the iMars T240 in
https://github.com/merbanan/rtl_433/issues/1820 (confirmed the same by
@zuckschwerdt in comment #34) -- and unlike #1820, this issue has real
ground-truth PSI/C readings paired with raw codes, which is what let this
decoder actually be written and verified rather than left as a guess.

## The encoding

Manchester-decoded, 8 bytes B0..B7, same structure as `tpms_imars_t240.c`:

- B7 repeats B0, (B0 & 0x0f) == (B1 & 0x0f)
- B3 = B0 - k1, B4 = k2 - B0, so (B3 + B4) mod 256 is a fixed per-unit
  checksum
- temperature_C = temp_offset - ((B2 + B5) mod 256)
- pressure_kPa = (pressure_offset - ((B5 + B6) mod 256)) * 2.5

Two physical sensor units are confirmed, both cross-checked against real
device-display readings posted in the issue:

- checksum `0xfb` (comment #5, sp372's KKMOON sensor): temp_offset 224,
  pressure_offset 273. 9 of 10 non-"DETACHED" ground-truth readings match
  the temperature formula exactly; the "DETACHED SENSOR"/"0PSI" readings
  (raw pressure byte-sum 18, wildly off the otherwise-linear trend) are
  a sentinel value for "no reading", not a literal pressure encoding.
- checksum `0x64` (comment #32, the "RL sensor"): temp_offset 153,
  pressure_offset 201. All 3 distinct temperatures match exactly across
  16 readings; pressure matches the ground-truth PSI within about
  0.5 PSI (manual analog-gauge reading precision) -- see `codes_test.txt`.

The `2.5` kPa/unit pressure scale matches both units here as well as
`tpms_jansite_solar`'s v2/v3 and `tpms_imars_t240`'s own (still
unconfirmed) guess -- likely a hardware-fixed ADC scale shared across
this whole chip family, with the checksum and the temperature/pressure
zero-offsets all individually calibrated per physical sensor unit.

Only these two units are known; a third would need its own checksum and
offsets derived similarly and added to `src/devices/tpms_jansite_ty468.c`.

No real `.cu8` IQ captures exist in the issue for either unit, only
already-demodulated text dumps -- hence `codes_test.txt`/`codes_test.json`
only, no numbered capture subdirectory.
