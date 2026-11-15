Baylan water meter with UM-1 RF module.

Recorded with an RTL-SDR: `rtl_433 -f 868M -s 1M -S unknown` (1 MS/s, cu8).
The signal is at about 867.96 MHz, 2-FSK, 38.4 kbps.

- `g001`, `g004`, `g006`: meter ID 00081647, counter display showed 0629 m3 -> decodes as 629.1 m3
- `g002`: a second meter nearby, ID 00083126, 273.4 m3 (no display reading available)

Photo: baylan_um1_meter.jpg
