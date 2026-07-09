# NetAtmo outdoor temp/hum and wind sensors

See https://github.com/merbanan/rtl_433/pull/3396 for the decoder submission
(unmerged as of this writing, author wxkpr).

No raw `.cu8` captures were available (the PR/issue thread only included
hex byte examples), so `codes_test.txt`/`codes_test.json` contain the three
example frames from the decoder's own doc comment: a TH data message, a TH
status message, and a wind data message.
