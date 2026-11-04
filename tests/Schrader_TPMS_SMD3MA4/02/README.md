# Schrader/Nissan-Infiniti MRXNIS315G3 (aka Redi-Sensor SE10001HP/SE10001HPR)

Two confirmed-good captures of the Schrader "3039" OEM sensor used on Nissan,
Infiniti and Renault vehicles (also sold as the Continental/Redi-Sensor
aftermarket replacement SE10001HP/SE10001HPR). It transmits the *identical*
wire format, preamble and timing as the Subaru-fit `../01/` SMD3MA4 captures,
which is exactly the point of including it here -- see
`../README.md` for the pressure-scaling discrepancy this causes.

Captured by @robcazzaro in
https://github.com/merbanan/rtl_433/issues/1734#issuecomment-861656696,
using the sensors' "learn" trigger (flags == 0, `learn` field set). Each
file contains one confirmed sensor, ID-matched against the serial number
printed on the physical sensor body (the printed serial is 32-bit, e.g.
`0CCEDE23`; only the low 24 bits are actually transmitted over the air):

| File                             | id     | printed serial |
|----------------------------------|--------|-----------------|
| `CEDE23_learn_315M_250k.cu8`     | CEDE23 | 0CCEDE23        |
| `D6136D_learn_315M_250k.cu8`     | D6136D | 0CD6136D        |

Two more sensors from the same batch (`820900` / printed `0C820900` and
`D004E2` / printed `0CD004E2`) were also captured but aren't included here;
see the issue thread if more samples are needed.
