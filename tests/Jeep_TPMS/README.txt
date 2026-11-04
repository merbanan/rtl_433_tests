Jeep (Continental?) FSK 10 byte Manchester encoded checksummed TPMS data.

See https://github.com/merbanan/rtl_433/issues/3364. Seen on a 2021 Jeep
Grand Cherokee (WK2); an OBD-II scanner identified the sensors as
Continental.

Wire format is identical to Citroen TPMS (protocol 82) -- both decoders
trigger on the same on-air data here, hence the `protocol` file forcing
380 rather than letting Citroen also fire. The only difference is the
pressure scale: Citroen's `raw * 1.364` reports exactly half of the real
tire pressure for this sensor; this decoder uses `raw * 2.728` instead.

Confirmed against the reporter's own session where all 4 tires were set
to 33-36 PSI: g031 decodes to 231.880 kPa (33.6 PSI) and g044 to
223.696 kPa (32.4 PSI), both in range. Temperature and id already matched
the reporter's OBD reading without any change.

Disabled by default (`.disabled = 1`) since it would otherwise double-
report every real Citroen TPMS user's data under a second model too.
