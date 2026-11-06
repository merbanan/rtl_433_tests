# Marantec, 868.35 MHz

Flipper Zero transmission with a made-up code, recorded with an RTL-SDR at 868.35 MHz, 1024 kHz.
Nothing was received at 250 kHz.

The signal is clipped (RSSI +1.3 dB): with the Flipper about 3 m away there was no gain setting
between nothing received and a clipped signal.

The Flipper's OOK carrier at 868 MHz moves by about 15 kHz between pulses. With any FSK decoder
enabled (e.g. the default Danfoss CFR) the pulse detector takes this sample as FSK, so `protocol`
selects the Marantec decoder only. Live reception with the default decoders did decode it.

| File | Key | id | button |
|---|---|---|---|
| `button_1_868.35M_1024k.cu8` | `1305A3C118697` | 5A3C186 | 1 |
