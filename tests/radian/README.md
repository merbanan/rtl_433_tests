# RADIAN / RADIAN0 meter

See https://github.com/merbanan/rtl_433/issues/3408. Physical/link layer
reverse engineered by @bennesp (raw hex posted in the issue, no IQ capture
attached). FSK_PCM at 2400 baud, UART 8N2 framing (start=0, 8 data bits
LSB-first, no parity, two stop bits), CRC-16/KERMIT trailer.

Frame layout (after CRC verification):

    L C rx[5] tx[5] body crc:16

The one real sample is a `control=0x11` ("response") frame whose body wraps
a complete wired M-Bus (EN 13757-2) telegram -- `68 L L 68 C A CI ...
checksum 16` -- for a Heat Cost Allocator. This is decoded by reusing the
existing wireless M-Bus CI/AC/ST/CW and DIF/DIFE/VIF/VIFE parsing in
`m_bus.c` (`m_bus_parse_ci()`, `parse_payload()`), which is also why the
decoder lives in `src/devices/m_bus.c` rather than its own file.

On this sample the full record stream decodes: `software_version`, two
timedate/date fields, two flow/external temperatures, 19 storage-numbered
H.C.A. units records, and an energy field -- including a 32-bit float
coding (`m_bus_decode_val()`'s case 5, a fix shared with wireless M-Bus),
rounded to the nearest integer per the existing int+exponent convention.

## Known limitations

- Only one real frame exists (a `-y` code from the issue thread, not a raw
  IQ capture) -- no `.cu8` fixture is possible yet.
- `inst_hca_0` appears twice with different values (`0.000` and `3.000`):
  two distinct records (an integer coding and the 32-bit float one) both
  compute the same storage-number-0 key. A duplicate JSON key, not a typo
  in this fixture -- matches a similar pre-existing issue documented in
  `../m_bus/01/README.md`, not investigated further here.
- The wired-frame secondary address (manufacturer/ID/version/medium) is
  reported as raw hex in `body` rather than decoded -- its bytes don't look
  like standard BCD, so asserting a manufacturer/ID reading wasn't
  confident enough to include.
- Collides with `Watchman-Plus` when run unrestricted (see `protocol`
  marker forcing `-R 379`) -- a normal cross-decoder false positive in the
  other decoder, not a RADIAN problem.
