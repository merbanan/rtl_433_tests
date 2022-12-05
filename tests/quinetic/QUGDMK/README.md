# Quinetic QUGDMK

The Quinetic series includes 433Mhz RF push-switches and receivers (e.g. Smart Plug, Lighting Relay, Lighting Dimmer).

* Grid-style switch for use in MK Grid Panels.
* Self-powered, momentary push style.
* Supports hold-and-release to perform dimming on a compatible receiver.

## Switch Info

* When "pushed" the switch generates 3 signals, sending the payload multiple times for redundancy.
* When "released" the switch generates 3 signals, sending the payload multiple times for redundancy.
* A fourth signal is sometimes generated, usually a partial packet.

## RF Signal Info

* Nominal pulse width: 10us @ 2048k sample rate.
* Modulation: FSK, PCM, NRZ.
* Approximate package size: 80bits.

## Flex Decoder

```
rtl_433 -s 2048000 -R 0 -Y minmax -c ./quinetic_switch.conf -r <FILE>
```
