# DeWalt Wireless-Tool-Connect (WTC)

Cordless vacuum cleaner control.  Used by DeWalt battery-operated 
power tools to start/stop a vacuum cleaner when the trigger is pulled.

The symbol displayed on tools/packaging are two chain links (like an '8') with
three radiating lines.

## FAQ

1. Note 1: Why/what?!?  Health and safety (eg. OSHA) require dust extraction; and 
mains-activated pass-through sockets don't work with cordless battery tools!

2. Note 2: DeWalt _Wireless-Tool-Connect_ (WTC; 433.92 MHz) is different
to DeWalt _Tool-Connect_ (Bluetooth), which is used for assest tracking
and customisation!

3. Note 3: Makita/Festool/Hilti/Bosch use Bluetooth advertisements for
their own vacuum start/stop control.

## DeWalt Wireless-Tool-Connect support (c.2021)

Tool   | Function           | Direction
:---   | :------            | :--------
DVC585 | Vacuum (T-Stak)    | RX
DVC586 | Vacuum (T-Stak)    | RX
DWH161 | Vacuum (shoulder)  | RX
DCV585KV | Remote (keyfob)  | TX
N69688 | Remote (keyfob)    | TX
DCW200 | Sander             | TX
DCE800 | Wall grinder       | TX
DCG200 | Wall chaser        | TX
DCH417 | Hammer drill (SDS) | TX
DCH614 | Hammer drill (SDS) | TX
DCH735 | Hammer drill (SDS) | TX
DCS520 | Plunge saw         | TX
DCS727 | Mitre saw          | TX

### Tool under investigation

The cheapest tool available with WTC was the DCW200 ("quarter-sheet")
orbital sander.  This has a mechanical off-on switch (under a rubber
moulding), and a rotary speed wheel.

