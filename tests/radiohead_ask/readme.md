RadioHead is a open source library for microprocessors like arduino.
It has an ASK/OOK driver for cheap 433MHz transmitters which
only need Vcc, GND and a TX pin. The signal is modulated (turned off and
on) by setting the TX pin on high and low.

The ASK-driver does a few operations to provide basic coding:
(Quote from RadioHead webpage. Link is below)
--------------------------------------------------------------------
- 36 bit training preamble consisting of 0-1 bit pairs
- 12 bit start symbol 0xb38
- 1 byte of message length byte count (4 to 30), count includes byte 
  count and FCS bytes
- n message bytes (uincluding 4 bytes of header), maximum n is 
  RH_ASK_MAX_MESSAGE_LEN + 4 (64)
- 2 bytes FCS, sent low byte-hi byte
Everything after the start symbol is encoded 4 to 6 bits, 
Therefore a byte in the message is encoded as 2x6 bit symbols, 
sent hi nybble, low nybble. Each symbol is sent LSBit first.
The message may consist of any binary digits.
-----------------------------------------------------------------
Everything is documented here:
http://www.airspayce.com/mikem/arduino/RadioHead/classRH__ASK.html




Provided recorded samples are basically a unsigned int counter 
which starts counting from 0. Bitrate is set to 500 bps but can be 
defined in a wide range.

Different message lengths and bps can be provided.
