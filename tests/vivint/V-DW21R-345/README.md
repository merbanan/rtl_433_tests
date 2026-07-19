# Vivint Door/Window Sensor, V-DW21R-345

See https://github.com/merbanan/rtl_433/issues/1504 for the decoder request
and protocol discussion (a large thread, revived in Jan 2026 with a much
deeper analysis than the original 2020 discussion).

Captures g001/g002 are a closed-state transmission, g003/g004 are the
matching open-state transmission from the same sensor (per the original
reporter's ground truth, not derived by the decoder — see below).

`01/` runs with no seed configured: `state`/`contact_open` are absent and
`data` carries the raw payload instead. `02/` reuses g001 (closed) and
g003 (open) with `protocol` supplying `342:0019-0507610=05c9` (the real
seed for this sensor's TXID), showing the decrypted `state`/`contact_open`
fields.

`codes_test.txt` contains 88 additional payloads (as `{96}<hex>` bitbuffer
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
- The byte after the counter (called `flags` here) does **not** directly
  indicate open/closed: an early hypothesis (its top bit) matched the
  handful of samples in the original 2020 report by coincidence, but
  failed on ~35% of a large labeled capture from the 2026 follow-up.

## Update: the door state is recoverable, given a per-device seed

`flags` is XORed with a keystream from a Rabbit stream cipher core (RFC
4503) keyed by a 16 bit per-device seed (burned in at manufacturing, not
transmitted over the air) and the transmission counter. Bit 7 of the
decrypted byte is the door contact. The seed can't be discovered by the
decoder itself; it must be recovered externally (e.g. via
https://github.com/n8henrie/vivint-decode's `crack` subcommand,
brute-forcing it from a handful of frames at known low counters).

Known seeds for the two sensors in this issue thread:

| TXID           | seed     |
|----------------|----------|
| 0019-0507610   | 0x05c9   |
| 0019-0507743   | 0xdda9   |

Once known, supply it at registration time to decrypt `flags`:

    rtl_433 -R 342:0019-0507610=05c9,0019-0507743=dda9

Verified against all 15 open/closed-labeled frames in `codes_test.txt`
(both sensors, the seeds above) — every one matches its label, including
the one the original annotator marked uncertain (`Open?`).
