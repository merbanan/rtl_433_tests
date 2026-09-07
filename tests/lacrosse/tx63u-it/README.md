# La Crosse TX63U-IT wind sensor

La Crosse Technology TX63U-IT solar-powered wind sensor.

- Model: TX63U-IT
- FCC ID: OMO-M-12
- RF frequency: 924 MHz
- Manufacturer page: https://www.lacrossetechnology.com/products/tx63u-it
- FCC manual: https://fccid.io/OMO-M-12/User-Manual/Users-Manual-1332689
- Nominal transmission interval: about 17 seconds
- Wind range: 0 to 50 m/s
- Wind resolution: 0.1 m/s
- Gust resolution: 0.1 m/s
- Direction: 16 compass positions

## Captures

The captures were made from one physical TX63U-IT while the vane and cups were controlled or observed.
All five files below contain a frame that has been independently decoded and verified with CRC-16/X-25.

| File | Current wind | Current direction | Gust | Gust direction | Frame body including CRC |
| --- | ---: | --- | ---: | --- | --- |
| `north_calm_924M_1000k.cu8` | 0.0 m/s | N (0 deg) | 0.0 m/s | N | `3C C0 00 00 00 00 38 18 51` |
| `east_calm_924M_1000k.cu8` | 0.0 m/s | E (90 deg) | 0.0 m/s | E | `3C C0 40 00 40 00 38 4C 96` |
| `west_calm_924M_1000k.cu8` | 0.0 m/s | W (270 deg) | 0.0 m/s | W | `3C C0 C0 00 C0 00 38 F5 10` |
| `south_12.9ms_gust12.9ms_924M_1000k.cu8` | 12.9 m/s | S (180 deg) | 12.9 m/s | S | `3C C0 80 81 80 81 38 60 73` |
| `north_outdoor_lowwind_924M_250k.cu8` | 0.2 m/s | N (0 deg) | 0.6 m/s | N | `3C C0 00 02 00 06 38 BE 3C` |

The 250 ksample/s capture is a short excerpt from a normal outdoor installation and is intentionally included to test decoding at a common low RTL-SDR sample rate. The other captures are 1 Msample/s controlled captures.

## Reverse-engineered RF protocol

The RF burst is approximately 6.1 ms long and is phase-coded/BPSK-like at approximately 36 ksymbol/s. It does not behave as conventional OOK despite amplitude artifacts that can appear in pulse analysis.

After symbol recovery, differential decoding, and HDLC zero-bit de-stuffing, the logical frame is:

    7E 3C C0 D0 D1 D2 D3 38 CRClo CRChi 7E

`0x7E` is an HDLC-style flag. Bit stuffing follows HDLC rules: a zero is inserted after five consecutive one bits. Bytes are transmitted LSB-first.

The 9-byte de-stuffed body is:

    3C C0 D0 D1 D2 D3 38 CRClo CRChi

Observed field interpretation:

    current_direction = (D0 >> 4) & 0x0f
    current_speed_raw = ((D0 & 0x0f) << 8) | D1
    gust_direction    = (D2 >> 4) & 0x0f
    gust_speed_raw    = ((D2 & 0x0f) << 8) | D3

    current_speed_m_s = current_speed_raw / 10.0
    gust_speed_m_s    = gust_speed_raw / 10.0

Direction code mapping is ordinal clockwise:

    0=N, 1=NNE, 2=NE, 3=ENE,
    4=E, 5=ESE, 6=SE, 7=SSE,
    8=S, 9=SSW, 10=SW, 11=WSW,
    12=W, 13=WNW, 14=NW, 15=NNW

or `direction_degrees = direction_code * 22.5`.

`3C C0` is fixed in all captures from this sensor. `0x38` is also fixed in all captures observed so far. Their exact meanings are not yet known.

No unique sensor ID field has been established from captures of this single physical transmitter. A decoder should not invent an ID from an unverified constant field.

## Integrity check

CRC is CRC-16/X-25 (CRC-16/IBM-SDLC):

- width: 16
- polynomial: 0x1021 (reflected implementation 0x8408)
- init: 0xFFFF
- refin: true
- refout: true
- xorout: 0xFFFF
- CRC input: first seven body bytes, `3C C0 D0 D1 D2 D3 38`
- transmitted CRC order: low byte first

Example:

    data:     3C C0 00 00 00 00 38
    CRC:      0x5118
    on-air:   18 51

