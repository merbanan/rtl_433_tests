# RFXMeter / RFXPower

Samples captured by @dblas, see https://github.com/merbanan/rtl_433/issues/2141
and decoder discussion at https://github.com/merbanan/rtl_433/pull/2142.

Each capture contains repeated transmissions from two RFXMeter addresses
(`id` 1 and 2). The counter (`msg_value`) advances by one between the two
captures for each address, confirming the byte order and checksum.
