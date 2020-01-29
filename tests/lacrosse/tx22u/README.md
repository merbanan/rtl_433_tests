# LaCross TX22U 915 Mhz Temperature and Humidity Sensor

The LaCrosse TX22U and presumably other, newer, 915 Mhz sensors use a
different protocol than the 433 Mhz sensors.  The TX22U is sold in
the US.

As of June 2015, these aren't supposed in rtl_433, yet.

This device may use Frequency hopping between 910, 915, and 920 Mhz.

The modulation may be FSK, rather than the OOK that rtl_433 currently
is capable of decoding.

## Device Info

* Product manual: https://www.lacrossetechnology.com/tx22/manual.pdf
* Amazon page: http://www.amazon.com/dp/B0016N2HCO
* FCC ID: OMO TX22U

## Possible Protocol Information from the net

From http://nikseresht.com/blog/?p=99
* Might be a bit rate of 8.621 Kbps
* Varying frame length, up to 13 bytes, starts with an "A".

http://www.g-romahn.de/ws1600/Datepakete_raw.txt

