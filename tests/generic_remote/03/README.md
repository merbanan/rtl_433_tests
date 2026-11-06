# PT2262/EV1527 doorbell button, TE ~214 us

Fixed code wireless doorbell button timing, base timing (TE) of about 214 us.

The signals are transmitted by a Flipper Zero (Princeton protocol) with made-up codes,
using the timing of a real doorbell button: TE 214 us, guard time 31 TE.
Recorded with an RTL-SDR at 433.92 MHz, 250 kHz, gain 10, three frames per file.

Measured: short pulse ~190 us, long pulse ~615 us, guard gap ~7780 us.

The default Generic-Remote range (TE 401-535 us) does not decode this,
it needs `conf/Generic-Remote-TE-ranges.conf` (Generic-Remote-TE180), named in `protocol`.

| File | Code | id | cmd |
|---|---|---|---|
| `code_a_433.92M_250k.cu8` | `9B4E5F` | 39758 | 95 |
| `code_b_433.92M_250k.cu8` | `6D21A7` | 27937 | 167 |

Flex decoder:

    rtl_433 -X 'n=pt2262_te214,m=OOK_PWM,s=243,l=728,r=1100,t=187,bits=25,invert'

Gives `{25}9b4e5f0` for `code_a`: the 24 bit code and the stop bit.
