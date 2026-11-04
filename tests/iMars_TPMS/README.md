# iMars T240 TPMS

From https://github.com/merbanan/rtl_433/issues/1820: flambert860's IMars T240
TPMS (SP372 sensor IC, atA5754 receiver), sold as a 4-sensor Banggood kit.

OOK, Manchester encoded, ~50 us half-bit time. The thread spent years
suspecting XOR/stream-cipher encryption -- the payload looked like noise
with only a few structural invariants surviving (tail byte repeats the
first byte, first two bytes share a low nibble). merbanan's 2026-04-13
comment guessed this was the same encoding family as `tpms_jansite_solar`'s
"v2"/"v3" variants, but that draft used the wrong modulation type
(`FSK_PULSE_PCM`, copy-pasted from the unrelated v1 device) and unverified
checksum/scale constants (`0x30`/`0x9a`) that don't match any real capture
in the issue.

## The actual encoding

Manchester-decoded, 8 bytes B0..B7:

- B7 repeats B0 (tail integrity check)
- (B0 & 0x0f) == (B1 & 0x0f)
- B3 and B4 are each an affine function of B0 (B3 = B0 - k1, B4 = k2 - B0),
  so (B3 + B4) mod 256 == (k2 - k1) mod 256 is a fixed checksum

**Two physical sensor units are confirmed** in the issue's captures, each
with its own (k1, k2) and thus its own checksum constant:

- Unit A -- checksum `0x41` -- `samples2.zip` (comment #4), 8 real packets
  across its 22 `.cu8` files: `g004`, `g006`, `g009`, `g011`, `g013`, `g016`,
  `g018`, `g020`, `g022` (the rest of the 22 are noise/no signal). See `01/`.
  Cross-checked byte-for-byte against the community's own manual BitBench
  decode in
  https://github.com/merbanan/rtl_433/issues/1820#issuecomment-932900872
  (`7363 4146 fb0a 8b73`, matching `g011`/`g013`/`g018`/`g020`/`g022`).
- Unit B -- checksum `0x3c` -- `sensor-a.txt` (comment attachment, "around
  80 valid data packages" from one sensor), 37 unique codes after dedup.
  See `codes_test.txt`/`codes_test.json`.

Only these two constants are known; a third unit would need its own
constant derived and added to `src/devices/tpms_imars_t240.c`.

`samples.zip` (comment #2, taken before @zuckschwerdt's antenna-distance
fix in comment #3) and `samples.sensor.1.n.2.raising.with.ask.txt` (the
issue body's earliest capture, also pre-fix) are clipped/overloaded/noisy
and don't decode -- expected, per the issue's own narrative; only 1 of 6
readings in the latter even passes the structural sanity checks, and it
matches neither unit's checksum.

## Unresolved: no temperature/pressure mapping

Nothing in the issue thread pairs a raw capture with a numeric ground-truth
reading (the two attached screenshots show the demod tool's raw bit view,
not the sensor's display). Bytes B2/B5/B6 vary between real captures
consistent with carrying temperature/pressure, but the scale and offset
can't be derived without a reading to calibrate against. The decoder
currently outputs the raw 7-byte `code` only.

## Known cross-decoder collision

`g011`/`g013`/`g018`/`g020`/`g022`'s signal also spuriously decodes as
`EezTire-E618` (pre-existing, not introduced by this decoder -- reproduces
with `tpms_imars_t240` disabled). The `EezTire-E618` output
(`temperature_C: 195.000`) is implausible for a TPMS and is the false one;
not fixed here since it's `tpms_eezrv.c`'s own checksum being too weak to
reject this signal, out of scope for this device.

## Captures in `01/`

| File | code |
|------|------|
| `g004_433.92M_1000k.cu8` | `15159fe859acc8` |
| `g011_433.92M_1000k.cu8` | `73634146fb0a8b` (same as `g013`/`g018`/`g020`/`g022`) |
| `g016_433.92M_1000k.cu8` | `7373431d1ff68b` |
