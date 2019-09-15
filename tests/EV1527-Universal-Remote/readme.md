# EV1527 4-button universal remote

This folder contains sample recordings from _two_ *EV1527-based key fob universal remote*s.
For both, a sequence of pressing `A`, `B`, `C` and `D` has been recorded.

The sample files are:
```
remote#1-pressed-A g016_433.92M_250k.cu8
remote#1-pressed-B g016_433.92M_250k.cu8
remote#1-pressed-C g016_433.92M_250k.cu8
remote#1-pressed-D g016_433.92M_250k.cu8

remote#2-pressed-A g016_433.92M_250k.cu8
remote#2-pressed-B g016_433.92M_250k.cu8
remote#2-pressed-C g016_433.92M_250k.cu8
remote#2-pressed-D g016_433.92M_250k.cu8
```

The decoder for the EV1527 based smoke detector get the following for the same sequence of `A`, `B`, `C` and `D` as above:

```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : 2019-06-24 15:46:21
model     : Smoke detector GS 558                  id        : 3148
unit      : 10           learn     : 0             Raw Code  : 81898a
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
time      : 2019-06-24 15:46:26
model     : Smoke detector GS 558                  id        : 3148
unit      : 10           learn     : 0             Raw Code  : 41898a
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : 2019-06-24 15:46:27
model     : Smoke detector GS 558                  id        : 3148
unit      : 10           learn     : 0             Raw Code  : 21898a
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : 2019-06-24 15:46:36
model     : Smoke detector GS 558                  id        : 3148
unit      : 10           learn     : 0             Raw Code  : 11898a
```
The first digit of the `Raw Code` shows the pressed EV1527-data-bit value (A=bit3, B=bit2, C=bit1, D=bit0).
Pressing two (or even more) buttons at the same time is possible. While two buttons pressed at the same time seems to be useful, more than two is hardly possible because of the size of the remote and the separators between the buttons. 
At least I managed pressing three at a time ;-)

Anyway, if implementing it as a protocol, adding the four bits would make sense IMHO.

For example `A`+`C` = `8+2=0xa`:

```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : 2019-06-24 15:57:08
model     : Smoke detector GS 558                  id        : 3148
unit      : 10           learn     : 0             Raw Code  : a1898a
```

Btw.: The `D` is sometimes detected as:

```
time      : 2019-06-24 15:50:17
model     : Akhan 100F14 remote keyless entry      ID (20bit): 0x6f3cb
Data (4bit): 0x8 (Alarm)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : 2019-06-24 15:50:17
model     : Akhan 100F14 remote keyless entry      ID (20bit): 0x6f3cb
Data (4bit): 0x8 (Alarm)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
time      : 2019-06-24 15:50:17
model     : Akhan 100F14 remote keyless entry      ID (20bit): 0x6f3cb
Data (4bit): 0x8 (Alarm)
```
