# Curv360 kinetic (self-powered) wireless light switches

https://www.curv360.com/product/wireless-light-switches/

See https://github.com/merbanan/rtl_433/issues/1790.

OOK PWM, 28-bit fixed code per button, no pairing/negotiation -- these are
self-powered kinetic switches with no battery or MCU, so the same fixed
code is sent every press. The top 20 bits are a per-switch-unit id, the
bottom 8 bits vary by button and on/off state.

Decoded with `conf/Curv.conf` (`decoder { n=Curv, m=OOK_PWM, s=40, l=100,
r=1200, g=120, t=20, bits=28, unique, get=id:@0:{20}:%05x,
get=cmd:@20:{8}:%02x }`), found by @zuckschwerdt and refined by
@merbanan in the issue thread. @lukestirk's own manual analysis in the
thread documented the full button map for both of his switch units,
confirmed working for real-world retransmission by @skeere with an
ESP32/RMT sample.

## Captures in this directory

Both are the same physical button ("living room 2" on one of @lukestirk's
two-gang switches, id `0d1bb`), captured twice -- once for the on press,
once for the off press. 2 more repeats of the same 2 readings
(`g011`/`g012`) are in the original issue attachment if more samples are
needed.

| File | id | cmd |
|------|----|-----|
| `g009_433.592M_1024k.cu8` | `0d1bb` (53691) | `41` (65) -- on |
| `g010_433.592M_1024k.cu8` | `0d1bb` (53691) | `21` (33) -- off |
