# Sefis M3 / Careud / Sykik SRTP300 TPMS

See https://github.com/merbanan/rtl_433/issues/3342. Reverse engineered by
@ivantichy (who built a CC1101 transmitter and confirmed the real display
accepts re-encoded packets), with the CRC identified by @ProfBoc75.

This decoder started from a community draft (`tpms_sefis_m3_draft.c`,
not from this issue thread directly) and was independently re-verified
here rather than trusted as-is: CRC-16/XMODEM, the pressure "page"
field layout, and the temperature formula were all re-derived/checked
against the same 24 real frames from @ivantichy's controlled 260->10 kPa
(2.6->0.1 bar as originally measured) deflation series (the only ground
truth available -- no raw IQ captures were used, only the demodulated
hex the issue posted). One real bug was caught and fixed in the
process: the ported pressure formula's divisor (1024) gave tenths of a
bar, not bar -- corrected (and later converted to kPa, divisor 102.4).

`codes_test.txt`/`codes_test.json` cover all 24 frames, reconstructed
as on-air Manchester-encoded FSK_PCM bitstreams from the issue's
posted decoded payload bytes (no raw IQ was ever attached for this
device).

## Known accuracy gaps (decoder is enabled by default despite these)

- **Pressure**: 20/24 exact to the nearest 10 kPa, 24/24 within +-10 kPa.
  All 4 near-misses are biased low (never high), suggesting the 0x0e00
  offset constant is close but not perfectly calibrated -- not random
  noise, but not exact either.
- **Temperature**: 23/24 exact. The one miss is the single sample at a
  different ambient temperature (26 C vs the rest at 24 C), calculated
  as 25 C.
- **B3/B6**: not decoded. Per the issue thread, the real receiver
  rejects some CRC-valid artificial payloads that only vary these
  bytes, meaning they participate in some application-level state that
  wasn't solved.
- **No fixed per-sensor ID** has been identified.

One of the 24 codes also happens to pass `Watts-WFHTRF`'s own checksum
(`{224}aaaaaaaaaaaa669996a6aaa96655a95695a565656996a9a95559a9a5`, the
215/216 kPa reading) -- a normal cross-decoder false positive in the
other decoder, not a Sefis-M3 problem; Sefis-M3 still decodes it
correctly.
