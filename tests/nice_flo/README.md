# Nice FLO fixed code gate remotes

E.g. Nice FLO2, FLO4, 433.92 MHz. PWM coded with a base time of 700 us: each bit is a gap and a
pulse, a 1 bit is a 1400 us gap and a 700 us pulse, a 0 bit is a 700 us gap and a 1400 us pulse.
A message is a 700 us start pulse and a 12 or 24 bit code, repeated after a 25 ms gap.
No integrity check, the decoder is disabled by default.

The Nice FloR-S rolling code remotes are a different protocol (`nice_flor_s`).

Flex decoder:

    rtl_433 -X 'n=nice_flo,m=OOK_PWM,s=700,l=1400,g=3000,r=30000,t=150'
