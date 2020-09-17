# Example from one Situo 5 RTS Pure II device

In this example, we pressed the down button and shortly after additionally pressed the Up button. The signal was captured with an RTL-SDR and is clipped, however, it is still decoded correctly.

Below, you find the expected output. Using the Situo 5 RTS Pure II remote control, the seed for the scrambler consists of two nibbles (each four bits long). The left nibble is constant and set to 0xA, while the right nibble is cyclically increasing.

The counter is a replay protection counter. For a frame to be accepted by a receiver, the counter value needs to be higher than values of already received frames. For each remote control address, a separate counter is used.

The address is a unique idenitfier of a remote control's channel.

When buttons are pressed for a long time, frames will be retransmitted without changing the frame payload.

The signal is captured in `g015_433.414M_250k.cu8` and the decoders JSON output can be found in `g015_433.414M_250k.json`.


```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA8          Control   : Down (4)      Checksum  : 0x2           Counter   : 9             Address   : ABC437        Retransmission: FALSE     Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA8          Control   : Down (4)      Checksum  : 0x2           Counter   : 9             Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA8          Control   : Down (4)      Checksum  : 0x2           Counter   : 9             Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA9          Control   : Up + Down (6) Checksum  : 0x2           Counter   : 10            Address   : ABC437        Retransmission: FALSE     Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA9          Control   : Up + Down (6) Checksum  : 0x2           Counter   : 10            Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA9          Control   : Up + Down (6) Checksum  : 0x2           Counter   : 10            Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA9          Control   : Up + Down (6) Checksum  : 0x2           Counter   : 10            Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA9          Control   : Up + Down (6) Checksum  : 0x2           Counter   : 10            Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA9          Control   : Up + Down (6) Checksum  : 0x2           Counter   : 10            Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.325252s
model     : Somfy-RTS    Seed      : 0xA9          Control   : Up + Down (6) Checksum  : 0x2           Counter   : 10            Address   : ABC437        Retransmission: TRUE      Integrity : CHECKSUM
```

Here, is another capture from the same remote but with a different address. Additonally, the single low bit after the preamble is missing. The signal is captured in `g006_433.414M_250k.cu8` and the decoders JSON output can be found in `g006_433.414M_250k.json`.

```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.079260s
model     : Somfy-RTS    Seed      : 0xAF          Control   : Down (4)      Checksum  : 0x7           Counter   : 160           Address   : AAC437        Retransmission: FALSE     Integrity : CHECKSUM
pulse_demod_pcm(): Somfy RTS
bitbuffer:: Number of rows: 2 
[00] {20} ff ff 00                                              : 11111111 11111111 0000
[01] {140} f0 f0 ff 66 55 56 6a 56 6a 9a 6a 56 a6 a6 96 a9 a9 00 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.079260s
model     : Somfy-RTS    Seed      : 0xAF          Control   : Down (4)      Checksum  : 0x7           Counter   : 160           Address   : AAC437        Retransmission: TRUE      Integrity : CHECKSUM
pulse_demod_pcm(): Somfy RTS
bitbuffer:: Number of rows: 1 
[00] {180} f0 f0 f0 f0 f0 f0 f0 ff 66 55 56 6a 56 6a 9a 6a 56 a6 a6 96 a9 a9 00 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.079260s
model     : Somfy-RTS    Seed      : 0xAF          Control   : Down (4)      Checksum  : 0x7           Counter   : 160           Address   : AAC437        Retransmission: TRUE      Integrity : CHECKSUM
pulse_demod_pcm(): Somfy RTS
bitbuffer:: Number of rows: 1 
[00] {180} f0 f0 f0 f0 f0 f0 f0 ff 66 55 56 6a 56 6a 9a 6a 56 a6 a6 96 a9 a9 00 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.079260s
model     : Somfy-RTS    Seed      : 0xAF          Control   : Down (4)      Checksum  : 0x7           Counter   : 160           Address   : AAC437        Retransmission: TRUE      Integrity : CHECKSUM
pulse_demod_pcm(): Somfy RTS
bitbuffer:: Number of rows: 1 
[00] {180} f0 f0 f0 f0 f0 f0 f0 ff 66 55 56 6a 56 6a 9a 6a 56 a6 a6 96 a9 a9 00 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.079260s
model     : Somfy-RTS    Seed      : 0xAF          Control   : Down (4)      Checksum  : 0x7           Counter   : 160           Address   : AAC437        Retransmission: TRUE      Integrity : CHECKSUM
pulse_demod_pcm(): Somfy RTS
bitbuffer:: Number of rows: 1 
[00] {180} f0 f0 f0 f0 f0 f0 f0 ff 66 55 56 6a 56 6a 9a 6a 56 a6 a6 96 a9 a9 00 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : @0.079260s
model     : Somfy-RTS    Seed      : 0xAF          Control   : Down (4)      Checksum  : 0x7           Counter   : 160           Address   : AAC437        Retransmission: TRUE      Integrity : CHECKSUM
```
