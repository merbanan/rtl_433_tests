# Apollo Ultrasonic Smart

The code fixtures are demodulated packets posted in
[rtl_433 issue #3533](https://github.com/merbanan/rtl_433/issues/3533) from an
Apollo Smart purchased in 2025. They were recorded with the sensor nominally
40 cm, 50 cm, and 60 cm from the target.

After the `555558` outer preamble/desynchronizer, each packet contains a
64-bit Manchester-coded payload. The decoded payloads are:

| Nominal distance | Payload | Decoded depth |
| --- | --- | --- |
| 40 cm | `5b7b7181565e28fc` | 40 cm |
| 50 cm | `5b7b7181565e3341` | 51 cm |
| 60 cm | `5b7b7181565e3c00` | 60 cm |

All three payloads pass the protocol's reflected CRC-8 (`poly=0x31`,
`init=0x00`). The one-centimetre difference in the middle sample is present in
the transmitted payload and is consistent with measurement resolution; it is
not a decoder alignment error.

These packets also exercise sensor IDs that do not start with `5558`. That
guards the fix in rtl_433 commit `3ca23d5a`, which removed the incorrect
assumption that the first two decoded payload bytes were an inner preamble.
They are the high half of the 32-bit sensor ID instead.
