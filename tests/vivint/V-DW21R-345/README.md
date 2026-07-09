# Vivint Door/Window Sensor, V-DW21R-345

See https://github.com/merbanan/rtl_433/issues/1504 for the decoder request
and protocol discussion (a large thread, revived in Jan 2026 with a much
deeper analysis than the original 2020 discussion).

Captures g001/g002 are a closed-state transmission, g003/g004 are the
matching open-state transmission from the same sensor (per the original
reporter's ground truth, not derived by the decoder — see below).

`test_codes.txt` contains 88 additional payloads (as `{96}<hex>` bitbuffer
codes), all transcribed from the issue thread, covering battery-insert,
open, and closed events across multiple sensors. All 88 decode
successfully with a valid CRC when fed to the decoder without the
trailing `#` comment text (a literal `/` in some comments is otherwise
misparsed by `bitbuffer_parse` as a row separator).

Two things confirmed by the 2026 follow-up discussion (with a ~14000
message capture and multiple independent sensors) that are not obvious
from the small 2020 sample alone:

- The 32 bit id decodes to the sensor's printed TXID by splitting it into
  a 12 bit and a 20 bit decimal number, e.g. id `0x0137beda` -> `19`,
  `507610` -> `0019-0507610`, matching the label `0019-050-7610` on the
  sensor used for g001-g004. Same trick as identified for Honeywell/2GIG
  in issue #1261.
- The byte after the counter (called `flags` here) does **not** reliably
  indicate open/closed: an early hypothesis (its top bit) matched the
  handful of samples in the original 2020 report by coincidence, but
  fails on ~35% of a large labeled capture from the 2026 follow-up. Nobody
  in the thread found a working formula, so the decoder does not expose a
  door state — only the raw fields that are actually understood.
