TFA Dostmann 30.390X T/H sensors series

See https://github.com/merbanan/rtl_433/pull/3446 for the protocol reverse
engineering (Jacob Maxa) and the CRC-32 confirmation (zuckschwerdt). That
PR is still open/unmerged; this decoder is an adaptation with several
bugs fixed (bounds check, model-name convention, humidity precision, id
string, non-static CRC helper) -- see the decoder's own doc-comment and
the commit that added it for details.

Why there's no `.cu8` sample here

No real IQ captures exist for this device anywhere searchable: not in
this repo, not attached to the PR or any linked issue, and a GitHub
search across both merbanan/rtl_433 and merbanan/rtl_433_tests turns up
nothing for this sensor family beyond the PR itself.

codes_test.txt/json contents

6 of the 7 codes are real device data, not fabricated: hand-transcribed
hex worked examples from the PR's own doc-comment (one each for ID-A0,
ID-A3, ID-A5, and three sequential ID-A4 readings), extracted by
concatenating each example's hex digits (ignoring the author's uneven
whitespace) and slicing into bytes. Each one independently validates
against the CRC-32 (poly 0x04c11db7, reflected, init/xorout 0xffffffff)
computed over its own bytes -- not just plausible, but cryptographically
confirmed to be genuine, uncorrupted device output. The 3 ID-A4 frames
additionally form an internally consistent sliding window: each frame's
"current" reading equals the next frame's "1 reading ago" value, and
so on, which a fabricated example could not satisfy by coincidence.

No genuine ID-A6 example exists in the PR text: it duplicates the ID-A0
example under an "A6:" heading, apparently a copy-paste error, since the
ID byte itself (0xa0) says ID-A0. The 7th code is a synthetic ID-A6
frame instead, built from the documented field layout the same way as
the other variants' real examples, just with fabricated values.
