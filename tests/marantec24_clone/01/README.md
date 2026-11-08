# Marantec24 clone remote

Not a Marantec protocol: a fixed code clone remote sold as a Marantec replacement, named
Marantec24 by the Flipper Zero firmware. Decoded by `Marantec24-Clone` (disabled by default,
`protocol` selects it).

PWM, 4000 us per bit: a 1 bit is an 800 us pulse and a 3200 us gap, a 0 bit is a 1600 us pulse
and a 2400 us gap. 24 bits (20 bit serial, 4 bit button), repeated after a 15200 us gap.
No integrity check.

Flipper Zero transmissions with made-up codes, recorded with an RTL-SDR at 433.92 MHz, 250 kHz,
RSSI about -12 dB, SNR about 24 dB.

| File | Key | id | button |
|---|---|---|---|
| `button_4_433.92M_250k.cu8` | `5B21E4` | 5B21E | 4 |
| `button_c_433.92M_250k.cu8` | `93A70C` | 93A70 | 12 |

Flex decoder:

    rtl_433 -X 'n=marantec24,m=OOK_PWM,s=800,l=1600,g=5000,r=20000,t=200,bits=24,repeats>=2'
