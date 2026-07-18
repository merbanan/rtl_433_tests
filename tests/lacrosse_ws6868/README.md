# LaCrosse WS6868 weather station (TX231RW, TX232TH-LCD)

See https://github.com/merbanan/rtl_433/issues/3120.

`01/` (TX232TH-LCD, temperature/humidity) and `02/` (TX231RW, wind/rain)
are one real capture each. `codes_test.txt`/`codes_test.json` cover all
22 real captures the reporter attached (10 TX232TH-LCD + 12 TX231RW;
one TX232TH-LCD capture, `g001`, never produced a usable code and isn't
included).

TX232TH-LCD's temperature and humidity are verified digit-for-digit
against the sensor's own displayed readings, posted directly in the
issue thread (20.1-21.1 °C, 53-56%) -- 10/10 exact matches, plus CRC-8
(poly 0x31, init 0x00) valid on every sample.

TX231RW's header (id/battery/test/channel/counter), CRC-8, and an
additional checksum (sum of the preceding bytes including the CRC, &
0xff) are all confirmed the same way. Its actual wind/rain payload is
not: none of the 12 real captures have any wind or rain occurring, so
all 6 payload bytes are fixed at the same value in every single one --
there's no way to locate speed/direction/rainfall fields without a
capture where they actually vary. Reported as `data_raw`. The decoder
ships `.disabled = 1` for this reason.
