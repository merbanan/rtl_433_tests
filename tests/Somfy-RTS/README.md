# Somfy RTS

See https://github.com/merbanan/rtl_433/issues/3038.

A roller-shade remote already decoded by `src/devices/somfy_rts.c`'s existing
"seed is the actual button code" quirk (previously only documented for the
TEL-FIX wall-mount remote), but with one button meaning missing: holding the
pairing button sends the control nibble fixed to `0xf` with seed low nibble
`0xc`, repeated for as long as the button is held -- this showed up as the
unmapped `? (12)` label. Confirmed against the `-R 167:vv` log the reporter
attached (`somfy-like-packets.txt`) that the control nibble is `0xf` for all
of Down/Stop/Up/Prog on this remote (same quirk, different seed high nibble:
`0x9.` here vs `0x8.` on the TEL-FIX remote), so this is the same code path,
just missing one label.

No `.cu8` capture was attached, only demodulated codes from a `-vv` log
dump, so this uses the `codes_test.txt`/`codes_test.json` fixture style
instead of a real IQ capture.
