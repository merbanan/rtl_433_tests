# Marantec garage door remote

Fixed code remote, seen on 868.35 MHz and 433.92 MHz. Decoded by `Marantec-Remote`.

Manchester coded, half-bit 1000 us (500 bit/s), a 1 bit is low then high. 49 bits per message,
repeated after a 10 ms gap: a leading 1, 8 bit constant (0x30), 20 bit serial, 4 bit button,
8 bit low serial (0x86 on known remotes), CRC-8 (poly 0x1d, init 0x01).

All samples are Flipper Zero transmissions (Marantec protocol) with made-up codes, recorded with
an RTL-SDR.

- `01`: 868.35 MHz, 1024 kHz
- `02`: 433.92 MHz, 250 kHz

Flex decoder:

    rtl_433 -X 'n=marantec,m=OOK_MC_ZEROBIT,s=1000,l=0,r=4000,t=300,invert'
