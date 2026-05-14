# Heidemann HX Extension

Testdata for Heidemann HX Extension. The original manufacturer is probably Quhwa.
This is a range extender for Heidemann HX door bells.
The sender product IDs are   HX 70372, HX 70835, HX 70836.
The receiver product IDs are HX 70825, HX 70835, HX 70873.

The device uses OOK modulation with Pulse Width Coding (PWM) on 433.92 MHz:
- '1' bit: Long gap (479 us) followed by short pulse (332 us)
- '0' bit: Short gap (135 us) followed by long pulse (676 us)

The frame length is 13 bits, it is repeated 97 times with a gap of 6200 us between the repeats.

The frame contains the following information (MSB sent first):
- Melody (bits 12 to 9): which of the 16 melodies the receiver should play.
- Device-ID (bits 8 to 1): It is randomly generated on each power on
- Constant (bit 0): always 1

## Test files and their decoded values

| Test file | ID  | Melody |
| --------- | --- | ------ |
| g002      | 180 | 1      |
| g017      | 180 | 3      |
| g040      | 180 | 5      |
| g071      | 180 | 9      |
| g116      | 180 | 14     |
| g124      | 180 | 6      |
| g127      | 221 | 1      |
| g144      | 221 | 3      |

## Run tests

```bash
for i in *.cu8 ; do ../../../../rtl_433/build/src/rtl_433 -F json -R 0 -c ../../../../rtl_433/conf/heidemann_hx_extension.conf -r $i 2>/dev/null  | jq -c ".filename=\"$i\""; done
```

## Output of tests

```json
{"time":"@0.289840s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"da08","id":180,"melody":1,"filename":"g002_433.92M_250k.cu8"}
{"time":"@0.272996s","model":"Heidemann-HX-Extension-Cfg","count":25,"num_rows":25,"len":13,"data":"da08","id":180,"melody":1,"filename":"g004_433.92M_250k.cu8"}
{"time":"@0.287588s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"da18","id":180,"melody":3,"filename":"g017_433.92M_250k.cu8"}
{"time":"@0.287436s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"da28","id":180,"melody":5,"filename":"g040_433.92M_250k.cu8"}
{"time":"@0.314844s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"da28","id":180,"melody":5,"filename":"g041_433.92M_250k.cu8"}
{"time":"@0.070564s","model":"Heidemann-HX-Extension-Cfg","count":34,"num_rows":35,"len":13,"data":"da28","id":180,"melody":5,"filename":"g042_433.92M_250k.cu8"}
{"time":"@0.086368s","model":"Heidemann-HX-Extension-Cfg","count":50,"num_rows":50,"len":13,"data":"da28","id":180,"melody":5,"filename":"g043_433.92M_250k.cu8"}
{"time":"@0.286468s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"da48","id":180,"melody":9,"filename":"g071_433.92M_250k.cu8"}
{"time":"@0.284824s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"da70","id":180,"melody":14,"filename":"g116_433.92M_250k.cu8"}
{"time":"@0.286372s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"da30","id":180,"melody":6,"filename":"g124_433.92M_250k.cu8"}
{"time":"@0.289360s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"ee88","id":221,"melody":1,"filename":"g127_433.92M_250k.cu8"}
{"time":"@0.284008s","model":"Heidemann-HX-Extension-Cfg","count":49,"num_rows":50,"len":13,"data":"ee98","id":221,"melody":3,"filename":"g144_433.92M_250k.cu8"}
```
