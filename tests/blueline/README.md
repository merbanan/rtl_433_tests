# Blueline PowerControl Monitor

These samples are from a Blueline PowerControl Monitor BLI-28000.  From everything I've read online, this
should be radio-compatible with all the other Blueline PCM models, as well as the Black and Decker EM100B.

Receiving most of the message types this sensor generates requires that the sensor's ID is known beforehand,
to know how to modify the data before validating the CRC and processing it.  The only exception is the one
message that actually transmits the ID itself, but that is only sent when the sensor is first powered on or
the button on it is pressed.

Further discussion and expected usage is provided in the decoder's source file in the main rtl_433 project.

The four samples in this directory provide an example of what each payload type looks like, to exercise
each decoder.  Each contains a burst of 3 or 4 rows of data.  The ID is repeated 4 times by itself.  The gap
payload is repeated 3 times by itself.  The temperature and impulse payloads are repeated twice followed by 
a gap payload.

Only the id_45364_433.92M_250k.cu8 sample can be decoded by the default operation of rtl_433 without parameters.

Decoding the other samples requires passing the transmitter ID as a parameter to the decoder.  These samples
were recorded from a monitor using ID 45364, so the command line would be like this:

rtl_433 -R 176:45364 -r gap_45364_433.92M_250k.cu8
