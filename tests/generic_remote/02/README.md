# PT2262/EV1527 remote, TE ~360 us

Fixed code 4-button gate remote timing, base timing (TE) of about 360 us.

The signals are transmitted by a Flipper Zero (Princeton protocol) with made-up codes,
using the timing of a real gate remote: TE 361 us, guard time 27 TE.
Recorded with an RTL-SDR at 433.92 MHz, 250 kHz, gain 10, three frames per file.

Measured: short pulse ~340 us, long pulse ~1065 us, guard gap ~10080 us.

The default Generic-Remote range (TE 401-535 us) does not decode this,
it needs `conf/Generic-Remote-TE-ranges.conf` (Generic-Remote-TE275), named in `protocol`.

| File | Code | id | cmd |
|---|---|---|---|
| `button_a_433.92M_250k.cu8` | `3A6C30` | 14956 | 48 |
| `button_b_433.92M_250k.cu8` | `3A6CC0` | 14956 | 192 |

Flex decoder:

    rtl_433 -X 'n=pt2262_te360,m=OOK_PWM,s=346,l=1037,r=1500,t=212,bits=25,invert'

Gives `{25}3a6c300` for `button_a`: the 24 bit code and the stop bit.
