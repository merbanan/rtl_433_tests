# Wireless M-Bus, Mode T -- Diehl Hydrus 2.0 water meter

From https://github.com/merbanan/rtl_433/issues/3393: raufaser was
receiving this signal on 868MHz and it was tripping a false positive in
the Arad/Master Meter Dialog3G decoder (protocol 260) -- a separate bug,
already fixed (see `../../Schrader_TPMS_SMD3MA4/README.md`-style history
in the issue itself, or just the issue for the Arad fix commits). The
actual device is not an Arad meter at all: it's a Diehl Hydrus 2.0 water
meter (manufacturer code `DME` = Diehl Metering), confirmed by `M: "DME"`
and `type_string: "Water"` below, and by raufaser reading "DIEHL HYDRUS"
off the physical meter label.

## Does not decode out of the box

Default settings (`rtl_433 -r g001_868.9M_1000k.cu8`) produce nothing --
not even a detected package under `-A`.

**`-Y minmax` alone is sufficient** -- `-Y magest` (found alongside it by
@ProfBoc75 in the issue thread) turned out not to be necessary; verified
against this file and all other real captures from both issues #1807 and
#3393. (Running `-Y minmax -A`, the generic pulse *analyzer*'s own
guess-and-decode, does produce garbage on this signal -- but that's the
analyzer's naive heuristic slicer, unrelated to whether the real M-Bus
decoder can decode it.)

```
$ rtl_433 -r g001_868.9M_1000k.cu8 -Y minmax -F json
{"time" : "@0.037023s", "model" : "Wireless-MBus", "mode" : "T", "M" : "DME",
 "id" : 84850129, "version" : 118, "type" : 7, "type_string" : "Water",
 "C" : 68, "data" : "5344a5112901858476078c00ae900f002c25f00c2f005d8c2c1dac2ca7c07a3a80310710a7f26ca73e8a384744684fe6a79dd0844ebe8c89debb0615906f9f9581b60dbf73e59f525cbc0182172ac76923f254d4",
 "CI" : 140, "AC" : 0, "ST" : 0, "CW" : 0,
 "max_volume_flow_min_1" : "2691.493 m3/min", "inst_energy_wh_0" : "0.700 kWh",
 "inst_power_w_0" : "150253200.000 kW", "inst_power_w_0" : "329263.000 MW",
 "max_power_w_0" : "0.000 kW", "mic" : "CRC"}
```

The low-level M-Bus framing is solid (`mic: "CRC"` -- a real CRC-valid
frame, not a fluke; `id`/`M`/`type_string` correctly identify the physical
device). But several of the higher-level derived fields look wrong --
`inst_power_w_0` appears twice with wildly different values (a duplicate
JSON key), and other captures from the same issue produce obviously
garbage fields like `min_ontime_h_0: "-1894580197.000 hours"`. That looks
like a separate bug in `src/devices/m_bus.c`'s data-record field mapping,
not investigated further here.

The capture doesn't decode under the default pulse-detector settings that
`bin/run_test.py` uses -- only under `-Y minmax` -- so a `demod` file
supplies that flag and this directory runs as a normal regression test.
