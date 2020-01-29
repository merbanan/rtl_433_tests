# LaCross TX6U, TX7U Temperature and Humidity Sensors 433 Mhz

Captured signals for LaCrosse TX7U (and TX6U) 433 Mhz temperature and
humidity sensors which are sold in the U.S.

TX6U - Temperature only, no display
TX7U - Temperature and Humidity with LCD display of both.

This should also work for LaCrosse TX3U and TX4U which use the same
protocol, but haven't been tested.

Note: LaCrosse 915 Mhz TX sensors use a different protocol.

## Device Info

* Amazon Link - 
  http://www.amazon.com/dp/B0002NIL10
* Owner's Manual - https://www.lacrossetechnology.com/tx7/anual.pdf

## Protocol Documentation

A nice page documenting how to decode the protocol is available on
F6FBB's site.  http://www.f6fbb.org/domo/sensors/tx3_th.php 

## Device Notes

* Random Device ID - When the device is powered up (batteries are
  changed) it will generate a random ID byte that it will send with
  all transmissions.
* Messages are sent twice.
* Temperature and humidity are sent in a separate transmissions.

## Files

gfile001.data, TX7U, temperature
2015-06-30 12:20:54 LaCrosse TX Sensor 30: Temperature 20.5 C / 68.9 F

gfile002.data, TX7U, humidity
2015-06-30 12:21:02 LaCrosse TX Sensor 30: Humidity 31.0%


gfile006.data, TX6U, temperature, note different sensor ID.
2015-06-30 12:21:08 LaCrosse TX Sensor 7b: Temperature 20.4 C / 68.7 F

