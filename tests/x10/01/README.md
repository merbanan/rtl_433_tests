# X10 Power Control RF Devices

These signals are captured from an X10 RF "PalmPad" HR12A
which is used for controlling power over powerlines and RF.

The frequency is 310 Mhz.

The signal contains "B1 ON":
- House Code: B
- Unit 01
- Function: Turn On.

Another signal contains "B DIM":
- House Code: B
- Unit 00 (invalid) - no unit for dim and bright commands
- Function: Dim.

NOTE: The encoding is actually the common N.E.C. Infrared (IR) remote
control protocol that is sent over RF.

## rtl_433 status

Implementation is complete, but operation is not exactly reliable.
It seems these devices have abysmal signals, full of noise and side bands.
Another implementation is focused on X10 security sensors.

Previous settings:
* Short Limit: 150 (600 uS)
* Long Limit: 420 (1,680 uS)
* Reset Limit: 2500 (10,000 uS)

## Protocol Documentation

The protocol is documented in a number of places on-line.  It is
pulse position coded with a long "wake-up" pulse that confuses
rtl_433's -a mode.

See:
* https://www.linuxha.com/athome/common/x10.rf.html
* http://www.wgldesigns.com/protocols/w800rf32_protocol.txt


