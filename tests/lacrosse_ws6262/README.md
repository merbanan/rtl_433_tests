# LaCrosse Technology WS6262 Weather Station, sensor WSTX62TY

See https://github.com/merbanan/rtl_433/pull/3199 for the original decoder
submission (unmerged as of this writing).

`codes_test.txt` contains the 6 payloads embedded in that PR's decoder file
comment, from 2 distinct physical stations (id `0xb61` and id `0x694`). All
6 decode with a valid checksum against the PR's own decoder patch, but
since that PR is unmerged there's no `lacrosse_ws6262.c` in this checkout
to decode them against -- marked `ignore` until it lands.

The frame shares its preamble and checksum with the existing `emax`
decoder's "Rain/Wind station" layouts, and coincidentally ends its filler
byte sequence at the same value (byte 29 == 0x16) as the `Emax-EM3551H`
"without UV/Lux with Wind Gust" layout, causing a false-positive decode by
`emax` before that decoder learned to tell the two apart (see
merbanan/rtl_433#3199 discussion and the accompanying `emax.c` fix).
