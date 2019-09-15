# DSC 433 Mhz Security Contacts

Recording of a DSC (Digital Security Controls) door/window security
contact Model: for an alarm system.  433 Mhz used with Power Series
and Alexor security systems.  The same protocol is used by many
other 433 mhz contacts (sensors) from DSC.

## Product Info

* Manufacturer Page: http://www.dsc.com/index.php?n=products&o=view&id=113
* Amazon Page: http://www.amazon.com/B000V9XTBM

## Protocol Information

The FCC ID is F5300NB912, the report actually includes
the protocol information.

https://apps.fcc.gov/eas/GetApplicationAttachment.html?id=100988

## Unusual On Off Keying (OOK) Protocol

These devices use a slightly unusual On-Off Keying scheme presumably
to save power.  Nothing is sent during zero bits.   If there are
multiple zero bits, there a long periods of silence. 

Packets are 26.5 mS long

* Packets start with 2.5 mS of constant modulation
* The period of a bit is 500 uS, broken into two 250 uS segments.
* A logic 0 is 500 uS (2 x 250 uS) of no signal.
* A logic 1 is 250 uS of no signal followed by 250 uS of  signal/keying
* After the wake-up pulse there are 4 sync logic 1 bits.
* There is a sync/start 1 bit in between every 8 bits.

A zero byte would be 8 x 500 uS of no signal (plus the 250 uS of
silence for the first half of the next 1 bit) for a maximum total of
4,250 uS (4.25 mS) of silence. 

The last byte is a CRC with nothing after it, no stop/sync bit, so
if there was a CRC byte of 0, the packet would wind up being short
by 4 mS. 

There are 48 bits in the packet including the leading 4 sync 1
bits. This makes the packet 48 x 500 uS bits long plus the 2.5 mS
preamble for a total packet length of 26.5 ms.

## rtl_433 Status

As of June 2015, this isn't currently decoded by rtl_433, a custom
demodulator needs to be written.  I (rct) am ready to implement this
but was waiting for the updated, more flexible plug-in / demodulator
architecture.

