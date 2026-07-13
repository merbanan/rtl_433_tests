# Wireless M-Bus, Mode T -- IMT meter behind a repeater (CI=0x72 long header)

From https://github.com/merbanan/rtl_433/issues/1807 (Aquastream water
meter, manufacturer IMT). Requires `-Y minmax` to decode at all, same as
`../01/` (`-Y magest`, used alongside it in the issue thread, turned out
not to be necessary).

This capture exercises the CI=0x72 "long transport layer" header, which
`m_bus.c` didn't handle at all (only the CI=0x7A short header was
implemented) -- AC/ST/CW/pl_offset stayed at their zero-init value and the
data-record walker started reading records from inside the header's own
secondary-address bytes, producing garbage values (e.g. a multi-billion
m3/min volume flow) instead of real readings. Fixed in merbanan/rtl_433.

```
rtl_433 -r g001_868.9M_1000k.cu8 -Y minmax -F json
{"model":"Wireless-MBus","mode":"T","M":"IMT","id":10025571,"version":5,
 "type":14,"type_string":"Bus/System component","C":68,"data":"4644b425...812405",
 "CI":114,"AC":154,"ST":0,"CW":9520,"payload_encrypted":1,"mic":"CRC"}
```

`CW`/Configuration Word now correctly decodes to a real value (was always
0 before the fix) and correctly trips the existing "payload encrypted"
check -- this meter's application-layer payload is AES-encrypted per OMS,
so the actual volume/flow readings aren't recoverable without the
device's key regardless of this fix; ground-truth readings from the
issue's screenshots (total volume 669.000 m3, flow 0 l/h at capture time)
can't be cross-checked against decoder output for that reason.

No `.json` reference for the same demod-settings reason as `../01/`.
