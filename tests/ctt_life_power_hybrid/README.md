Cellular Tracking Technologies (https://celltracktech.com/) LifeTag/PowerTag/HybridTag.

The CTT LifeTag/PowerTag/HybridTag is a lightweight transmitter used for wildlife tracking and research - most commonly used with the Motus Wildlife Tracking System (https://motus.org/).
The tags transmit a unique identifier (ID) at a fixed bitrate of 25 kbps using Frequency Shift Keying (FSK) modulation on 434 MHz.

The packet format consists of:

    • PREAMBLE: 24 bits of alternating 1/0 (0xAA if byte-aligned) for receiver bit-clock sync (preamble length can be shorter, depending on hardware)
    • SYNC:     2 bytes fixed pattern 0xD3, 0x91 marking the packet start
    • ID:       20-bit tag ID encoded into 4 bytes (5 bits per byte) using a 32-entry dictionary
    • CRC:      1-byte SMBus CRC-8 over the 4 encoded ID bytes

    AA AA AA   D3 91   78 55 4C 33   58
   |--------| |-----| |-----------| |--|
    Preamble   Sync        ID       CRC

    A beep is a single packet.

    LifeTag - programmed with a standard 5-second beep rate.
    PowerTag - user-defined beep rate
    HybridTag - transmits a beep every 2-15 seconds

There's a 20-bit subset of the 32-bit ID space set aside for Motus tag use. We set `valid_motus` to true if all 4 bytes of the ID are present in the Motus code dictionary.
However, `valid_motus` not being set doesn't mean that a tag is invalid, just that it's not recognized as a tag used with Motus.
