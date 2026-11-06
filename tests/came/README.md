# CAME gate remotes (also Prastel, Airforce)

Fixed code PWM remotes on 433.92 MHz, base time 320 us. Each bit is a gap and a pulse:
a 1 bit is a 640 us gap and a 320 us pulse, a 0 bit is a 320 us gap and a 640 us pulse.
A message is a 320 us start pulse and a 12, 18 (Airforce), 24, 25 or 42 (Prastel) bit code,
repeated after a 5 to 25 ms gap. No integrity check, the decoder is disabled by default.

Flex decoder:

    rtl_433 -X 'n=came,m=OOK_PWM,s=320,l=640,g=2000,r=30000,t=150'
