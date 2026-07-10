OWL CM130 energy monitor, from https://github.com/merbanan/rtl_433/issues/1493
(out.zip attached by @mzealey). Captures taken while pressing the reset button,
so power and energy read 0.

Oregon-Scientific v3 family, OOK Manchester, preamble 00 00 00 60. These now
decode as model "Oregon-CM130" (protocol 12); see the .json reference files
and ../readme.txt for the message format and checksum.

Raw messages after the decoder's reflect_nibbles() normalization (these match
zuckschwerdt's original example codes in the issue), with the checksum byte
last:

    g002 : 60 c8 bf 00 00 00 00 00 00 00 00 69
    g004 : 60 c4 0f 00 00 00 00 00 00 00 00 4c
    g006 : 60 cc fd 00 00 00 00 00 00 00 00 9d
