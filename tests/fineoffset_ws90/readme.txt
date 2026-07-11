Fine Offset Electronics WS90 weather station

See https://github.com/merbanan/rtl_433/issues/3599 and
https://github.com/merbanan/rtl_433/issues/3600.

Both issues were filed against different (mis-identified) devices -- "Ecowitt
WH40BH rain gauge" and "Ecowitt WH57 lightning sensor" respectively -- but the
attached captures turned out to be the exact same Fine Offset WS90 weather
station (id 77656) already supported by the existing fineoffset_ws90 decoder
(protocol 244). The reporter's own -R 190/113 filters excluded protocol 244,
so the WS90 packets were only ever seen "recognized but rejected" by the
unrelated WH31L/WH31E decoders that happen to share the same aa 2d d4 sync
word.

Contents:
- 01/g001_915M_1000k.cu8 / .json - from issue #3600's re-recorded sample.
- 02/g001_915M_1000k.cu8 / .json - from issue #3599's re-recorded sample
  (same station, different reading: wind now non-zero, temp/humidity/UVI/lux
  differ).
- codes_test.txt / codes_test.json - the two raw codes above, extracted via
  `-R 244:v -M level`.

No dedicated WS90 test fixtures existed in this repo before; both captures
decode cleanly with a valid CRC.
