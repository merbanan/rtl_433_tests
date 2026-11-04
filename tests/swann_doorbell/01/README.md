# Swann SWHOM-DC820P Wireless Doorbell Chime

Capture from https://github.com/merbanan/rtl_433/issues/2784, originally
posted by @tom-hooper; analyzed and refined by @klohner.

https://support.swann.com/hc/en-us/articles/4645286448153-HOM-DC820P-User-Manual

Fixed 25-bit code, OOK PWM, no CRC/checksum, per @klohner's flex decoder
(`../../../conf/Swann-Doorbell.conf`). Of the 5 samples originally attached
to the issue, only this one (`g002`) is a complete capture of the doorbell
signal - `g001` and `g003` are unrelated devices (Cotech-367959 and
Ambientweather-F007TH respectively, already decoded by other decoders),
and `g004`/`g005` are truncated captures of the same signal/code (same
25-bit id `007df78`, just missing the start or end of the transmission).
