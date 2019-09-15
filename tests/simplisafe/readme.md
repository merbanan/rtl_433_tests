# Simplisafe Home Security

Simplisafe Home Security sensors transmit using Pulse Interval
and Width Modulation (PIWM) on 433.92 MHz. Manufacturer website
is https://simplisafe.com/

Some description is at:
 - https://greatscottgadgets.com/2016/02-19-low-cost-simplisafe-attacks/

Unlike most modulations the total duration of transmission
depends on the value of bits. The bits are encoded into distance
between edges (short pulse/gap represent 0, long pulse/gap represents 1).

Update: 5/16/2018:
Additional information related to the security advisory disclosure can be read at 
https://www.simpleorsecure.net/ on or after 5/17/2018

The KeyPad transmissions require you to disable automatic gain in order for the SDR 
to receive the signal properly.

You'll note the KeyChain is indistinguishable from a normal sensor except when the
Alarm Off button is selected.
