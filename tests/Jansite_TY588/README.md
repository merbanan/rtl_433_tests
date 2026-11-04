# Jansite TPMS TY588-EU2

From https://github.com/merbanan/rtl_433/issues/2320. A different,
Manchester-coded FSK protocol from the older Jansite Solar TPMS already
supported by `tpms_jansite_solar.c` (confirmed a genuinely different wire
format: different preamble, no CRC, not just a decode bug).

## The encoding

174 bit packet: 44 raw preamble bits (`99aa5a6a9aa`) then 128 Manchester
bits decoding to 8 bytes B0..B7.

- B7 repeats B0 (used as the "mic" here, since there is no real CRC)
- B3 = (B0 - 0x1e) mod 256, B4 = (0x4e - B0) mod 256 (structural, always
  true)
- (B0 & 0x0f) == (B1 & 0x0f) (structural, ditto)
- temperature_C = (B2 + B5) mod 256 - 139
- pressure_kPa = ((B5 + B6) mod 256 - 90) * 2.5

Sensor ID and battery status are not decoded -- resolving which bits are a
fixed per-sensor ID needs samples from a second physical sensor, which was
never posted to the issue.

## codes_test.txt/json

15 real messages from one real sensor, covering a slow 1.6-2.8 bar
pressure ramp (posted to the issue as text, not as raw `.cu8` -- despite
several raw captures being posted earlier in the same issue by a
different reporter using exploratory demod settings, none of those were
found to decode against the final, confirmed protocol above, so they are
not included here).

Verified: temperature matches the reported value exactly on all 15;
pressure matches within one 2.5 kPa sensor step on all 15 (the sensor's
own display rounds/truncates more coarsely than its native resolution),
e.g. reported "1.7 bar" decodes to 175.0 kPa (1.750 bar) exactly at that
resolution.
