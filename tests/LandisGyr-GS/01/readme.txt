Landis & Gyr GridStream (LandisGyr-GS)
======================================

Two real off-air captures of the Landis & Gyr GridStream sub-GHz AMI mesh
(Puget Sound Energy deployment, 902-928 MHz ISM band) for the gridstream
decoder in src/devices/gridstream.c (rtl_433 protocols 271/272/273).

Samples
-------
  g001_903.2M_250k.cu8   subtype 0x55 / CI 0x30   broadcast beacon
  g002_908.9M_250k.cu8   subtype 0xD2 / CI 0x52   encrypted directed (AES-256)

g002 exercises the pre-CRC detection of the encrypted frame type: the decoder
emits encrypted=1 with no CRC check, because the frame trailer is an AEAD
authentication tag rather than the CRC-16 the plaintext families carry.

Decode
------
These frames are GFSK and only slice with the min-max FSK detector. The default
detector does not pick them up, so -Y minmax is required:

  rtl_433 -r tests/LandisGyr-GS/01/g001_903.2M_250k.cu8 -Y minmax -M level

Because bin/run_test.py invokes rtl_433 without -Y minmax, there is no expected-
output .json here (the harness skips sample dirs that have no .json, the same as
tests/Neptune-R900/01).

Provenance
----------
Received with an AirSpy R2 at 908 MHz center / 10 MSPS, then frequency-translated
to the narrow channel of each frame and decimated to 250 kSPS (GridStream is
FHSS). These are real captures, not synthetic.

Privacy
-------
GridStream LAN addresses are device identifiers. g001 is a broadcast beacon from
a meter belonging to the capturer (destaddress = broadcast; only that one LAN ID
appears). g002 is encrypted and carries no addressing on the wire. No third-party
meter identifiers are present in these samples.
