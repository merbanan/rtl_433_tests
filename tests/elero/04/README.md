# Elero blind commands and motor replies

A LilyGO T-Embed and a Heltec WiFi LoRa 32 V4 received these packets during tests of one blind on channel 6. Each movement trial started and ended with the motor reporting the bottom position. The first eight test inputs retain the recorded payloads and counters. The device addresses are examples.

- An addressed Stop (counter 147) was followed by a Stopped reply. The motor used its own counter, 244, and copied 147 into header byte 6.
- Full Up and Full Down sent addressed command codes 33 and 65. A short press produced a selector packet with release code 0.
- Preset recall sent selector command 68. A later status request (counter 185) received a reply with state 3 (intermediate position) and request counter 185.

Header byte 6 matched the sending command counter in 14 complete status exchanges across ten receivers. In each exchange, the request counter differed from the channel number. The ninth input adds a second example destination to the Full Up packet to check the payload offset.

The hubs supplied packet bytes and two receiver quality bytes. The test inputs omit the quality bytes and reconstruct the radio checksum, whitening, and synchronization word for packet replay. The original Silent Gliss samples in the other directories test signal reception.

Run from the root of this repository with the decoder on the search path.

```sh
python3 bin/run_test.py -t tests/elero -I time
```
