# Elero bidirectional blinds/awning remote (Silent Gliss and others)

See https://github.com/merbanan/rtl_433/issues/3083. Reporter's device is a
Silent Gliss SG11490 5-channel wall switch; the wire protocol is Elero's
general bidirectional 868/915 MHz protocol, also used by other Elero-based
motor brands.

`ignore` is present on `01/`-`03/`: this GFSK signal only demodulates with
the non-default `-Y minmax` FSK pulse detector, which `run_test.py` has no
mechanism to pass per fixture (see `tests/hanwell_ml4000/` for the same
situation). Test manually with:

```
rtl_433 -r 01/g003_869.4M_2048k.cu8 -Y minmax -R 372 -F json
```

`01/`-`03/` (Ch1 Up/Stop/Down) are 3 of the 60 real captures the reporter
posted (15 each of channel 1/2/3 Up/Stop/Down presses, plus 15 of an "all
channels" button, 5 of each action). Verified the whole set, not just these
three files: demodulated all 60 myself (`-Y minmax -X 'm=FSK_PCM,s=13,l=13'`),
reproducing byte-identical codes to what's independently posted in the issue
thread by the maintainer. 38 of 60 have a complete enough capture to pass the
CRC (the rest are cut a few bits short by the demod) -- of those 38, every
single one decodes to the channel and command implied by its position in the
reporter's capture sequence (5x Up, 5x Stop, 5x Down, per channel, in order),
across all 4 channel groupings including the multi-destination "all
channels" case. All 38 CRC-valid codes (not just Ch1) are in
`codes_test.txt`/`codes_test.json`, run through `rtl_433 -y "<code>"` --
unlike the flex-decoder fixtures elsewhere in this repo, this is a compiled
decoder so `-y` works directly without needing the underlying `.cu8` for
every code.

The 8-byte trailing "obfuscation" block is not a checksum or rolling-code
authenticator -- it's fixed and reversible, using the exact algorithm from
`QuadCorei8085/elero_protocol`'s `xor_decode.py` (nibble substitution table,
two decrementing-key nibble subtractions, one byte-XOR step). An earlier,
different theory floated for this field (a simple advancing-XOR-keystream)
was tested against this same data and did not hold up -- the substitution
algorithm is the one that is actually verified here.
