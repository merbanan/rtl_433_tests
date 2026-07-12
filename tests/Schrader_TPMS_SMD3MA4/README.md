# Schrader SMD3MA4 / Nissan-Infiniti-Renault MRXNIS315G3 TPMS

See `01/README.md` for the original Subaru SMD3MA4 protocol writeup and
`02/README.md` for the Nissan/Infiniti/Renault (MRXNIS315G3, aka aftermarket
Redi-Sensor SE10001HP/SE10001HPR) captures.

## The pressure-scaling discrepancy

Both sensor families share the exact same preamble, Manchester timing and
frame layout, and are both decoded by `schrader_SMD3MA4_decode()`. They
differ only in how many bits of the 10-bit pressure field are meaningful,
and its scaling:

- SMD3MA4 (Subaru): all 8 usable bits, PSI * 5 (after the low 2 bits, once
  assumed to be low-order pressure bits, were identified as a checksum --
  see below)
- MRXNIS315G3 (Nissan/Infiniti/Renault/Redi-Sensor): PSI * 4

There is no reliable way to tell which sensor produced a given packet from
the wire data alone -- IDs, preamble and timing all overlap between the two.
The decoder therefore outputs both interpretations: `pressure_PSI` (/5,
SMD3MA4 assumption) and `pressure_NIS_PSI` (/4, MRXNIS315G3 assumption).
Pick whichever matches your vehicle.

Full discussion: https://github.com/merbanan/rtl_433/issues/1734

## Checksum

The 2 bits that early decoder versions treated as low-order pressure bits
are actually a checksum, found by RonNiles: realign the data to an even bit
count (38 bits, padded with the fixed leading 1-bit from the tail of the
preamble), split into 2-bit groups, and add them arithmetically (not XOR)
modulo 4 -- the result is always 1.

## Known device IDs

Collected from the issue thread. Pressure values are as originally reported
using the /5 (SMD3MA4) scaling; multiply by 1.25 for the /4 (NIS315G3)
equivalent.

### Confirmed MRXNIS315G3 (Nissan/Infiniti/Renault/Redi-Sensor)

Confirmed against the serial number printed on the physical sensor body.

| id     | source |
|--------|--------|
| 54A7E0 | robcazzaro, OEM sensor |
| 54A7AD | robcazzaro, OEM sensor |
| 54A7D0 | robcazzaro, OEM sensor |
| 53E22F | robcazzaro, OEM sensor |
| CEDE23 | robcazzaro, aftermarket Redi-Sensor SE10001HP (printed 0CCEDE23), see `02/` |
| 820900 | robcazzaro, aftermarket Redi-Sensor SE10001HP (printed 0C820900) |
| D004E2 | robcazzaro, aftermarket Redi-Sensor SE10001HP (printed 0CD004E2) |
| D6136D | robcazzaro, aftermarket Redi-Sensor SE10001HP (printed 0CD6136D), see `02/` |

### Confirmed SMD3MA4 (Subaru)

Confirmed by consistent 25-33 PSI inflate/deflate cycling typical of a
normally-operating Subaru TPMS, cross-referenced across repeated captures
from the same vehicle.

| id     | source |
|--------|--------|
| 3F0650 | RonNiles, see `01/` (existing rtl_433_tests fixture) |
| 3F0B51 | RonNiles, same vehicle as 3F0650 |
| 3F103C | RonNiles, same vehicle as 3F0650 |
| 3F135B | RonNiles, same vehicle as 3F0650 |
| 3AE33B | RonNiles, second vehicle |
| 3AE92A | RonNiles, second vehicle |
| 3AE948 | RonNiles, second vehicle |
| 3AEDA4 | RonNiles, second vehicle |

### Ambiguous / unconfirmed

Stray sensor IDs seen once in passing (wardriving), with no repeat vehicle
data to cross-validate against. Listed pressure is the /5-scaled reading as
originally reported by RonNiles.

| id     | pressure_PSI (/5) | notes |
|--------|--------------------|-------|
| 788C89 | 39.75 | plausible if overinflated SMD3MA4; too high for a sane NIS315G3 reading |
| 78E7CE | 15.0  | suspiciously low for either type; no repeat transmission to confirm it wasn't corrupt |
| 79F153 | 31.6  | in the overlap zone, could be either type |
| B0CB02 | 27.1  | in the overlap zone, could be either type |

### Vehicle/sensor-type compatibility lists

Two Schrader/Continental catalog-derived vehicle compatibility lists were
posted in the issue thread (which cars use which sensor type):

- MRXNIS315G3: https://github.com/merbanan/rtl_433/files/6640410/Schrader-NIS315G3.txt
- SMD3MA4: https://github.com/merbanan/rtl_433/files/6640411/Schrader-SMD3MA4.txt
