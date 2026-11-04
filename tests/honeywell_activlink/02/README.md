# Honeywell "ActivLink" Wireless Chimes

North American variants of this device operate at 916.8 MHz FSK 50kHz deviation. Australian variants are also reported to use this same frequency.

European variants seem to operate at or near 868 MHz, thought I haven't personally tested
these systems.  However, their data frame seems to be the same format.

[There's some](https://livewell.honeywellhome.com/en/support/alarm-support/) [indication](https://livewell.honeywellhome.com/en/support/alarm-support/) that this protocol may be based on the Friedland / Response 868MHz alarm system.  [This FAQ](https://livewell.honeywellhome.com/en/support/doorbell-support/) 
indicates that the 868MHz variants of the Honeywell ActivLink system is compatible 
with the Friedland Libra+ Wirefree Doorbell system.  [An IQ sample from this system](https://www.sigidwiki.com/wiki/Friedland_Libra%2B_48249SL_wireless_doorbell) is available at the [Signal Identification Guide wiki](https://www.sigidwiki.com/wiki/Signal_Identification_Guide) and should be analyzed further.

Data below applies to the 916.8 MHz systems I've tested and and signal submissions I've
been able to review.  If you'd like to get in touch with me to 
[submit data from your Honeywell device](https://goo.gl/forms/SuxA3qgVRivXmNMf1), I'd
like to hear from you.

Modulation rate seems to be 6250 baud, so each HIGH or LOW symbol is 160 μs.

Data bits are encoded over three symbols. A "0" bit is defined as HIGH-LOW-LOW,
and a "1" bit is defined as "HIGH-HIGH-LOW".

Each frame of data consists of a LOW-LOW-LOW signal preamble, 48 bits (144 
symbols) of data, and a postamble of HIGH-HIGH-HIGH.

The signal seems to be 50 consecutive repetitions of the frame, then symbols
LOW-LOW-LOW-HIGH-HIGH-HIGH, and finally 2 continuous milliseconds (2000 μs) of
LOW.

Each data frame is 48 bits, or 6 bytes long.  From experimentation and from
the signals I've collected so far, this seems to be how bits are being used.

	# Frame bits used in Honeywell RCWL300A, RCWL330A, Series 3, 5, 9 and all Decor Series Wireless Chimes
	# 0000 0000 1111 1111 2222 2222 3333 3333 4444 4444 5555 5555
	# 7654 3210 7654 3210 7654 3210 7654 3210 7654 3210 7654 3210
	# XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XXXX XX.. XXX. .... KEY DATA (any change and receiver doesn't seem to recognize signal)
	# XXXX XXXX XXXX XXXX XXXX .... .... .... .... .... .... .... KEY ID (different for each transmitter)
	# .... .... .... .... .... 0000 00.. 0000 0000 00.. 000. .... KEY UNKNOWN 0 (always 0 in devices I've seen)
	# .... .... .... .... .... .... ..XX .... .... .... .... .... DEVICE TYPE (10 = doorbell, 01 = PIR Motion sensor)
	# .... .... .... .... .... .... .... .... .... ..XX ...X XXX. FLAG DATA (may be modified for possible effects on receiver)
	# .... .... .... .... .... .... .... .... .... ..XX .... .... ALERT (00 = normal, 01 or 10 = right-left halo light pattern, 11 = full volume alarm)
	# .... .... .... .... .... .... .... .... .... .... ...X .... SECRET KNOCK (0 = default, 1 if doorbell is pressed 3x rapidly)
	# .... .... .... .... .... .... .... .... .... .... .... X... RELAY (1 if signal is a retransmission of a received transmission, only some models)
	# .... .... .... .... .... .... .... .... .... .... .... .X.. FLAG UNKNOWN (0 = default, but 1 is accepted and I don't observe any effects)
	# .... .... .... .... .... .... .... .... .... .... .... ..X. LOWBAT (1 if battery is low, receiver gives low battery alert)
	# .... .... .... .... .... .... .... .... .... .... .... ...X PARITY (LSB of count of set bits in previous 47 bits)

## Data Frame Device ID Notes:
For simplicity, the full Device ID for the device might just be the first 
4 bytes.  Device Type should be included as part of the Device ID since if 
it is changed, a receiver would no longer recognize the signal as being from 
the same device.  Bits after byte 4 that seem to be part of the Key ID are
always 0 on all devices I've seen.

## Data Frame KEY UNKNOWN 0 Notes:
These bits are 0 in all devices I've seen.  Some preliminary tests with
generating artificial signals seems to indicate that if these bits are not
0, the receiver does not seem to recognize the signal as a previously
recognized device.  So, these bits are either part of the device ID, or they
simply must be 0 for the receiver to accept the signal as valid.  Further
testing here is required.

## Data Frame DEVICE TYPE Notes:
For all devices I've tested, it seems that only the two bits specified for this
field change depending on the type of device used to generate the signal.
It seems logical that perhaps the the width of this field is more than two
bits.  It might even be all of the 4th byte.  I have no data to confirm this, 
though.  For all devices I've seen, though, only these two bits of the 4th 
byte might be anything other than 0.

## Data Frame ALERT Notes:
On some receivers, such as the Honeywell RDWL917AX, an alert type of 01 or
10 forces the receiver to display a blinking right and left pattern, instead
of the normal full perimeter LED blinking.

## Data Frame RELAY Notes:
On some receiver models, such as the "Honeywell RDWL917AX", the base receiver 
will immediately retransmit a valid received signal if the RELAY bit is NOT 
set. The data in the retransmitted signal will be modified with the RELAY bit 
set. This seems to be an effort to extend a signal to more distant receivers.

## Devices using this signal
Here's an incomplete list of devices and kits known or suspected to use this signal.

### North American models
- RCA902N1004/N Wireless Motion Detector
- RDWL311A 3 Series Portable Wireless Doorbell & Push Button
- RDWL313A 3 Series Portable Wireless Doorbell with Strobe Light & Push Button
- RDWL313P 3 Series Plug-In Wireless Doorbell with Strobe Light & Push Button
- RDWL515A2000/E 5 Series Portable Wireless Doorbell with Halo Light & Push Button
- RDWL515P 5 Series Plug-In Wireless Doorbell with Halo Light & Push Button
- RDWL515A2000/E Portable Wireless Doorbell with Halo Light and Push Button 2 Pack
- RDWL917AX2000/E Series 9 Portable Wireless Doorbell / Door Chime & Push Button
- RCWL251A1005 Décor Door Chime & Push Button
- RPWL300A Decor Wireless Push Button
- RPWL302A1005/A Decor Wireless Surface Mount Push Button for Door Chime
- RPWL4045A Wired to Wireless Doorbell Adapter Converter for Series 3, 5, 9 Honeywell Door Bells
- RPWL401B Wireless Doorbell Push Button for Series 3, 5, 9 Honeywell Door Bells (Black)
- RPWL401B2000/A Wireless Surface Mount Push Button
- RPWL400W Wireless Doorbell Push Button for Series 3, 5, 9 Honeywell Door Bells (White)
- RPWL400W2000/A Series 3, 5, 9 Wireless Doorbell Push Button with Halo Light
- RPWL4045A2000 Wired to Wireless Doorbell Adapter for Series 3, 5, 9
- RCWL330A1000/N P4-Premium Portable Wireless Doorbell / Door Chime and Push Button
- RCWL35 Series, includes RCWL35N, RCWL3501A, RCWL3502A, RCWL3503A, RCWL3504A, RCWL3505A, RCWL3506A
- RCWL3501A1004/N Decor Wireless Door Chime
- RCWL3502A1002/N Decor Wireless Door Chime
- RCWL3503A1000/N Decor Wireless Door Chime
- RCWL3504A1008/N Decor Wireless Door Chime
- RCWL3505A1005/N Decor Customizable Wood Wireless Doorbell / Door Chime and Push Button
- RCWL3506A1003/N Decor Wireless Door Chime

### Australian models (916.8 MHz)
- DC917NGA Wireless portable MP3 doorbell with range extender, customisable melodies and push button – Grey
- DC515NA Wireless portable doorbell with halo light, sleep mode and push button – White
- DC515NGA Wireless portable doorbell with halo light, sleep mode and push button – Grey
- DC515NP2A Wireless plug-in doorbell with sleep mode, nightlight and push button – White
- DC515NGP2A Wireless plug-in doorbell with sleep mode, nightlight and push button – Grey
- DC313NA Wireless portable doorbell with volume control and push button – White
- DC313NGA Wireless portable doorbell with volume control and push button – Grey
- DCP311GA Wireless push button with LED confidence light – Portrait, Grey
- DCP511A Wireless push button with nameplate and LED confidence light – Offset Landscape, White
- DCP511GA Wireless push button with nameplate and LED confidence light – Offset Landscape, Grey

### European models

- DW915SG Wired and wireless doorbell with range extender, sleep mode and halo light – Grey
- DW915S Wired and wireless doorbell with range extender, sleep mode and halo light – White
- DC917SL Wireless portable doorbell with range extender, customisable melodies and push button – White
- DC917SG Wireless portable doorbell with range extender, customisable melodies and push button – Grey
- DC917NG Wireless portable doorbell with range extender, customisable melodies and push button – Grey
- DC915SG Wireless portable doorbell with range extender, sleep mode and push button – Grey
- DC915SEA Wireless portable doorbell with range extender, wireless motion sensor and push button – White
- DC915SCV Wireless portable doorbell with range extender, sleep mode and wired to wireless converter – White
- DC915S Wireless portable doorbell with range extender, sleep mode and push button – White
- DC915NG Wireless portable doorbell with range extender, sleep mode and push button – Grey
- DC915N Wireless portable doorbell with range extender, sleep mode and push button – White
- DC515S Wireless portable doorbell with halo light, sleep mode and push button – White
- DC515NGBS Wireless plug-in doorbell with sleep mode, nightlight and push button – Grey
- DC515NG Wireless portable doorbell with halo light and push button – Grey
- DC515NBS Wireless plug-in doorbell with sleep mode, nightlight and push button – White
- DC515N Wireless portable doorbell with halo light, sleep mode and push button – White
- DC315NG Wireless portable doorbell with halo light and push button – Grey
- DC315NBS Wireless plug-in doorbell with halo light, USB charging and push button – White
- DC315N Wireless portable doorbell with halo light and push button – White
- DC313SFB Wireless portable doorbell with volume control and two push buttons – White
- DC313NHGBS Wireless portable and plug-in doorbell with volume control and push button – White
- DC313NG Wireless portable doorbell with volume control and push button – Grey
- DC313NFB Wireless portable doorbell with volume control and two push buttons – White
- DC313NBS Wireless plug-in doorbell with volume control and push button – White
- DC313N Wireless portable doorbell with volume control and push button – White
- DC312SP2USB Wireless plug-in doorbell with push button – White
- DC311NBS Wireless plug-in doorbell with push button – White
- DC311N Wireless portable doorbell with push button – White
- DCP311 Wireless push button with LED confidence light – Portrait, White
- DCP311G Wireless push button with LED confidence light – Portrait, Grey
- DCP511 Wireless push button with nameplate and LED confidence light – Offset Landscape, White
- DCP711 Wireless push button with LED confidence light – Round, White
- DCP711G Wireless push button with LED confidence light – Round, Grey
- DCP917S Doorbell wired to wireless converter kit – White
- HS3MAG1N Wireless door and window sensor – White
- HS3MAG1S Wireless door and window sensor – White
- HS3MAG2S Wireless door and window sensor twin pack – White
- HS3SS1S Wireless solar siren
- HS3PIR2S Wireless motion sensor (PIR) twin pack
- HS3PIR1S Wireless motion sensor (PIR)
- HS3FOB1S Wireless remote control key fob
- HS3BS1S Wireless battery siren
- L430S Wireless Motion Sensor (IP54) – White

## Contact Me

I'm actively working to understand this protocol and documenting what I find in [This Honeywell Wireless Doorbell GitHub](https://github.com/klohner/honeywell-wireless-doorbell).
 
[Please contact me](https://docs.google.com/forms/d/e/1FAIpQLSdp9HEu3CN5-piqU99VRzgcrQNJJ2AkFsnU2TQhqLPHvdzj4g/viewform?usp=sf_link) if you'd like to help.

--Karl Lohner.
