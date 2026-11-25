# Hormann BiSecur samples

Flipper Zero transmissions (Hormann BiSecur protocol, sent by the Flipper Zero encoder from key
files) with made-up serials and random encrypted bytes, valid CRC, recorded with an RTL-SDR at
868.276 MHz, 250 kHz, FSK, RSSI about -9.5 dB, SNR 28 dB. The decoder is enabled by default.

| File | Type | Serial (id) | Encrypted |
|---|---|---|---|
| `bisecur_50_a1b2c3d4_868.276M_250k.cu8` | `0x50` | `a1b2c3d4` | `9f41bd5bcbb0f1d7bda6ec8707d777c6` |
| `bisecur_70_0badf00d_868.276M_250k.cu8` | `0x70` | `0badf00d` | `f13fa60de6281c5f78de3f618b1a923f` |
