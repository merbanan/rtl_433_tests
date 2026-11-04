# Elsner Solexa 230V

From https://github.com/merbanan/rtl_433/issues/2798. A handset/receiver
pair (open/close/stop/automode/switchdisplaymeasures) plus an outdoor
sensor (wind/temperature/light), reported at 868.2 MHz.

FSK, Manchester coded with a fixed leading zero bit, ~11 us chip width.
Framing and CRC-16 (poly 0x1021, init 0x68b3, over the on-air bytes) are
confirmed against all 98 CRC-valid messages available across the linked
issue's captures and later BitBench comments.

The on-air payload initially looks encrypted -- two presses of the same
button ~100 ms apart differ across the whole payload -- but it is actually
whitened by a self-synchronizing scrambler, G(x) = x^7 + x^5 + 1
(`plain[n] = onair[n] ^ onair[n-5] ^ onair[n-7]`), reverse engineered from
these messages. After descrambling every frame shares the constant 4 byte
sync/id marker 0xc945a400 (reported as `id`).

The raw on-air payload bytes p0..p10 are an arithmetic expansion of a single
rolling state p0: with `spread_k(x) = ((x<<k)&0xff) | (x.b0 ? 2^k-1 : 0)`,
all 98 telegrams satisfy `p3 = spread_3(p0)+0x48`, `p4 = spread_4(p0)+0xd0`,
`p5 = spread_5(p0)+0xa0`, and p1 carries a transmission sequence counter
`= (p1 - spread_1(p0)) & 0xff`. The decoder validates those p3/p4/p5
identities and reports the rolling state p0 (`rolling`) and the `counter`.

The button (open/close/stop/automode) is not in p0..p10 or in any fixed
byte position, but it is recoverable: at a relocated two-byte slot (chosen
by a one-bit selector), reconstructing the rolling-state bytes that would
be expected there and subtracting them from the observed bytes collapses
all 60 labeled messages to exactly seven values, one per button/role
(`command`; see `elsner_solexa.c` for the full derivation). This is
confirmed on one handset/receiver pair only; protocol 364, enabled by
default, gated on the on-air CRC-16.

- 01/ - one representative `.cu8` capture (an "open" button press, 3
  repeats), from the issue's `elsner.zip` attachment. **Requires
  `-Y minmax`** -- the default FSK pulse detector mode recovers nothing
  from this capture, so a `demod` file supplies that flag to
  `run_test.py`.
- `codes_test.txt`/`codes_test.json` - 98 known-good messages: 60 labeled
  ones from every capture in `elsner.zip` (open/close/stop/automode/
  switchdisplaymeasures/sensor-report), extracted via `-Y minmax -R 364:vv`
  (see AGENTS.md's "codes_test" convention), plus 38 additional CRC-valid,
  unlabeled messages from a second population in a later issue BitBench
  comment (for which the decoder does not report `command`, see
  `elsner_solexa.c`). Each code's CRC-16 and p0..p10 model validate
  (`rolling`/`counter` present); annotations record which command/file the
  labeled ones came from.
