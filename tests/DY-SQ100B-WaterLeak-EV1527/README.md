# DY-SQ100B water leak detector (EV1527 variant)

See https://github.com/merbanan/rtl_433/issues/2606. Some units sold under
this listing use a different RF chip than the one in `conf/LeakDetector.conf`
(33 bit, `short=316/long=968`, unverified against real captures) -- this is
a distinct, separately-verified variant: a classic EV1527-style fixed-code
PWM transmitter, confirmed against the two real `.cu8` captures attached to
the issue (short ~500us, long ~1500us, ~2048us bit period).

Use the flex decoder, not `-R`, since this isn't a compiled-in protocol:

```
rtl_433 -c conf/DY-SQ100B-WaterLeak-EV1527.conf -r <file>
```

`01/` is one of the two real captures (`g003`). The other real capture
(`g002`) and both files together only ever produced 2 distinct codes
(with/without an extra leading sync bit) -- both are in `codes_test.txt`/
`codes_test.json`, which also has a top-level `protocol` file pointing at
the same flex-decoder config as `01/`. No alarm/battery/heartbeat state
variation was ever captured, so only the raw 24 bit code is decoded;
there's no evidence for any further sub-field.

The same signal also happens to satisfy the existing `Generic-Remote`
decoder (protocol 30) -- this is a real, expected coincidental overlap
(the original reporter's own posted output showed this too), not a bug.
