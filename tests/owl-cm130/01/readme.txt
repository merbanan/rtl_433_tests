OWL CM130 energy monitor, from https://github.com/merbanan/rtl_433/issues/1493
(out.zip attached by @mzealey). Captures taken while pressing the reset button,
so they carry no meaningful power/energy readings.

Oregon-Scientific v3 family, OOK Manchester, preamble 00 00 00 60.

Raw messages (flex decoder, m=OOK_MC_ZEROBIT,s=490,l=490,r=2000), the message
proper starts at the 0x60 sync nibble:

    g002 : {121}0000006031df0000000000000000698
    g004 : {121}00000060320f0000000000000000238
    g006 : {121}0000006033fb00000000000000009b8

No CM130 decoder is merged yet (see ../readme.txt), so there are no reference
.json files for these captures.
