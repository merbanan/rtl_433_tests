# X10 Power Control RF Devices

These signals are captured from an X10 RF "PalmPad" HR12A
which is used for controlling power over powerlines and RF.

The frequency is 310 Mhz.

The signal contains "B1 ON":
- House Code: B
- Unit 01
- Function: Turn On.

NOTE: The encoding is actually the common N.E.C. Infrared (IR) remote
control protocol that is sent over RF.

## rtl_433 status

Not currently supported as of June 2015.  There was some rudimentary
X10 decoding in an earlier version that seems to have been dropped.
That implementation was forcosed on X10 security sensors.

Previous settings:
* Short Limit: 150 (600 uS)
* Long Limit: 420 (1,680 uS)
* Reset Limit: 2500 (10,000 uS)

## Protocol Documentation

The protocol is documented in a number of places on-line.  It is
pulse position coded with a long "wake-up" pulse that confuses
rtl_433's -a mode.

See:
* http://davehouston.net/rf.htm
* http://www.homautomation.org/2014/04/25/how-to-decode-x10-rf-protocol/
* http://home.comcast.net/~ncherry/common/x10.rf.txt

