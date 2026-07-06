# EcoWitt WN20 Rain Gauge

High-sensitivity tipping bucket rain gauge, 0.3 mm per tip.
Battery-powered (2xAAA), transmits every 48 seconds at 915 MHz FSK PCM.

Manufacturer page: https://www.ecowitt.com/shop/goodsDetail/325

Captured with `rtl_433 -f 915M -S unknown -T 120` on RTL2832U.

All three captures contain the same device (ID 11399) with 1.9 mm cumulative rain
and 3.04V battery (fresh 2xAAA). The gateway (GW1100B_V2.4.4) confirms the battery
voltage matches and reports 100% battery level.

Protocol is identical to the WH40 family (type code 0x40) in ambientweather_wh31e.c,
but uses type code 0x20, a 10-byte payload (one extra byte before CRC/SUM vs WH40's 9),
and full-byte battery encoding at 0.02V per unit instead of 5-bit at 0.1V.
