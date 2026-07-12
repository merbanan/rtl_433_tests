# Fine Offset / Ecowitt WH52 — 3-in-1 soil sensor (moisture / temperature / EC)

Test captures for the Ecowitt **WH52** wireless soil probe, which reports soil
**moisture (%)**, soil **temperature**, and **electrical conductivity (EC, µS/cm)**.
It is a Fine Offset family device and shares the WH51's FSK/PCM modulation and
`aa2dd4` preamble, but uses a different family byte (`0xA2`) and a longer 24-byte
frame, so the existing WH51 decoder does not pick it up.

These are the captures used to develop a decoder for it. They are shared in the hope
they are useful to others; the notes below are what we observed and how we checked it,
not a definitive specification.

## Captures

US 915 MHz, sampled at 250 kHz (CU8). Four different physical units, deployed in soil,
recorded live off-air alongside the manufacturer gateway/app for ground truth. Each
file contains one WH52 transmission.

| file | id | moisture | temperature | EC | battery |
|---|---|---|---|---|---|
| `wh52_soil_nw_915M_250k.cu8` | 0058ac | 44 % | 20.4 °C | 107 µS/cm | ~1.56 V |
| `wh52_soil_ne_915M_250k.cu8` | 005b45 | 34 % | 21.0 °C | 26 µS/cm | ~1.58 V |
| `wh52_soil_sw_915M_250k.cu8` | 005cb5 | 25 % | 20.7 °C | 56 µS/cm | ~1.58 V |
| `wh52_soil_se_915M_250k.cu8` | 005995 | 36 % | 18.4 °C | 6 µS/cm | ~1.62 V |

The four units span a useful spread of moisture (25–44 %) and EC (6–107 µS/cm). All
four verify with the proposed decoder (`rtl_433 -r <file>`), and the decoded values
match the app readings.

## Signal / timing

- Modulation: FSK/PCM, ~58 µs bit period (NRZ), preamble `aa aa aa 2d d4`.
- Frame after the preamble: 24 bytes.
  `A2 II II II Bt tt MM .. Ec cc rr .. .. .. .. VV .. .. .. .. .. .. CC SS`
  - `A2` family byte; `II II II` 24-bit id.
  - temperature: `(((b4 & 0x1F)<<8) | b5) * 0.1 − 40 °C` (top 3 bits of b4 are a
    transmission/retry counter and must be masked).
  - moisture: byte 6, direct %.
  - EC (20-bit): `((b8 & 0x0F)<<16) | (b9<<8) | b10`; observed `µS/cm ≈ raw / 25.6`.
    This constant is an empirical fit from one unit over a stepped salt-water series
    and may need refinement.
  - byte 15 tracks battery voltage (`≈ b15 * 0.02 − 0.06`, approximate).
  - byte 22 CRC-8 (poly 0x31, init 0x00, over bytes 0–21); byte 23 = sum of bytes 0–22.
- Some bytes are not yet characterised; they appear constant per unit (likely a
  factory serial / calibration).

## Notes

Captured with the RTL-SDR **rtl_433 (next)** Home Assistant add-on by Peter (@pbkhrv,
github.com/pbkhrv/rtl_433-hass-addons) — thanks to him for making off-air capture
straightforward. And thanks to Benjamin Larsson (@merbanan) and the rtl_433 contributors
for the tool this builds on. Corrections and improvements very welcome.
