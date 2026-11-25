# CAME TWEE gate remotes

433.92 MHz, Manchester coded, half-bit 500 us, a 1 bit is high then low. A button press sends
15 messages of 54 bits with a counter from 14 down to 0, each followed by a 51 ms gap.

The top 22 bits are the constant 0x3fff72. The low 32 bits are the code XOR a value for the
counter c (the low nibble): three bytes of 0x0e + 0x0f * c and the byte 0x11 * c. In the
de-XORed code the button is bits 6-9 and the 10 DIP switches are bits 18-27 (switch 1 first).
No integrity check besides the constant, the decoder is disabled by default.
