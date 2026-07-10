# Florabest FB-TH-1 BBQ Thermometer

See https://github.com/merbanan/rtl_433/issues/1223 for the decoder
reverse-engineering discussion (author ai-xyz, with protocol details
worked out together with @zuckschwerdt).

`01/g045_433.92M_250k.cu8` and `01/g047_433.92M_250k.cu8` are real
captures from the issue's attached `samples.zip`, both at room
temperature (id 0x4909, ~22 C).

`test_codes.txt`/`test_codes.json` contain a spread of temperature
readings (21-229 C) extracted from the bitbench links posted across the
issue discussion, useful for exercising a wider range of the 13-bit
temperature field than the two real captures alone. Expect small
(<1 degree) differences from the originally reported values -- the
reporter noted the sensor itself appears to truncate/round its own
internal reading before transmitting.
