# Silver Spring Networks mesh endpoint (narrow-band FHSS PHY)

See https://github.com/merbanan/rtl_433/issues/3583.

235 codes: 212 real frames converted from an independently-validated
canonical (F3A0-aligned) corpus for this issue, plus 23 noise/truncated
lines from the original two `.cu8` capture sets (a Badger Meter
GIF2014W-OSE report, 904.4 MHz and 916.45 MHz), kept as false-positive
regression coverage. The frames belong to the AMI mesh network the
endpoint rides on -- Silver Spring Networks' narrow-band FHSS mesh, based
on the IEEE 802.15.4g draft (Itron acquired Silver Spring Networks in
2018, so both OUIs appear on endpoint ids) -- logged by a mobile
(drive-by) reader.

Frame model, fully reverse-engineered:

    preamble | SFD 0xF3A0 | PHR(3) | scrambled PSDU(N) | scrambled FCS(4)

- PHR = `seed(8) | FCTRL(4) | EXT(1) | length(11)`, byte-aligned, in the
  clear. FCTRL and EXT are always `0` in every frame seen; `length` is the
  PSDU byte count (up to 2047, not just 8 bits -- an earlier draft of this
  decoder mis-parsed byte 1 as a fixed `0x00` marker and silently rejected
  any frame with `length >= 256`, which this corpus contains).
- PSDU + FCS are scrambled by an 8-bit additive LFSR (`x^8+x^4+x^3+x^2+1`)
  with a per-hop seed. The FCS is a CRC-32/MPEG-2 over the *descrambled*
  PSDU. The decoder recovers the seed by trying all 255 values and keeping
  the one whose CRC matches -- a decode is therefore CRC-verified
  (`mic: CRC`), and the decoder is enabled by default.
- The PSDU is `FCTRL | [destination EUI-64] | [source EUI-64] | TLVs`.
  FCTRL bit 0/1 select the destination/source address, reported as
  `dst_id`/`src_id`; each address carries the `00:07:81` (Itron) or
  `00:13:50:ff:fe` (Silver Spring Networks) OUI, both confirmed against the
  IEEE OUI registry. The TLV stream (DLL/MPDU type/length/value records,
  US20090310511A1) is walked and reported as `tlvs` (`D<type>/<len>` or
  `M<type>/<len>`, MPDU 17's mandatory nested TLV as `M17/<len>{...}`); the
  optional trailing DLL CRC-32/MPEG-2 (DLL type 6) is checked and shown as
  `:ok`/`:bad`.
- Several TLV values are decoded further, matching best-evidence candidates
  from an independent corpus analysis: `link` (poll/poll_ack/data/data_ack/
  broadcast, from FCTRL and which TLV types are present), `seq_num`/
  `frag_num`/`frag_more`/`retry` (Sequence Control), `fet` (Fractional Epoch
  Tick), `rssi` (signed RSSI candidate), `cli_tx_pri`/`cli_tx_time`/
  `cli_rx_pri`/`cli_rx_time` (Communication Link Info candidate),
  `sync_channel` (channel-sync candidate), `routes` (network/routing MPDU
  route advertisements: hop count, path/link cost candidates, egress/next-hop
  EUI-64s), and `ipv6` (IPv6/UDP datagrams with a verified checksum, plus
  `mgmt_len` for the UDP/648 management envelope's declared cleartext length
  -- the cipher/authentication suite and encrypted contents remain unknown).

210 of the 212 real frames descramble and CRC-validate (matching an
independent analysis of the same corpus exactly); the other 2 are damaged
captures. Uses a `protocol` file (`383`) to select this decoder explicitly.

Also includes 3 of the original real `.cu8` captures (out of the ~38
across both capture sets), exercising the full demodulation chain rather
than just the bit-level decode: `g003_904.4M_1000k.cu8` (poll_ack +
data_ack), `g024_904.4M_1000k.cu8` (broadcast with routes, plus a
poll_ack), and `g007_916.45M_1600k.cu8` (poll, at the other frequency
and sample rate the decoder is used at).
