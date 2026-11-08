# Cotech 36-9231 weather station

Clas Ohlson Cotech 36-9231, outdoor unit FT020TL, indoor unit FT0203A.
The outdoor unit transmits LoRa SF7, 500 kHz bandwidth, on 868.35 MHz.

Samples from https://github.com/merbanan/rtl_433/issues/3242

- 01: FT020TL-2.zip, `rtl_433 -f 868M -S all`, no antenna, sensor 40-50 cm from the receiver.
  Indoor unit display: 21.7 C, 39 %, NW, 0 m/s, 0 m/s
- 02: FT020TL.zip, `rtl_433 -vv -f 868350000 -R 0 -S unknown`, sensor within 10 cm of the receiver.
- 03: 36-9231.zip, a second station.
