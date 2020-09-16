# Example from one Situo 5 RTS Pure II device

In this example, we pressed the down button and shortly after additionally pressed the Up button. The signal was captured with an RTL-SDR and is clipped, however, it is still decoded correctly.

Below, you find the expected output. Using the Situo 5 RTS Pure II remote control, the random number used as seed for the scrambler consists of two nibbles (each four bits long). The left nibble is constant and set to 0xA, while the right nibble is cyclically increasing (168 = 0xA8, 169 = 0xA9). Hence, it is actually not random but quite deterministic.

The counter is a replay protection counter. For a frame to be accepted by a receiver, the counter value needs to be higher than values of already received frames. For each remote control address, a separate counter is used.

The address is a unique idenitfier of a remote control's channel.

When buttons are pressed for a long time, frames will be retransmitted without changing the frame payload.

The signal is captured in `g015_433.414M_250k.cu8` and the decoders JSON output can be found in `g015_433.414M_250k.json`.


```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 168           Control   : Down (4)      Checksum  : OK            Counter   : 9             Address   : abc437        Retransmission: FALSE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 168           Control   : Down (4)      Checksum  : OK            Counter   : 9             Address   : abc437        Retransmission: TRUE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 168           Control   : Down (4)      Checksum  : OK            Counter   : 9             Address   : abc437        Retransmission: TRUE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 169           Control   : Up + Down (6) Checksum  : OK            Counter   : 10            Address   : abc437        Retransmission: FALSE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 169           Control   : Up + Down (6) Checksum  : OK            Counter   : 10            Address   : abc437        Retransmission: TRUE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 169           Control   : Up + Down (6) Checksum  : OK            Counter   : 10            Address   : abc437        Retransmission: TRUE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 169           Control   : Up + Down (6) Checksum  : OK            Counter   : 10            Address   : abc437        Retransmission: TRUE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 169           Control   : Up + Down (6) Checksum  : OK            Counter   : 10            Address   : abc437        Retransmission: TRUE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 169           Control   : Up + Down (6) Checksum  : OK            Counter   : 10            Address   : abc437        Retransmission: TRUE
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : @0.325252s
model     : Somfy-RTS    Random    : 169           Control   : Up + Down (6) Checksum  : OK            Counter   : 10            Address   : abc437        Retransmission: TRUE
```
