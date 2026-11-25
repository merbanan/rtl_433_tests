# CAME Atomo gate remotes

433.92 MHz rolling code remotes. Each parcel is a 1200 us pulse and a 600 us gap, then 60 bits
Manchester coded with a half-bit time of 600 us (a 1 bit is low then high), then a 68 ms gap.
A button press sends up to 8 parcels.

The 64 bit message (sent without its low 4 bits) has bits 8 to 58 scrambled with a 7 bit shift
register (feedback bit 3 XOR bit 4) seeded with the negated hold counter, byte 0 is XOR 5.
After descrambling: hold counter (7 bit), press counter (16 bit), serial (32 bit), button code
(4 bit, 0/2/4/6 for buttons 1 to 4). No integrity check, the decoder is disabled by default.
