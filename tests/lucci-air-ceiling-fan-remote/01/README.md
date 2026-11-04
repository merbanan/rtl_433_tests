# Lucci Air Slimline Ceiling Fan Remote

<https://www.beaconlighting.com.au/lucci-fan-slimline-remote-1.html>

* SKU: 210012
* Model: UC7216T (transmitter), UC7076RY (receiver)
* Voltage: 2x 1.5V AAA (transmitter), 230-240VAC 50/60Hz (receiver)
* Frequency: 433.92MHz
* Range: Approx. 20-30 feet
* Made in China

* PCB: RHINE UC7216T Ver. b 140403
* MCU: RHINE RH787T, RH787T3B-T 17ADP03B
* FCC ID: Similar to CHQ7216T, but with white buttons and 433.92MHz

* 5 buttons, 4 DIP switches, 1 red LED.

### Buttons:

* 1: HI
* 2: MED
* 3: LOW
* 4: OFF
* 5: LIGHT

![photo](photo.jpg)

In the examples below I've pressed each of the 5 buttons with each of the 16 DIP switch combinations.
DIP=0001 means only the 4th DIP switch from the left is ON/up. The rest OFF/down.

Captured at 433.988265 MHz with RTL-SDR.com Blog V3 dongle.

### Captures:

```
$ rtl_433 -f 433987000 -a -t
```

File                   | DIP  | Button
---------------------- | ---- | ------------------
g001_433.987M_250k.cu8 | 0000 | HI
g002_433.987M_250k.cu8 | 0000 | MED
g003_433.987M_250k.cu8 | 0000 | LOW
g004_433.987M_250k.cu8 | 0000 | OFF
g005_433.987M_250k.cu8 | 0000 | LIGHT
g006_433.987M_250k.cu8 | 0001 | HI
g007_433.987M_250k.cu8 | 0001 | MED
g008_433.987M_250k.cu8 | 0001 | LOW
g009_433.987M_250k.cu8 | 0001 | OFF
g010_433.987M_250k.cu8 | 0001 | LIGHT
g011_433.987M_250k.cu8 | 0010 | HI
g012_433.987M_250k.cu8 | 0010 | MED
g013_433.987M_250k.cu8 | 0010 | LOW
g014_433.987M_250k.cu8 | 0010 | OFF
g015_433.987M_250k.cu8 | 0010 | LIGHT
g016_433.987M_250k.cu8 | 0011 | HI
g017_433.987M_250k.cu8 | 0011 | MED
g018_433.987M_250k.cu8 | 0011 | LOW
g019_433.987M_250k.cu8 | 0011 | OFF
g020_433.987M_250k.cu8 | 0011 | LIGHT
g021_433.987M_250k.cu8 | 0100 | HI
g022_433.987M_250k.cu8 | 0100 | MED
g023_433.987M_250k.cu8 | 0100 | LOW
g024_433.987M_250k.cu8 | 0100 | OFF
g025_433.987M_250k.cu8 | 0100 | LIGHT
g026_433.987M_250k.cu8 | 0101 | HI
g027_433.987M_250k.cu8 | 0101 | MED
g028_433.987M_250k.cu8 | 0101 | LOW
g029_433.987M_250k.cu8 | 0101 | OFF
g030_433.987M_250k.cu8 | 0101 | LIGHT
g031_433.987M_250k.cu8 | 0110 | HI
g032_433.987M_250k.cu8 | 0110 | MED
g033_433.987M_250k.cu8 | 0110 | LOW
g034_433.987M_250k.cu8 | 0110 | OFF
g035_433.987M_250k.cu8 | 0110 | LIGHT
g036_433.987M_250k.cu8 | 0111 | HI
g037_433.987M_250k.cu8 | 0111 | MED
g038_433.987M_250k.cu8 | 0111 | LOW
g039_433.987M_250k.cu8 | 0111 | OFF
g040_433.987M_250k.cu8 | 0111 | LIGHT
g041_433.987M_250k.cu8 | 1000 | HI
g042_433.987M_250k.cu8 | 1000 | MED
g043_433.987M_250k.cu8 | 1000 | LOW
g044_433.987M_250k.cu8 | 1000 | OFF
g045_433.987M_250k.cu8 | 1000 | LIGHT
g046_433.987M_250k.cu8 | 1001 | HI
g047_433.987M_250k.cu8 | 1001 | MED
g048_433.987M_250k.cu8 | 1001 | LOW
g049_433.987M_250k.cu8 | 1001 | OFF
g050_433.987M_250k.cu8 | 1001 | LIGHT
g051_433.987M_250k.cu8 | 1010 | HI
g052_433.987M_250k.cu8 | 1010 | MED
g053_433.987M_250k.cu8 | 1010 | LOW
g054_433.987M_250k.cu8 | 1010 | OFF
g055_433.987M_250k.cu8 | 1010 | LIGHT
g056_433.987M_250k.cu8 | 1011 | HI
g057_433.987M_250k.cu8 | 1011 | MED
g058_433.987M_250k.cu8 | 1011 | LOW
g059_433.987M_250k.cu8 | 1011 | OFF
g060_433.987M_250k.cu8 | 1011 | LIGHT
g061_433.987M_250k.cu8 | 1100 | HI
g062_433.987M_250k.cu8 | 1100 | MED
g063_433.987M_250k.cu8 | 1100 | LOW
g064_433.987M_250k.cu8 | 1100 | OFF
g065_433.987M_250k.cu8 | 1100 | LIGHT
g066_433.987M_250k.cu8 | 1101 | HI
g067_433.987M_250k.cu8 | 1101 | MED
g068_433.987M_250k.cu8 | 1101 | LOW
g069_433.987M_250k.cu8 | 1101 | OFF
g070_433.987M_250k.cu8 | 1101 | LIGHT
g071_433.987M_250k.cu8 | 1110 | HI
g072_433.987M_250k.cu8 | 1110 | MED
g073_433.987M_250k.cu8 | 1110 | LOW
g074_433.987M_250k.cu8 | 1110 | OFF
g075_433.987M_250k.cu8 | 1110 | LIGHT
g076_433.987M_250k.cu8 | 1111 | HI
g077_433.987M_250k.cu8 | 1111 | MED
g078_433.987M_250k.cu8 | 1111 | LOW
g079_433.987M_250k.cu8 | 1111 | OFF
g080_433.987M_250k.cu8 | 1111 | LIGHT
g081_433.987M_250k.cu8 | 0000 | HI (long press)
g082_433.987M_250k.cu8 | 0000 | MED (long press)
g083_433.987M_250k.cu8 | 0000 | LOW (long press)
g084_433.987M_250k.cu8 | 0000 | OFF (long press)
g085_433.987M_250k.cu8 | 0000 | LIGHT (long press)

### Decoding

rtl_433 -q -F json -R 0 -X 'lucci:OOK_PWM:340:680:800:800' -r g001_433.987M_250k.cu8

The signal needs a closer inspection, it does not look like just PWM, the gaps might matter too. It is not Manchester encoding like rtl_433 guesses, though.

So far, it looks like:

DIP=1111, press Lights button

packet | packet | packet
------ | ------ | ------
0f c0 | 07 e0 | 07 f0
00001111 110 | 00000111 1110 | 00000111 1111
AAAA1CCC 1CC | 0AAAA1CCC 1CC | 0AAAA111 1111

1. 4x address bits xor'd
2. `1`
3. 3x command bits
4. `1`
5. 2x command bits
6. `0`
7. 4x address bits xor'd
8. `1`
9. 3x command bits
10. `1`
11. 2x command bits
12. `0`
13. 4 address bits xor'd
14. `1111111`
