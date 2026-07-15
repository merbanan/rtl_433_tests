# Kidde RF-SM-DC wireless-interconnect smoke alarm

See https://github.com/merbanan/rtl_433/issues/2240 for the original request
and the reverse engineering discussion.

OOK, differential Manchester coded (DMC), 400 us chip width, preceded by a
non-DMC "de-sync" preamble of unknown length. Decoded (post DMC) message is
25 bits: a fixed start bit, an 8 bit reflected "house code" (the alarm's
DIP switches), a fixed 0x7f byte, then the same reflected house code again
XOR 0x80 (a simple double-send integrity check, not a real checksum).

Only the periodic idle/presence "heartbeat" message is confirmed (sent
whether or not the alarm is going off) -- no alarm/test/low-battery capture
has ever been posted to the issue.

`disabled = 1`: the double-send check is not a real CRC, and a
repeated-row requirement (the usual rtl_433 idiom for a protocol without a
strong checksum) does not work here -- real repeats arrive 60-125 ms apart,
well past rtl_433's own (global) ~10 ms same-reception cutoff, so every
repeat is always its own separate single-row capture.

- 01/ - one real capture (DIP 00000000, from `kidde_RF-SM-DC_3dif-codes.zip`;
  every repeat across the whole multi-second file decodes to the same,
  correct ID). Uses a `protocol` file (361, disabled by default) since the
  decoder needs to be explicitly enabled.
- codes_test.txt/json - the dominant repeated raw code (verified against a
  wide margin over any other pattern in each reporter's capture) for all 4
  real DIP switch settings actually reported in the issue: 00000000,
  10000000, 11111111 (`kidde_RF-SM-DC_3dif-codes.zip`) and 11110000 (the
  same reporter's earlier `g001_434M_1024k.zip`, at a different sample
  rate, superseded by the 3dif capture for the same DIP range but kept
  here since it's the original capture that started the reverse
  engineering).