(Extra numbers/letters after "DCW200-..." indicate the number of
included 18V batteries in the set and whether it includes a case.  In this example,
a "DCW200-NT" (European) or "DCW200-BT" (US) was obtained:

* -N/-B = Naked/Bare-bones tool: without batteries, without charger
* -T = in DeWalt T-Stak transport case

The DeWalt 18V battery slot has four contacts: the two main +18V/0
power rails, and two sensing pins.  Supplying just 18V was
insufficient: all four contacts must be connected (via a correct set
of resistors!) to power the tool up.

(...An adaptor for using DeWalt tools with eg. Makita LXT batteries can
be obtained from the usual online sources; but on the DCW200 (only) using
larger batteries/adaptors will require unclipping the dust extraction port.)

### FCC Marking

There are no FCC markings on the outside, or under the battery label,
or in the (European) manual.  But we know that the tool contains
a modular transmission self-contained assembly: YJ7WTCTX (DeWalt, WTC, Transmitter).

#### Tool module
* "Theory of operation, WTC TX"
* YJ7WTCTX (DeWalt, WTC, Transmitter)
* https://fcc.report/FCC-ID/YJ7WTCTX/4160332

"""... self-contained 433 MHz transmitter requiring only a 5–25 VDC
power input and a 5–20 VDC transmit enable signal.
... the enable signal indicates the run/not run status of the tool.
... the module broadcasts a fixed pre-programmed data packet.
... prefix of the data packet is the target address of the paired receiver."""

The last line is probably misleading; the protocol is one-way only: so
"pairing" is performed only at the vacuum cleaner end, by memorising
the next seen transmission.

* Internal Photos
* https://fcc.report/FCC-ID/YJ7WTCTX/4160329
* "WTC TX V0_7" / "HS D E315835" / "94V-0" / "CT13"

* "Transmit Module User's Manual"
* https://fcc.report/FCC-ID/YJ7WTCTX/4160335
*

"""...The WTC TX (Wireless Tool Control Transmit) module is a 433 MHz
transmitter for sending DEWALT WTC status messages. ... The WTC TX
module is based on the Microchip MICRF112 UHF transmitter and the
ATTINY416 microcontroller."""

"""...sends a "Start" command and starts a 10 second timer.
...If the timer reaches 10 seconds, it re-transmits the "Start" command.
...If at any time the circuit is deactivated by the user, a "Stop"
command is sent,"""

(The repeating 10-second transmissions were not yet observed, but the
"start" and "stop" messages have been observed; each is send twice).

#### YJ7DCV585

A remote control keyfob also exists, supplied in conjunction with
purchase of a DVC585 battery-powered T-Stak-mounted wet/dry vacuum
cleaner.

* "DCV585 Remote for Dust Extractor Test Report"
* https://fccid.io/YJ7DCV585/Test-Report/Test-Report-3995116
* "Flexvolt Vac" / "RF Tag V0.7" / "E179720" / "2518"

Which gives the overview:

"""The Stanley Black & Decker, Inc. 433 MHz Device is a Key fob
wireless remote to turn on/off a DC-powered dust extractor for jobsite
use.""

and an observed emmisions designation, from the test analysis:

"""
* ... Occupied Bandwidth (20dB): 122.8 kHz
* ... Occupied Bandwidth (99%): 179 KHz
* ... FCC Emission Designator: 179KP0N
"""

#### Microchip MICRF112

This RF chip is normally sold for "Remote Keyless Entry" (RKE), garage
door openers, "Tire Pressure Monitor Systems" (TPMS), outdoor weather
stations... (ie. all the normal suspects, etc, etc.)

* https://www.microchip.com/en-us/product/MICRF112
* https://ww1.microchip.com/downloads/en/DeviceDoc/MICRF112.pdf

The chip requires a 13.56 MHz external crystal, which goes through an
internal 32x phase-locked loop (PLL) divider to get 433.92 MHz.

Out of the box the chip does ASK, but according to the datasheet (2013)
"To operate the MICRF112 in FSK Mode, one additional capacitor
is needed between XTLOUT pin and XTAL_MOD pin."

And "Data rates up to 50kbps ASK, 10kbps FSK"

#### 433 MHz signal

Eyeballing the signal with "Universal Radio Hacker" (URH) suggests that the signal is 
FSK, (but with variable length pulses of 55-135 usec...):

Centre frequency: 433.92 MHz.
FSK F1:               20 kHz   (50 us cycle)
FSK F2:                2 kHZ  (500 us cycle)

When the RF is awake, but has no data input, a pure 20 kHz sine wave
is being transmitted---probably corresponding to 00000..."

The training prefix is a smooth pure sine wave:

* F1 frequency (20 kHz, 50 usec period)
* ~150 cycles
* ~7.2 ms

Although not stated, the chip appears to attempt continuous-wave FSK,
leading to the observed variable length pulse widths while waiting for
F1/F2 to match.  The switch is not perfect though and gives a slight
discontinutity/blip at the state transition when viewed in PSK mode.

#### Analysis with RTL-433

The closest attempt at decoding so far has been; for tool-to-vacuum START:

    $ rtl_433 -R 0 -X 'n=DeWaltWTC,m=FSK_MC_ZEROBIT,s=55,l=135,r=1000,invert,reflect' -r dewalt-wtc-start_433.92M_250k.cu8
    {178} 010000000000003e93a710 010000000000003e93a710 0
    
and for tool-to-vacuum STOP:

    $ rtl_433 -R 0 -X 'n=DeWaltWTC,m=FSK_MC_ZEROBIT,s=55,l=135,r=1000,invert,reflect' -r dewalt-wtc-stop_433.92M_250k.cu8
    {178} 010000000000003e93a718 000000000000003e93a718 0

##### Message format

Appears to be a 32-bit message, repeated twice (because, noise, etc).
Probably ~16 bits of header, ~8 bits of unique-ID/serial number, and
~8 bits of status.

(There must ... be *some* unique identifier otherwise all the vacuums on
a job site will start everytime somebody starts a power tool.)

On a sample-size of one available tool it is difficult to identify the
remainder of the message contents, except for the start/stop bit in
the last octet.  Needs a visit to a friendly DeWalt dealer or hardware
store!
