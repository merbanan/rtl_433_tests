# Oria WA150KM freezer and fridge thermometer

See https://github.com/merbanan/rtl_433/issues/3136. The decoder
(`src/devices/oria_wa150km.c`) was already merged via PR #3143 before
this fixture existed; these captures are additional real-world data
from two later attachments in the same issue thread, not previously
covered by any test fixture.

`01/` and `02/` are one real capture each (`WA144_Samples.zip` from
@janiwe and `g003_433.92M_250k.zip` from @AJolly, respectively).
`codes_test.txt`/`codes_test.json` cover all 26 distinct decoded
readings found across the 71 real captures in both zips (many captures
decode to the same reading -- same device, same temperature, sent
repeatedly).

## Checksum

@AJolly reported the shipped decoder occasionally produces wildly wrong
temperature readings. @ProfBoc75's claimed 16-bit XOR checksum (last
byte `0x65` excluded) was checked against all 39 unique real frames
here and does not hold under any contiguous-range/byte-order/self-
validating interpretation -- not implemented.

The decoder now validates an Oregon Scientific v3 style nibble
checksum instead (see `src/devices/oria_wa150km.c`'s doc comment):
computed on the pre-`reflect_bytes()` Manchester-decoded bytes, each
of nibbles 7-23 individually 4-bit-reflected, sum of the first 15 (mod
256) compared against the last two combined into a byte. Verified
against all 39 real frames (100% match) and confirmed discriminating:
every single-bit corruption within the checked nibble range breaks the
match, while corruption outside it (preamble, trailing constant byte)
does not. All fixtures here include `"mic" : "CHECKSUM"`.
