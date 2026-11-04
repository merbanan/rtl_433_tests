# Cheap EV1527 based PIR sensor

EV1527 based devices are supported (at least?) in the _Generic remote_ [30] and _Wireless Smoke and Heat Detector GS 558 protocol_ [86]

I've now picked up some EV1527 based PIR from brand _SGOOWAY_ model _PR2_. This one is detected as 

```
time      : 2019-06-05 14:06:02
model     : Smoke detector GS 558                  id        : 11148
unit      : 19           learn     : 0             Raw Code  : 357193

```

Not that bad at the first try. But the reception is quite poor. Just one wall in between the sender and the rtl_sdr breaks the "connection".
This has been tested with two different rtl-sdr sticks and two different antennas (one dedicated 433MHz antenna and one DVB-T antenna which came with one of the radio sticks).

A lot of other 433MHz sensors (Oregon, Alecto, Globaltronic) can be received from other floors (even from within a fridge downstairs ;-).

I'm going to provide new samples for it to help improving its reception/decoding.
Folder /01 contains some samples.

btw.: Similar thing has been dealed with at:
https://github.com/merbanan/rtl_433/issues/663
