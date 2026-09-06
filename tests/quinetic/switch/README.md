# Quinetic Switches and Sensors

## Overview

The Quinetic series includes a number of 433Mhz switches, PIR sensors and receivers.
All operate on 433Mhz, and some devices also include 2.4Ghz Wifi.

A Quinetic switch/sensor is typically paired with a Quinetic Receiver (Smart Plug, 5A-Mini-Reciever, etc.)
However if left unpaired - the switch/sensor can be used by rtl_433 for control/automation.

## Hardware Info

* PIR sensors are battery powered. The signals are (presumed) to be consistent with switches.
* Switches are self-powered, and operate on 2.5V power generation when pushed or released (using mag coil).
* Switches are available in many form-factors: 1-Button, 2-Button, 3-Button, 1-Button-Fob, Door Switch

## Hardware Validated

***'x' represents colour variation***

* QUGDMK (Grid Switch - 1 Gang)
* QUWS1x (Wall Switch 1 Gang)
* QUWS2x (Wall Switch 2 Gang)
* QUWS3x (Wall Switch 3 Gang)

## RF Signal

Frame Layout:

```
...PPPP SS IISCC
```

* P: 48-bits+ of Preamble
* S: 16-bits of Sync-Word (0xA4, 0x23)
* I: 16-bits of Device ID
* S: 8-bits of Device Action
* C: 16-bits of In-Packet Checksum (CRC-16 AUG-CCITT)

CRC Checksum Method:

* In-Packet Checksum: CC
* 24-bits of data to CRC-check: IIS

Signal Summary:

* Frequency: 433.3 Mhz, +/- 50Khz
* Nominal pulse width: 10us
* Modulation: FSK_PCM
* Checksum: CRC-16/AUG-CCITT

Button Characteristics:

* A switch emits 3-4 transmissions (rows) when a button is pressed (with button ID).
* A switch emits 3-4 transmissions (rows) when a button is released (without button ID).
* This retransmission is common.
* CRC failures are relatively common, perhaps 1 in 20 rows.
* Buttons are 'push-button / momentary' style, without ON/OFF position (stateless).

## Debugging

### Capture Sample Files

* Prepare a new directory to store the captures.
* With an RTL2832 SDR, manually setting gain to 30 or 37 is recommended.

```
# Capture known and unknown data into sample file(s) and stop after 15 secs
rtl_433 -g 37 -f 433.4M -s 1024k -Y minmax -S all -T 15
```

### Debug Flex Decoder : quinetic_switch.conf

* CRC validation is not included within the flex-decoder.
* Flex decoder is only for basic inspection of data.

```
rtl_433 -c ./quinetic_switch.conf -r <FILE>
```
