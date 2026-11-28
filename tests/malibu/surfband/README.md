# Malibu Boats Surf Band

Wrist-worn 8-button remote with an LED, used on Malibu and Axis wake boats to
control the surf system, ballast wedge, cruise speed and stereo volume.
The tested unit is model "26DRF8/LR2000" (PCB marked `26DRF8 LR2000 PCB1.0 2016.12.13`).
There appear to be at least 2 models of this remote.

The receiver on the boat is a separate Medallion module, "Surf Band Dongle
Universal", Medallion PN 1539-10855-01, Malibu PN 3962071.1.

FCC ID: [2AFN315RM01](https://fccid.io/2AFN315RM01).
The FCC filing describes a different, ASK-modulated 433.92 MHz "Go Rider
Controller" by Medallion, not this unit.

Photos: [front](front.jpg), [back](back.jpg), [inside front](inside_front.jpg),
[inside back](inside_back.jpg).

## Hardware

Two labelled chips on the board:

```
1026AA
G2D0A
```

```
S14031
BPS1W7
1637
```

The second is a SiLabs [Si4031](https://www.silabs.com/documents/public/data-sheets/Si4030-31-32.pdf)
transmitter, used with its packet handler in the default configuration.

## Signal

- 433.00 MHz (not 433.92 MHz); one unit measured 432.997 MHz with a
  receiver calibrated against ATSC pilot tones, within its crystal's tolerance
- FSK, 1200 baud (833 us per bit), NRZ, no Manchester coding or whitening
- Very small deviation: the two tones are about 4.1 kHz apart (about +-2 kHz)
- Each frame is about 123 ms long

Frame format (Si443x packet handler defaults):

    PREAMBLE:40b SYNC:2dd4 LEN:08 'B' 'U' BTN BTN 'O' 'N' BTN '\r' CRC:16

- `LEN` is always 0x08, the number of payload bytes that follow
- `BTN` is the button code, sent three times
- `CRC` is CRC-16, poly 0x8005, init 0x0000, over `LEN` and the payload

A brief press sends one frame with the button code, then a Release frame.
Holding a button repeats a Hold frame every 131 ms, followed by a Release frame.
There is no device ID: every remote sends identical frames.

| Code | Button | PCB label |
|------|--------|-----------|
| 0x01 | Surf Left | SW1 |
| 0x07 | Surf Right | SW3 |
| 0x0a | Volume Up | SW4 |
| 0x03 | Volume Down | SW9 |
| 0x02 | Wedge Up | SW5 |
| 0x05 | Wedge Down | SW6 |
| 0x08 | Speed Up | SW7 |
| 0x0b | Speed Down | SW8 |
| 0xaa | Hold (repeat while held) | |
| 0x00 | Release | |

Volume Up/Down follow the speaker icons on the faceplate (SW4 is under the
louder icon). The PCB silkscreen labels them the other way around, `SW4_VOL-`
and `SW9_VOL+`; this has not been checked against the boat.

All frames are listed in `codes_test.txt`.

Flex decoder:

    -X 'n=Surf-Band,m=FSK_PCM,s=833,l=833,r=20000,preamble=2dd408'

## Samples

One short press per file: the button frame, one Hold frame, then the Release
frame.

- `sw3_surf_right_433M_250k.cu8`
- `sw5_wedge_up_433M_250k.cu8`
- `sw7_speed_up_433M_250k.cu8`

Volume Up (SW4) held for about half a second: the button frame, 4 Hold frames
131 ms apart, then the Release frame.

- `hold_volume_up_433M_250k.cu8`

A short Surf Left (SW1) press whose signal sits just below the default
minimum detection level (`-Y minlevel`, -12.1 dB), so the default only partly
decodes it:

- `sw1_surf_left_433M_250k.cu8`

It holds the Surf Left frame at 0.50 s, a Hold frame at 0.63 s and the Release
frame at 0.95 s, all CRC-valid and about 35-40 dB above the noise. The default
detector currently decodes only the Release, so that is all its expected output
lists. With `-Y autolevel`, which sets the minimum level from the noise, all
three decode; so does the default with the signal scaled up by about 3.5 dB.
The file keeps 0.5 s of noise before the first frame, which `autolevel` needs
to settle; with less it also decodes only the Release. Update the expected
output if detection at this level improves.

Captured with a Nooelec NESDR SMArt v5 (RTL-SDR) at 433.0 MHz, 250 kS/s,
fixed 25.4 dB gain (`rtl_sdr -f 433000000 -s 250000 -g 25.4`), and trimmed
to the frames with 50 ms margins, otherwise unprocessed. Automatic gain
overloads the receiver at close range.

The deviation is too small for the classic and min/max FSK pulse detectors
alone, but the default (auto) detector decodes it: every frame in these
samples except the two noted above for `sw1_surf_left_433M_250k.cu8`.
Decoder: [merbanan/rtl_433#3746](https://github.com/merbanan/rtl_433/pull/3746).
