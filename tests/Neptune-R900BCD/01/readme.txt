Neptune R900 BCD flow meter (Neptune T-10)

Captures and reference readings contributed by @kirks, see
https://github.com/merbanan/rtl_433_tests/pull/517

Contents:
  g012_912.38M_1000k.cu8, g020_912.38M_1000k.cu8
                - two separate captures of the same meter
  *.json        - expected output for protocol 385, Neptune-R900BCD
  protocol      - selects protocol 385; the BCD decoder is not enabled by
                  default because it overlaps the plain Neptune-R900 frame
                  format and only the meter knows which encoding it uses
  rtlamr.txt    - readings from rtlamr over the same time window
  900bcd.jpg    - photo of the meter, taken slightly later but close to the
                  captured readings

These meters use the same frame layout as the plain Neptune R900, but encode
the 24-bit consumption field as six BCD digits instead of binary. The captured
field is 0x223700: read as binary that is 19019520, read as BCD it is 223700,
which is what both rtlamr and the meter display show.

No technical specification is available from Neptune.
Product page: https://www.neptunetg.com/products/watermeters/residential/t10/

Two files from the original submission are not included here:
  g016_912.38M_1000k.cu8 - contains a single 36 us pulse, no decodable frame
  g015_912.38M_1000k.json - no matching capture was submitted
