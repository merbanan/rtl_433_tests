# Chamberlain CWPIRC PIR sensor

See https://github.com/merbanan/rtl_433/issues/2582 -- a 26-comment thread
where zuckschwerdt, ProfBoc75, klohner and the reporter kuenkin reverse-
engineered the framing (preamble `552dd4`, two 48-bit sub-messages each
prefixed 0x00/0x01, CRC-16/XMODEM poly 0x1021 init 0x0000). ProfBoc75's
decoder (PR #2962) reports the two raw sub-messages plus CRC integrity;
the relationship between them (motion/battery/sensor ID) was never
solved despite the extended investigation, and remains a TODO in the
decoder's docstring.

`01/`-`04/` are 4 real `.cu8` captures pulled from the issue's attached
zips, each a distinct transmission (different msg_0/msg_1 pair), no
other-decoder collisions. Pulled from `chamberlain_r820t_distance(2).zip`
specifically -- the R820T-tuner recaptures that ProfBoc75 confirmed as
good signal in the thread, not the original FC0012 batch that
zuckschwerdt flagged as "severely overloaded". Of 161 `.cu8` files across
all 4 attached zips checked, only these ~15 decode cleanly (consistent
with klohner's own comment that "many of these sample files don't
decode too well").

`codes_test.txt`/`codes_test.json` additionally hold 85 unique hex codes
hand-transcribed across the thread (triq.net bitbench links, flex-decoder
dumps), each independently verified against CRC-16/XMODEM before
inclusion -- a much larger sample than the 4 real captures alone.

While collecting these, found and fixed two bugs in the merged decoder:
an `&&`/`||` logic mistake in the message-marker check, and a missing
tolerance for a 1-bit demod misalignment ProfBoc75 flagged in the
thread (comment from 2023-08-04) -- 4 of the 85 codes needed exactly a
1-bit forward shift past the preamble match to decode.
