# Elsner Solexa 230V

From https://github.com/merbanan/rtl_433/issues/2798. A handset/receiver
pair (open/close/stop/automode/switchdisplaymeasures) plus an outdoor
sensor (wind/temperature/light), reported at 868.2 MHz.

FSK, Manchester coded with a fixed leading zero bit, ~11 us chip width.
Framing (fixed 4-byte ID, CRC-16 poly 0x1021 init 0x68b3) is confirmed
against all 60 messages available across the linked issue's captures.
The 32-byte payload could not be decoded further: repeated transmissions
of the exact same button press produce entirely different payload bytes,
and no byte position correlates with the command across the whole
sample set -- this looks like per-message encryption or whitening, not a
fixed field layout. See the decoder's doc comment in `elsner_solexa.c`
for details. Registered disabled by default (protocol 364) since it
cannot report anything actionable beyond confirming a transmission and
its (fixed) ID.

- 01/ - one representative `.cu8` capture (an "open" button press, 3
  repeats), from the issue's `elsner.zip` attachment. **Requires
  `-Y minmax`** -- the default FSK pulse detector mode recovers nothing
  from this capture, which is also why this directory has an `ignore`
  marker (the regression harness has no way to pass that flag).
- `codes_test.txt`/`codes_test.json` - all 60 known-good messages from
  every capture in `elsner.zip` (open/close/stop/automode/
  switchdisplaymeasures/sensor-report), extracted via
  `-Y minmax -R 364:vv` (see AGENTS.md's "codes_test" convention). Each
  code's CRC-16 validates; annotations record which command/file it came
  from.
