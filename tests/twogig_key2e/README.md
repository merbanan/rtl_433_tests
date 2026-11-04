# 2GIG-KEY2E-345 encrypted keyfob

See https://github.com/merbanan/rtl_433/issues/2584. Same OOK/Manchester
family and 24-bit preamble as the plain Honeywell/2Gig door-window
sensors (protocol 70, `honeywell.c`), but a longer 72-bit frame. CRC-16
(poly 0x8005, init 0x4c57) confirmed by zuckschwerdt and independently
re-verified here against all 7 distinct real codes found across the
thread, from two different physical units.

The 32-bit "id" and 16-bit "status" fields are almost certainly
encrypted (2GIG's undocumented "eSeries Encrypted Technology") and are
reported as opaque hex, not as a real `id` field. Nobody has decoded
them: the thread never collected two samples of the same button on the
same unit pressed twice, so there isn't even enough data to tell
whether it's a rolling code. Decoder ships `.disabled = 1` for this
reason -- see the file's docstring.

`.cu8` captures in `01/`-`04/` are dfiore1230's own button1-4 recordings
from https://github.com/merbanan/rtl_433_tests/pull/456 (unmerged).
Each directory has a `protocol` file (`370`) since the decoder is
disabled by default.

Note: buttons 3 and 4 decode to the exact same code (`b19b9da3`/`721a`).
This isn't a transcription slip on my part -- it's reproducible from
dfiore1230's own capture files and matches klohner's independent
bitbench extraction of the same two buttons. Unclear whether this is a
capture mistake (e.g. button 3 recorded twice) or a real device quirk.
