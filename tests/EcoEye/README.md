# Eco-Eye solar PV / grid current monitor

https://www.eco-eye.com/product-monitor-solar-smartpv

Transmitter unit with two current clamps (grid usage and PV/solar
generation) sending to a paired display every 4 seconds. No id field --
each transmitter/display pair is expected to be alone on its channel.

Captured and reverse-engineered by @teb1880 and @zuckschwerdt in
https://github.com/merbanan/rtl_433/issues/1757 (solved in 2021, decoder
added in 2026).

- `01/` - two of the reporter's original `.cu8` captures (`g033` and
  `g048`, from a continuous run at 4-second intervals), cross-validated
  against the transmitter's own serial console log -- every decode
  matches the console digit for digit.
- `codes_test.txt`/`codes_test.json` - all 23 known-good messages: all 16
  captures from that same run (raw demodulated codes, as originally
  posted via BitBench by @zuckschwerdt; only two are kept as `.cu8` in
  `01/`) plus 7 additional real readings posted later in the thread
  specifically to confirm the checksum works for `used` > 255, a range
  the 16 captures never reach.

## Protocol

FSK_PCM, 200 us bit width. Center frequency drifts with temperature and
sits somewhat below 433.92 MHz; the reporter had to tune off-center
(432.5-433.55 MHz) to get a clean capture.

After the `aa2dd4` sync word:

    PPPPPPPPPPPPPPPP UUUUUUUUUUUUUUUU CCCCCCCC

- P: 16 bit PV/solar generation current, centi-amps (0.01 A/count)
- U: 16 bit grid current used, centi-amps (0.01 A/count)
- C: 8 bit checksum: `b0+b1+b2+b3 == b4` (mod 256)

Neither field's engineering unit was ever confirmed in the issue thread.
Centi-amps is assumed: it is the only scale that keeps a later reading of
used=2348 (posted when the reporter deliberately turned on more
appliances) within the range of a typical CT clamp (23.48 A), while
deci-amps or whole amps would put it far beyond what the clamp/circuit
could plausibly read.

A large `reset_limit` (8100 us) is required: the protocol has no clock
recovery beyond the bit period, so a long run of zero bits (e.g.
pv=0, used=0, check=0, i.e. 40 zero bits) can't be reliably counted
otherwise.

Full archive of all 16 original `.cu8` captures (source for `01/`):
https://www.dropbox.com/s/kt7z1cdtqb2imdy/ecoeye%20decoding.zip?dl=0
