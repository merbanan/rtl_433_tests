# Roger Technology fixed code gate remotes

433.92 MHz, PWM coded with a base time of 500 us: a 1 bit is a 1000 us pulse and a 500 us gap,
a 0 bit is a 500 us pulse and a 1000 us gap. Each message is 28 bits followed by a 9.5 ms gap:
16 bit serial, 4 bit button (one bit per button), 8 bit end code (usually the button again,
0x20 or 0x23 seen on some remotes). No integrity check. Decoded with `conf/Roger.conf`.
