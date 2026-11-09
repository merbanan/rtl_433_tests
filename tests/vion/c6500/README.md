# Vion C6500 wind sensor

Outdoor wind sensor (cup anemometer + wind vane) of the Vion C6500 weather station.
The console displays wind speed and direction in three modes: instant, gust and average.
All three are transmitted in every message.

- Frequency: ~434.21 MHz (measured; the console is sold as 433 MHz)
- Modulation: OOK PWM, short 142 us, long 278 us, sync 414 us
- 82 bits every ~14.4 s, each message sent twice

A flex decoder is available as `conf/Vion-C6500.conf` in rtl_433.

- [01](01/) — samples from one unit
