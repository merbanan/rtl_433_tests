# Auriol 4-LD6654 temperature/humidity/rain sensor

Outdoor sensor of the Lidl Auriol "RC weather station with rain gauge",
IAN 452207, made by digi-tech gmbh. Reports temperature, humidity and a
tipping bucket rain counter. No public protocol documentation exists.

433.92 MHz, OOK PPM: ~500 us pulse, ~960 us gap for a 0-bit, ~1936 us gap
for a 1-bit, ~3892 us sync gap between repeats. 52 bit frame, repeated 7
times per transmission, every ~57 seconds.

Data layout:

    b1       81       05       f2       d0       09       e
    IIIIIIII B?CCTTTT TTTTTTTT FFFFHHHH HHHHRRRR RRRRRRRR RRRR

- `I`: 8 bit id, random per battery insertion
- `B`: 1 bit battery, 1=OK. Assumed from the 4-LD5661 family; the low
  state was never observed, all captures are on a fresh battery.
- `?`: 1 bit flag, always 0 here
- `C`: 2 bit channel, always 0 on this unit (no channel switch on it)
- `T`: 12 bit temperature, 2's complement, scale 0.1 C. Confirmed below
  zero: `g032` is -0.1 C (`0xfff`), which rules out sign-magnitude
  (that would be `0x801`). `g045` is -5.1 C.
- `F`: 4 bit constant `0xf`, separator
- `H`: 8 bit humidity in percent
- `R`: 16 bit tipping bucket counter

No checksum, no CRC, no sync word, so the decoder is disabled by default
(see the `protocol` file) and relies on the constant `0xf` nibble, the
always-zero flag bit, a repeated-row check and range limits.

## Samples

Captured from a single unit over ~50 minutes, covering a rain test and a
freezer run.

| file | temp C | humidity | rain tips | note |
|------|--------|----------|-----------|------|
| g001 | 25.8 | 45 | 158 | ambient baseline |
| g009 | 24.6 | 47 | 173 | rain test, the +10 tip calibration run |
| g032 | -0.1 | 31 | 176 | first frame below zero, `0xfff` |
| g045 | -5.1 | 31 | 177 | coldest |
| g060 | 7.3 | 54 | 177 | warming back up |

The remaining 47 frames of the same session are in `codes_test.txt` as
bitbuffer codes rather than further `.cu8` files, to keep the repo small.
They cover the rest of the rain test (+1, +4, +3 tips) and the full
temperature sweep. Each code is written three times on its line because
the decoder requires a repeated row in place of a checksum, so a single
row is deliberately rejected.

## Rain calibration

Tipping the bucket by hand advanced the counter by exactly one per tip.
Read against the display unit:

    counter 158 -> 0.0 mm, 163 -> 5.8 mm, 173 -> 17.4 mm, 176 -> 20.9 mm

which is exactly `(counter - 158) * 1.16`. The 20.9 mm point also rules
out a slightly smaller constant, since 1.155 would have shown 20.8 mm.

The sensor's counter is free running and is not cleared by the display
unit's rain reset, which only re-baselines the display: the display read
0.0 mm while the counter was already at 158. Reported `rain_mm` is
therefore a lifetime total and does not match the display.

## Relation to Auriol 4-LD5661

Shares the modulation, frame length and the first 28 bits with the
4-LD5661/4-LD5972/4-LD6313 family, but splits the trailing 24 bits into
8 bit humidity + 16 bit rain instead of a 24 bit rain counter.
