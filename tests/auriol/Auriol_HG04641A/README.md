# Auriol HG04641A temperature station

From https://github.com/merbanan/rtl_433/issues/2014. Lidl-branded "temperature
station" (IAN 307350) with a DCF77 radio-clock receiver in the head unit
(unrelated to the 433 MHz sensor protocol below).

OOK, PPM (distance coding): fixed ~510 us pulse, ~980 us gap for a 0-bit,
~1976 us gap for a 1-bit. Each transmission repeats the same 36-bit
message up to 4 times, with the last repeat sometimes truncated by one
bit -- confirmed directly from the issue's `-A` analyzer dumps (still
live, no raw `.cu8` was ever attached).

Data layout (nibbles): `II II F TTT C`

- `I`: 16 bit id. Stayed constant across every test in the issue,
  including a battery pull -- not confirmed to be a rolling code.
- `F`: 4 bit flags. Bit 3 (`0x8`) is battery_low, confirmed by an
  old-vs-fresh-battery comparison. Bit 0 is always set and bits 1-2
  always clear in every capture here; whether those are unused,
  reserved, or channel bits was never tested (no channel switch tried).
- `T`: 12 bit temperature, 2's complement, scale 0.1 C -- confirmed
  against a freezer test (`-14.1 C`) and multiple above-zero readings.
- `C`: 4 bit checksum -- sum of the preceding 8 nibbles, mod 16.

The checksum is genuinely only 4 bits (verified: it's not a truncated
display of something wider). Combined with this device's fairly generic
OOK/PPM timing, that's too weak to reject noise reliably on its own --
enabling `auriol_hg04641a` against the full rtl_433_tests corpus produced
two dozen false positives on unrelated weather-sensor protocols before a
flags-nibble check and a plausible temperature range were added in the
decoder itself (both satisfied by every real capture below).

## One correction to the issue thread

The original post labeled `12 f4 10 e2 70` as `-22.6 C`, but that was
posted before the freezer test established the actual 2's-complement
encoding -- decoding it with the confirmed formula gives `+22.6 C`
instead. Treated the freezer test (a deliberate, controlled
verification) as authoritative over the early, pre-formula label.

## Captures

No `.cu8` IQ file exists for this device anywhere in the issue, only
already-demodulated text dumps -- hence `codes_test.txt`/`codes_test.json`
only, no numbered capture subdirectory.
