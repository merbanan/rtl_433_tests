# LaCrosse Technology View LTV-TH2 / LTV-TH2i Thermo/Hygro Sensor

See https://github.com/merbanan/rtl_433_tests/pull/404 for the original
recordings, and https://github.com/merbanan/rtl_433/pull/3406 for the
decoder discussion (LTV-TH2i support).

`g001`/`g002_915M_1000k.cu8` are the two captures that made it into the
final merge, from sensor id `3335511`. `g001` uses the newer LTV-TH2i
CRC-8 init `0xb2` variant; `g002` uses the original LTV-TH2 init `0xac`.

`codes_test.txt` additionally recovers 5 codes from a second, independent
sensor (id `1306551`) that were posted in the PR discussion but dropped
from the final merged tree (the PR went through several rounds of
uploading and deleting `g001`-`g012` before settling on the final two
files).
