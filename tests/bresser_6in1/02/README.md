# Ambient Weather TX-3107 (Bresser 6-in-1 protocol)

US 915 MHz pool / spa thermometer sold as **Ambient Weather TX-3107**
(<https://www.ambientweather.com/amtx3107.html>). It is a rebranded
Bresser / Fine Offset "6-in-1" device and is decoded by the existing
`Bresser-6in1` decoder (protocol 172) as **sensor type 3 (pool thermometer)**.

Originally requested in rtl_433 issue
[#1424](https://github.com/merbanan/rtl_433/issues/1424). The samples there were
captured at ~76 bits, which only covered the digest + id + channel and not the
temperature bytes, so the temperature appeared "scrambled". The full packet
carries the temperature as plain BCD.

## Capture

- FSK PCM, ~120 us bit width, preamble `aa..`, sync `2dd4`, 915 MHz.
- `g022_915M_1000k.cu8` is from the issue's `amtx3107_cu8+ook.zip` sample set
  (`g023`/`g024` are identical captures of the same reading).

## Decoded

    Bresser-6in1  id 0x18701c9b  channel 7  31.6 C  (sensor_type 3, pool)

## Packet (18 bytes after the 2dd4 sync)

    09 d4 | 18 70 1c 9b | 3f | 00 00 00 00 00 | 31 60 | 00 | 00 00 f0
    digest|     id      | T/C/start           |  temp | hum|

- `msg[0..1]`   digest, `lfsr_digest16(msg[2..16], 0x8810, 0x5412)`
- `msg[2..5]`   id `0x18701c9b`
- `msg[6]`      `0x3f` -> sensor_type 3, startup 1, channel 7
- `msg[12..13]` `31 60` -> temperature 31.6 C (BCD)
- `msg[14]`     humidity (unused on this sensor)
