OWL CM130 energy monitor

See https://github.com/merbanan/rtl_433/issues/1493.

Sister device to the CM160/CM180, Oregon-Scientific v3 family, OOK
Manchester, 97-bit message, preamble 00 00 00 60. Decoded as model
"Oregon-CM130" by the oregon_scientific decoder (protocol 12).

Contents:
- 01/           three raw .cu8 captures (reset-button presses)
- codes_test.*  all 47 known readings, as on-wire frames for `rtl_433 -y`
                plus their reference decodes

Message format (12 bytes, after the decoder's reflect_nibbles(), then a
per-byte nibble swap as the CM130 branch applies):

    60 II II PL PH 0. EE EE EE EE XX
    -- sync (0x60)
    II II  house code (id = byte 2)
    PL PH  power, 16-bit little endian, in units of 16 W
           power_W = ((byte4 << 8) | byte3) * 16
    EE..   32-bit little-endian cumulative energy counter (bytes 6..9),
           reported as energy_kWh = counter / 8192 (8192 = 2^13 = 16 * 512,
           matching the power scale of 16). This is the meter's absolute
           lifetime total, so it reads higher than the console, which shows a
           relative value with a device-specific offset (~35 kWh here).
    XX     checksum, byte 11

Checksum (was unsolved in the issue for years, now solved): CRC-8 with
polynomial 0x07, init 0x00, non-reflected, no final XOR, computed over
message bytes 1..10 in the reflect_nibbles() domain; the stored value is
that CRC with its two nibbles swapped, i.e.

    crc8(&msg[1], 10, 0x07, 0x00) == swap_nibbles(msg[11])

Validated against all 47 readings here and the 3 reset captures.
