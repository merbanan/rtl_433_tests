Documenting flex-decoder examples—for the 433 MHz sensors and remotes included with this Amazon alarm kit:

https://www.amazon.com/dp/B0H1VYZY54  
ASIN: `B0H1VYZY54`

The kit appears to use a fixed-code x1527-style protocol. I have captured and confirmed the PIR motion sensor, door/window contact, four-button remote, and separate single-button SOS remote.

## Environment

- rtl_433 version: `rtl_433 version 25.02-47-g7433023b`
- Receiver: RTL-SDR selected as device 1
- Center frequency: 433.92 MHz
- Sample rate: 1.024 MS/s
- Modulation: OOK PWM

Capture command:

```bash
rtl_433 -d 1 -c 0 -f 433.92M -s 1024k \
  -R 0 -A -S all -T 15 \
  -Y autolevel -Y magest \
  -M level -M noise
```

The following general flex timing reliably decodes all four device types:

```text
m=OOK_PWM,s=432,l=1152,r=1300,bits>=24,bits<=25
```

Measured values vary somewhat by device:

- Short pulse: approximately 380–440 µs
- Long pulse: approximately 1150–1255 µs
- Inter-frame gap: approximately 12–14 ms
- Each transmission is normally repeated several times

## Protocol format

The decoded row contains:

```text
20-bit fixed device ID
4-bit command
1 trailing framing bit, always 1
```

rtl_433 therefore commonly displays 25 bits. For example:

```text
ffb0288
^^^^^ ^ ^
 ID  cmd trailing bit
```

The actual payload is the first 24 bits; the final displayed `8` represents the single trailing bit left-aligned in the last hex nibble.

I do not see a checksum, CRC, rolling counter, or model discriminator. The device ID is fixed and appears unique per physical transmitter.

## Confirmed devices and commands

The example IDs below are specific to my physical units and are not a vendor or model signature.

| Device               | Example ID | Decimal ID | Command  | Meaning   | 24-bit payload |
| -------------------- | ---------- | ---------- | -------- | --------- | -------------- |
| PIR motion sensor    | `ffb02`    | 1047298    | `8`      | Motion    | `ffb028`       |
| Door/window sensor   | `92fc9`    | 602057     | `9`      | Open      | `92fc99`       |
| Door/window sensor   | `92fc9`    | 602057     | `6`      | Closed    | `92fc96`       |
| Four-button remote   | `06fbf`    | 28607      | `E` / 14 | Arm       | `06fbfe`       |
| Four-button remote   | `06fbf`    | 28607      | `D` / 13 | Disarm    | `06fbfd`       |
| Four-button remote   | `06fbf`    | 28607      | `B` / 11 | Home mode | `06fbfb`       |
| Four-button remote   | `06fbf`    | 28607      | `7`      | SOS       | `06fbf7`       |
| Single-button remote | `9ead9`    | 649945     | `F` / 15 | SOS       | `9ead9f`       |

The four-button mappings were confirmed in a controlled live test, pressing ARM, DISARM, HOME, and SOS in that order:

```text
ARM:     06fbfe8
DISARM:  06fbfd8
HOME:    06fbfb8
SOS:     06fbf78
```

The separate SOS remote repeatedly produced:

```text
9ead9f8
```

## Working per-device flex decoders

The `match` values below are specific to my units. Matching the known ID or complete payload is necessary to prevent unrelated 433 MHz traffic from producing false events.

### PIR motion sensor

```text
n=Amazon-PIR-FFB02,m=OOK_PWM,s=432,l=1152,r=1300,bits>=24,bits<=25,match=ffb028,unique,get=id:@0:{20},get=@20:{4}:cmd:[8:MOTION]
```

### Door/window contact

```text
n=Amazon-Door-92FC9,m=OOK_PWM,s=432,l=1152,r=1300,bits>=24,bits<=25,match=92fc9,unique,get=id:@0:{20},get=@20:{4}:cmd:[6:CLOSED 9:OPEN]
```

### Four-button remote

```text
n=Amazon-Remote-06FBF,m=OOK_PWM,s=432,l=1152,r=1300,bits>=24,bits<=25,match=06fbf,unique,get=id:@0:{20},get=@20:{4}:cmd:[14:ARM 13:DISARM 11:HOME 7:SOS]
```

### Single-button SOS remote

```text
n=Amazon-SOS-9EAD9,m=OOK_PWM,s=432,l=1152,r=1300,bits>=24,bits<=25,match=9ead9f,unique,get=id:@0:{20},get=@20:{4}:cmd:[15:SOS]
```

## Relationship to existing rtl_433 support

This looks related to the existing [[Chuango Security Technology decoder](https://github.com/merbanan/rtl_433/blob/master/src/devices/chuango.c)](https://github.com/merbanan/rtl_433/blob/master/src/devices/chuango.c) and [[EV1527 PIR flex configuration](https://github.com/merbanan/rtl_433/blob/master/conf/EV1527-PIR-Sgooway.conf)](https://github.com/merbanan/rtl_433/blob/master/conf/EV1527-PIR-Sgooway.conf), but the measured timing is closer to approximately 400/1200 µs than the Chuango decoder's 568/1704 µs profile.

I understand that fixed-code protocols without a checksum are prone to false positives and should not necessarily be enabled by default. In light of the concerns discussed in issue #3611, any of the following would be useful:

1. Confirmation that these devices should be treated as a Chuango/x1527 variant.
2. A disabled-by-default native decoder with the appropriate timing and command mappings.
3. Example flex configuration files documenting the PIR, door-contact, and remote mappings.
4. Guidance on the preferred way to contribute the labeled sample files as regression tests.

## Sample files

I can attach the following captures:

- `pir-test.zip` — PIR motion transmissions
- `door3.zip` — labeled door-open and door-closed transmissions
- `remote.zip` — four-button remote and separate SOS remote transmissions
- `IMG_6527.jpeg` — internal PIR PCB photograph; PCB marking `V1.0 20250910`

Useful annotated samples and recovered codes include:

- PIR motion: repeated `ffb028`
- Door open: repeated `92fc99`
- Door closed: repeated `92fc96`
- Four-button remote ARM: `06fbfe`
- Four-button remote DISARM: `06fbfd`
- Four-button remote HOME: `06fbfb`
- Four-button remote SOS: `06fbf7`
- Separate SOS remote: `9ead9f`

I can provide additional individually labeled `.cu8` captures if the current samples are insufficient or if a different capture command is preferred.
