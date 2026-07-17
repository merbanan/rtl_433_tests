# Chamberlain CWPIRC PIR sensor

See https://github.com/merbanan/rtl_433/issues/2582 -- a 26-comment thread
where zuckschwerdt, ProfBoc75, klohner and the reporter kuenkin reverse-
engineered the framing (preamble `552dd4`, two 48-bit sub-messages each
prefixed 0x00/0x01, CRC-16/XMODEM poly 0x1021 init 0x0000), but never
decoded the payload itself.

The payload has since been decoded: each 40-bit message half reuses, bit
for bit, the Security+ 2.0 joint-message permutation from `secplus_v2.c`
-- an unrelated Chamberlain product's payload encoding, reused verbatim
inside this different FHSS transport. Verified independently against
this fixture set: the reassembled 40-bit `id` stays constant per
physical sensor across many transmissions while a 28-bit `rolling`
counter changes every time, and bit 5 of `id` is a low-battery flag
(confirmed by 4 consecutive low-battery reports decoding to consecutive
rolling values). See the decoder's docstring for the full writeup.

`01/`-`04/` are 4 real `.cu8` captures pulled from the issue's attached
zips, each a distinct transmission, no other-decoder collisions. Pulled
from `chamberlain_r820t_distance(2).zip` specifically -- the R820T-tuner
recaptures that ProfBoc75 confirmed as good signal in the thread, not
the original FC0012 batch that zuckschwerdt flagged as "severely
overloaded". Of 161 `.cu8` files across all 4 attached zips checked,
only these ~15 decode cleanly (consistent with klohner's own comment
that "many of these sample files don't decode too well"). `02/` is a
real, CRC-valid capture whose message permutation nibble falls outside
the 9 values Security+ 2.0 actually uses (same restriction `secplus_v2.c`
itself enforces) -- kept here specifically to cover that rejection path,
so its expected `.json` is intentionally empty.

`codes_test.txt`/`codes_test.json` additionally hold 85 unique hex codes
hand-transcribed across the thread (triq.net bitbench links, flex-decoder
dumps), each independently verified against CRC-16/XMODEM before
inclusion. 75 of the 85 also decode the payload; the other 10 hit the
same permutation-nibble rejection as `02/`.

While collecting these, found and fixed two bugs in the merged decoder:
an `&&`/`||` logic mistake in the message-marker check, and a missing
tolerance for a 1-bit demod misalignment ProfBoc75 flagged in the
thread (comment from 2023-08-04) -- 4 of the 85 codes needed exactly a
1-bit forward shift past the preamble match to decode.
