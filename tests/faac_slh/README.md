# FAAC SLH rolling code gate remotes

E.g. FAAC XT2/XT4 SLH, 433.92 MHz and 868.35 MHz. Each message is a 1190 us pulse and a
1190 us gap, then 64 bits PWM coded: a 1 bit is a 595 us pulse and a 255 us gap, a 0 bit is a
255 us pulse and a 595 us gap. Messages are repeated back to back.

The high 32 bits are the fixed part (28 bit serial, 4 bit button), the low 32 bits are
encrypted (KeeLoq with a key derived from a per remote seed). A master remote in programming
mode sends the seed instead (fixed part starting with 0x520f, low byte of the encrypted part 0).
No integrity check, the decoder is disabled by default.

Flex decoder:

    rtl_433 -X 'n=faac_slh,m=OOK_PWM,s=255,l=595,r=3000,t=100,bits=64,invert,repeats>=2'
