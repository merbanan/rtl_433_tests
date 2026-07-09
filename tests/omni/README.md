# Omni Multisensor

See https://github.com/merbanan/rtl_433/pull/3278 for the decoder submission
(unmerged as of this writing, author hdtodd). The decoder covers a DIY
microcontroller (Raspberry Pi Pico 2 / Arduino) transmitting up to 16
possible internal data-field formats in one packet; only format 0 (core
temp + voltage) and format 1 (BME688 indoor/outdoor temp/humidity/
pressure/light) are implemented.

`01/g001_433.92M_250k.cu8` is a real capture posted in the PR discussion
(format 1, id 9), recovered from a gzip attachment on the PR.

`codes_test.txt`/`codes_test.json` contain the two manually-typed test
codes (`-y`) posted by @zuckschwerdt in the PR discussion covering both
implemented formats (0 and 1).
