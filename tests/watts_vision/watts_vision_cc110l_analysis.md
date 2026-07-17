# Watts Vision / CC110L bitstream analysis

The wire framing, both CRCs, record grammar, temperature representation, and
the `8a` mode byte are now understood. Several state flags still lack safe
human-readable names.

Confidence terms used below:

- **Confirmed**: demonstrated by valid captures.
- **Strong**: multiple independent observations agree, but a controlled state
  sweep.
- **Provisional**: best interpretation with a concrete experiment to test it.
- **Unknown**: only width, storage, or bit propagation is known.

## Main results

1. The packet is not simply `length + source + destination`. A fixed `c6` byte
   separates the two 32-bit identifiers:

   ```text
   AA...AA  D3 91 D3 91
   length source[4] c6 destination[4] records... CRC-MODBUS[2] CRC-CMS[2]
   ```

2. `length` counts all bytes after itself through the application MODBUS CRC.
   It excludes itself and the radio CRC. This is exactly CC110L variable-length
   packet behavior.

3. The middle is a universal length-coded record stream. For a nonzero tag:

   ```text
   value_length  = (tag >> 6) + 1       # 1, 2, 3, or 4
   record_length = value_length + 1     # tag plus value
   ```

   The short payload is therefore:

   ```text
   03 P1 | df S0 S1 S2 S3 | 3b X
   ```

   `03` is a tag, not a message-type byte. `df` has four values, so the alleged
   standalone `00` separator is actually `df[3]`. This closes both unexplained
   short-frame byte gaps.

4. Temperatures and setpoints are unsigned, big-endian, native tenths
   Fahrenheit:

   ```text
   F = raw / 10
   ```

5. `8a[2]` is an operating-mode selector, not an unexplained qualifier.
   Values `00, 01, 02, 03, 04, 08, 0b` have community API matches.
   `8a 02 84 03` is the active Eco setpoint 64.4 °F; `8a 02 cc 00` is Comfort
   71.6 °F.

6. The second-temperature gap is closed: `5e` is a second big-endian
   floor/external-sensor temperature. `084c` is the unavailable sentinel for
   both primary and secondary temperature.

7. The two CRC checks have combined GF(2) parity-check rank 32 at both observed
   frame lengths. Requiring both gives nominal random-error strength `2^-32`,
   rather than an assumed or correlated 16-bit strength. This is error
   detection, not authentication.

8. `03` is strongly a controller pairing/association slot, not operating mode:
   its value is stable per endpoint and the builder carries mode separately in
   tag `94`. Pairing code allocates the stored association value.

9. `cc` is a pair of native F×10 floor-limit temperatures used in FLL mode.
   Zero selects an inactive/unavailable path. Which word is lower versus upper
   remains the only unresolved part of this tag.

## Physical and CC110L packet layer

### Measurements from the IQ captures

| Property | Result | Confidence |
|---|---:|---|
| Modulation | Gaussian-shaped 2-FSK (GFSK) | Strong |
| Symbol period | approximately 26 µs | Confirmed |
| Data rate | approximately 38.46 kb/s | Confirmed |
| Tone separation | approximately 38.0 kHz | Confirmed |
| Frequency deviation | approximately ±19.0 kHz | Confirmed |
| Preamble | four alternating `aa`/`55` bytes | Confirmed |
| Sync | `d391 d391` | Confirmed |
| Bit order | MSB first within on-air bytes | Confirmed |
| Manchester/FEC | neither present | Confirmed |
| Whitening | disabled | Confirmed |

The tone difference is reliable but absolute carrier is not: the sample files
were centered at 868.25 MHz with uncalibrated transmitter/receiver offsets. In
one capture the stable tones were about +67.6 and +105.6 kHz from file center.

The instantaneous-frequency transition occupies most of a symbol rather than
being an abrupt two-tone switch, consistent with the CC110L GFSK shaper. A
generic rtl_433 FSK PCM slicer can still recover its NRZ data.

## Byte-level frame format

Offsets start at the length byte after sync.

| Offset | Size | Field | Notes |
|---:|---:|---|---|
| 0 | 1 | `length` | Bytes 1 through inner CRC; total frame bytes minus 3. |
| 1 | 4 | source ID | Displayed big-endian. |
| 5 | 1 | marker | `c6` in all known frames. |
| 6 | 4 | destination ID | Displayed big-endian. |
| 10 | variable | record stream | Ends immediately before inner CRC. |
| `N-4` | 2 | CRC-16/MODBUS | Numeric CRC serialized low byte first. |
| `N-2` | 2 | CRC-16/CMS | Numeric CRC serialized high byte first; hardware CRC. |

| Length | Post-sync bytes | Record bytes | Typical role |
|---:|---:|---:|---|
| `14` (20) | 23 | 9 | compact central-to-endpoint command/state |
| `22` (34) | 37 | 23 | endpoint-to-central status/report |

For `length=20`, the CC110L FIFO payload has 20 bytes following the length:
IDs, `c6`, records, and inner CRC. Its hardware appends two CRC bytes outside
that count.

### Direction and identifiers

`d0904d89` is the common central-controller ID; `d037xxxx` varies by endpoint.
The strong direction interpretation is:

```text
short: d0904d89 -> d037xxxx   central command/state distribution
long:  d037xxxx -> d0904d89   thermostat status/report
```

For a given endpoint, the first three bytes of short `df` recur in long `8d`,
consistent with command acknowledgement/reporting. A near-field capture at
each transmitter would independently prove physical direction, but the
multi-endpoint address pattern is already strong.

## CRC definitions and coverage

### Inner application CRC

```text
name:      CRC-16/MODBUS
poly:      8005 (reflected implementation a001)
init:      ffff
refin/out: true / true
xorout:    0000
coverage:  source through final record; excludes length and both CRCs
wire:      low byte, high byte
```

### Outer CC110L CRC

```text
name:      CRC-16/CMS (same parameters as CC110L CRC-16-IBM naming)
poly:      8005
init:      ffff
refin/out: false / false
xorout:    0000
coverage:  length through and including the inner CRC bytes
wire:      high byte, low byte
```

| Frame | Inner numeric / wire | Outer numeric / wire |
|---|---|---|
| short to `...4654`, `df=00110100` | `0cc9` / `c9 0c` | `1607` / `16 07` |
| long from `...4654` | `0d31` / `31 0d` | `98a4` / `98 a4` |
| long from `...4655` | `9274` / `74 92` | `faf3` / `fa f3` |

## Quantifying selectable integrity in rtl_433

Use effective check bits:

```text
integrity_bits = -log2(P_undetected)
```

Do not add nominal widths blindly. Checks may cover the same bytes or be
linearly dependent. For fixed length, form each check's syndrome for every
possible transmitted-bit flip, concatenate the syndromes, and compute the
GF(2) matrix rank. That rank is the number of independent check bits for
uniform random error patterns.

For Watts Vision, the combined matrices have rank 32 for both observed lengths:

| Accepted evidence | Effective integrity | Level |
|---|---:|---:|
| sync/length/fixed fields only | 0 check bits | L0 |
| inner MODBUS CRC only | 16 bits | L3 |
| outer CC110L/CMS CRC only | 16 bits | L3 |
| both CRCs | 32 bits | L4 |

A useful general rtl_433 scale is:

| Level | Effective bits | Typical evidence |
|---:|---:|---|
| L0 | 0 | framing/plausibility, no validated integrity |
| L1 | 1-7 | parity or tiny checksum |
| L2 | 8-15 | CRC-8 or comparable checksum |
| L3 | 16-23 | applicable full CRC-16 or equivalent |
| L4 | 24+ | independent combined checks, CRC-24/32, or authenticated MIC |

Watts should default to `both`/L4. `outer` and `inner` are useful L3 recovery
modes; `raw`/L0 should be explicitly diagnostic and expose failed checks.
Suggested output is `integrity_level`, `integrity_bits`, and
`integrity_checks=["CRC-16/MODBUS","CRC-16/CMS"]`, while retaining rtl_433's
existing `mic="CRC"` convention if desired.

Preamble, sync, length, `c6`, known IDs, repetition, RSSI, and field
plausibility are signal/framing evidence. Do not add them to `integrity_bits`.
A 32-bit sync is not a message MIC, and CC110L modes can accept 30 of 32 bits.

The outer CRC alone guarantees detection of all burst errors up to 16 bits.
Requiring both gives a nominal uniformly random false-accept probability of
about one in 4.29 billion. Both are unkeyed, so an intentional transmitter can
recompute them: there is no authenticity, anti-replay, or cryptographic MIC.

## Record grammar

The parser advances by `(tag >> 6) + 2`:

| Tag range | Value bytes | Total record bytes |
|---|---:|---:|
| `01-3f` | 1 | 2 |
| `40-7f` | 2 | 3 |
| `80-bf` | 3 | 4 |
| `c0-ff` | 4 | 5 |

`00` is a special parser terminator, not an ordinary one-value tag. The high
two bits encode width. A decoder must
not merge tags just because their low six bits match.

### The former P1/separator gap

The compact payload consumes exactly nine bytes:

```text
03 P1       # tag 03, one-byte value
df A B C D  # tag df, four-byte state; D was the alleged separator
3b E        # tag 3b, one-byte flags
```

Example: `03 01 | df 00 11 01 00 | 3b 00`.

No byte is outside the grammar. Nor is `03` evidence of a unique short message
type: it is the first record tag in this command family. Other commands may
carry other record sets.

## Temperature, setpoint, and operating mode

| Tag/field | Meaning | Confidence |
|---|---|---|
| `4b` | primary regulation/air temperature, BE u16 F×10 | Confirmed |
| `5e` | secondary floor/external temperature, BE u16 F×10 | Confirmed |
| `8a[0:2]` | active setpoint, BE u16 F×10 | Confirmed |
| `084c` | unavailable temperature sentinel | Confirmed |

| Raw F×10 | Native value |
|---:|---:|
| `02bf` | 70.3 °F |
| `02cf` | 71.9 °F |
| `02f0` | 75.2 °F |
| `0284` | 64.4 °F |
| `02cc` | 71.6 °F |

The community integration independently treats API `temperature_air` as F×10,
matching the native wire representation.

### `8a[2]` modes

| Value | Behavior | Community API name | Confidence |
|---:|---|---|---|
| `00` | selects Comfort setpoint bank | Comfort | Confirmed |
| `01` | Off | Off | Confirmed |
| `02` | frost-protection bank | Frost Protection | Confirmed |
| `03` | Eco/reduced bank | Eco | Confirmed |
| `04` | Boost | Boost | Confirmed |
| `08` | scheduled state using Comfort-side bank | Program on | Confirmed numeric/strong wording |
| `0b` | scheduled state using Eco-side bank | Program off | Confirmed numeric/strong wording |

### Transient `02f0`, later `0284`

An early truncated prefix after the target request has `8a 02 f0 03`, or native
75.2 °F in mode 03. It matches the requested UI target after the controller's
display-unit conversion. Later prefixes and the complete CRC-valid frame have
`8a 02 85 03` and `8a 02 84 03`, native 64.5/64.4 °F in the same Eco mode.

This is no longer an encoding or qualifier ambiguity: byte three is mode 03
and the word is a setpoint. The remaining uncertainty is the transition:

- a temporary manual setpoint while the zone remained in Eco;
- a command followed by thermostat rejection/fallback to stored Eco;
- distinct reporting/cached phases; or
- timing interleave with another command.

The `02f0` prefix is truncated and cannot itself pass both CRCs, though its
exact target match is unlikely to be accidental. A timestamped mode/setpoint
sweep is required before naming this product behavior.

## Capture-confirmed tags

| Tag | Bytes | Current meaning | Confidence |
|---:|---:|---|---|
| `03` | 1 | stable controller association/slot value | Strong class, exact slot scope provisional |
| `3b` | 1 | small status/command flags | Storage confirmed, names unknown |
| `4b` | 2 | primary/air temperature | Confirmed |
| `4c` | 2 | diagnostic code and flags | Class confirmed, bits partial |
| `8a` | 3 | active setpoint plus operating mode | Confirmed |
| `8d` | 3 | compact/delta state report | Behavior confirmed |
| `8e` | 3 | setpoint bounds/configuration plus sensor/operation flags | Strong/partial |
| `cc` | 4 | two BE u16 floor-limit temperatures; zero disabled/unavailable | Strong meaning, order provisional |
| `df` | 4 | full four-byte state/command | Behavior confirmed, bits partial |

### Tag `03`

Cross-capture correlation resolves most of this field. Its value is stable for
each destination even while `df` changes:

| Endpoint | `03` value | Integrity of evidence |
|---|---:|---|
| `...4654` | `01` | multiple dual-CRC-valid frames |
| `...4590` | `02` | inner CRC valid; one-bit error in outer CRC field |
| `...465e` | `03` | dual-CRC valid |
| `...15c1` | `04` | multiple dual-CRC-valid frames |
| `...4655` | `07` | multiple dual-CRC-valid frames |

The tag `03` comes from a
per-zone/device association byte. In the same builder, operating mode is
normalized separately into the third value of tag `94`; it is **not** the tag
`03` value. Pairing/initialization sets the association field to 1 for one
class and allocates subsequent entries as an index plus 2. Parser and lookup
paths compare it while selecting stored entities.

Thus `03` is strongly a controller-assigned entity/zone/member slot or routing
index, not a mode. What is still unresolved is its exact namespace: zone number,
device position within a zone, RF association slot, or a closely related
controller index. Expose it as `association_id`/`slot` with the raw value; a
pairing capture that records central zone and member order will choose the
final name.

### Tags `df` and `8d`

Let `df` be `S0 S1 S2 S3`. It overwrites all four stored state bytes. `8d` is
a compact partial update of the same state family:

```text
8d[0]: updates S0 bits 0-1
8d[1]: updates S1 bits 0-1; bit 0 also opens an update gate
8d[2]: updates S2 bits 2, 3, and 7; bit 0 feeds a separate status bit
```

It carries no `S3`. Known timed pairs include:

```text
endpoint ...4654: df 00 11 01 00 -> 8d 00 11 01
endpoint ...4655: df 00 10 08 00 -> 8d 00 10 08
```

Other valid `...4655` commands change between `00 11 08 00` and
`00 10 08 00`, so an echo must be matched by time, not endpoint alone.

The UI/status bits as follows:

| Source | Derived use |
|---|---|
| `S2.bit3` | status bit 0 |
| `S2.bit6` | bit 3 for some classes; bit 5 for entity class `ef` |
| `S2.bit7` | status bit 4 |
| `S1.bit1` | status bit 5 |
| `S1.bit3` | status bit 6 |
| `S0.bit1` | status bit 8 |
| `S1.bit6` | status bit 11 |
| `S2.bits4-5` | warning/secondary-state path |

This is exact use, but not enough to label bits battery, heat demand, window,
lock, or acknowledgement. Those names require one-variable state captures.

### Tag `8e`

The known value is `8e 0a 24 93`. The first two bytes are stored separately.
Native bytes `0a=10` and `24=36` are very likely configured minimum and maximum
setpoint-bound values. The official UI exposes those settings with documented
numeric ranges 5-15 and 20-37. Values 10 and 36 fit both order and ranges. Tag
`1a` updates the first field alone, supporting a separately editable lower
bound. This is strong; changing the UI bounds independently would confirm it.

The low two bits of byte three select the regulation sensor:

| `8e[2] & 3` | Selection | Confidence |
|---:|---|---|
| 0 | `Amb`, external ambient | Strong |
| 1 | `FLR`, floor-only regulation | Behavior confirmed/label strong |
| 2 | `FLL`, air plus floor limits | Behavior confirmed/label strong |
| 3 | `Air`, internal air sensor | Strong |

Mode 1 can copy secondary `5e` into the primary regulation temperature; mode 2
enables the `cc` pair. This matches the official `Air`, `Amb`, `FLR`, and `FLL`
selector names.

Other third-byte use:

| Bit | Use | Meaning status |
|---:|---|---|
| 7 | copied to central state bit 1 | likely heat/cool or polarity family; unresolved |
| 6 | copied to state bit 0 under update conditions | probable output-demand family; unresolved polarity |
| 4 | retained raw in `93` | unknown |
| 3 | parser force/validity condition | unknown UI name |
| 1:0 | regulation sensor selector | mapped above |

`93 = 10010011b` sets bits 7, 4, 1, and 0 and selects `Air`. Both valid long
frames have the same value, so those two captures cannot correlate its flags.

### Tag `cc`

The four values are two big-endian words:

```text
cc[0:2] -> per-zone field +0x116
cc[2:4] -> per-zone field +0x114
```

The controller exposes them only in `FLL` sensor mode, and its resources contain
`Floor limit low` and `Floor limit high`. The strongest interpretation is a
floor lower/upper limit pair, probably low then high. Both are zero in current
Air-mode reports, consistent with inactive floor limits.

The FLL display path passes the stored word through the same temperature
formatter used by the confirmed temperature fields, and substitutes the
`084c` unavailable/default sentinel when it is zero. Thus the values use the
same F×10 temperature representation and zero means inactive/unavailable in
that path. Only the low-versus-high wire order remains provisional; distinct
nonzero FLL limits will settle it.

### Tag `4c`

`4c[0]` is stored as a diagnostic/error byte. `4c[1]` controls diagnostic state:

| Field | Confirmed behavior |
|---|---|
| low two bits both set | sets a diagnostic/update-gate bit |
| bit 3 or bit 5 | sets the high/sign bit of stored error code |
| bit 0 | sets another state bit and clears stored error code |

The central builder emits `4c 00 08` if its stored diagnostic byte is negative
and `4c 00 00` otherwise. Bit 3 is therefore an error-present forwarding path,
but exact error class is unknown. The manual lists floor, air, ambient, battery,
and RF communication failures. Both valid reports have `4c 00 00`.

### Tag `3b`

This byte is zero in every short capture. One parser context uses its high bit;
another uses bit 0, and a builder derives it from internal zone flags. With no
observed variation it must remain raw, not be named battery/demand/ack.

## Other known tags

The parser recognizes more than the nine capture-confirmed tags:

| Tag | Bytes | Use | Confidence |
|---:|---:|---|---|
| `0a` | 1 | special handler | Unknown |
| `10` | 1 | high-bit status forwarded into central state | Partial |
| `1a` | 1 | updates first `8e`-family bound | Strong lower-bound relation |
| `43` | 2 | capability/status pair | Unknown names |
| `5b` | 2 | stored as nonzero timer/duration while mode 04 | Strong Boost-timer relation |
| `5e` | 2 | second floor/external temperature | Confirmed |
| `64` | 2 | special handler | Unknown |
| `78` | 2 | numeric/status value plus forwarded flag | Partial |
| `80` | 3 | three independently stored state bytes | Unknown |
| `bb` | 3 | special handler | Unknown |
| `c0` | 4 | two structured u16/capability values | Partial |
| `c1` | 4 | four stored state bytes | Unknown |
| `da` | 4 | special handler | Unknown |
| `e1` | 4 | four stored bytes; also emitted by builder | Unknown |

Other builders emit grammar-valid tags `45`, `81`, `94`, `97`, `98`, `9a`,
and `b2` for other device/entity classes. They are absent from these thermostat
captures and should remain raw until their device types are known.

This resolves the suspected missing second-temperature record (`5e`) and proves
the tag table is broader than two sample layouts. A decoder should generically
retain every structurally valid record and add semantic fields only when sound.

## Annotated valid frames

### Compact command/state

```text
14                         length = 20
d0 90 4d 89                source = central
c6                         fixed marker
d0 37 46 54                destination = endpoint
03 01                      tag 03, controller association slot 01
df 00 11 01 00             full state S0..S3
3b 00                      flags
c9 0c                      MODBUS CRC, numeric 0cc9
16 07                      CC110L/CMS CRC, numeric 1607
```

### Report from endpoint `...4654`

```text
22                         length = 34
d0 37 46 54                source = endpoint
c6                         fixed marker
d0 90 4d 89                destination = central
8d 00 11 01                compact state
8a 02 84 03                active setpoint 64.4 F, Eco mode
4b 02 bf                   measured 70.3 F
cc 00 00 00 00             inactive floor-limit temperature pair
8e 0a 24 93                likely bound bytes 0a/24, flags 93/Air
4c 00 00                   no diagnostic
31 0d                      MODBUS CRC, numeric 0d31
98 a4                      CC110L/CMS CRC
```

### Report from endpoint `...4655`

```text
22 d0374655 c6 d0904d89
8d 001008
8a 02cc00                   active setpoint 71.6 F, Comfort
4b 02cf                     measured 71.9 F
cc 00000000
8e 0a2493
4c 0000
7492                        MODBUS CRC, numeric 9274
faf3                        CC110L/CMS CRC
```

## Decoder algorithm

1. Demodulate GFSK as NRZ/FSK PCM at about 26 µs/symbol.
2. Search for `d391d391`, preferably with alternating preamble context.
3. Read length and require exactly `length + 3` post-sync bytes when the outer
   CRC is present.
4. Require source, `c6`, destination, and both CRC fields.
5. Validate outer CRC over `frame[0:N-2]`.
6. Validate inner CRC over `frame[1:N-4]`, reading the wire value little-endian.
7. Walk `frame[10:N-4]` with `value_len=(tag>>6)+1`; reject any overrun or
   leftover byte.
8. Decode confirmed records and preserve unknown tags/bits as raw hex.
9. Keep provisional labels visible as provisional; never infer a changing
   state from a constant two-frame field.


## Remaining uncertainties and capture plan

The shortest route to complete human semantics is a controlled state matrix.
Keep raw IQ, timestamps, endpoint ID, central UI, thermostat display, and only
compare frames that pass both CRCs.

1. **Finish naming `03` and resolve the `02f0`→`0284` transition.** During pairing,
   record central zone number and device order to distinguish zone/member/RF
   slot. Separately select Comfort, Off, Frost, Eco, Boost, scheduled Comfort,
   and scheduled Eco; request two setpoints and record command/report order.

2. **Name `df/8d` bits.** At fixed temperature cross heat demand on/off, then
   independently toggle schedule/manual, Boost, window detection, keypad lock,
   and displayed acknowledgements.

3. **Confirm `8e[0:2]`.** Change the displayed minimum so native byte `0a`
   should become `0b`, and maximum so `24` should become `23`. Expected records
   are `8e 0b 24` and `8e 0a 23`; note whether `1a` is a delta update.

4. **Confirm `5e`, `cc`, and selector.** Cycle Air, Amb, FLR, and FLL. Make air
   and floor sensors differ and configure distinct nonzero floor limits. The
   scale and zero behavior are confirmed; this fixes `cc` field order.

5. **Resolve heat/cool and demand.** Switch Heating Only, Cooling Only, and
   Heating/Cooling, then cross demand in each. Correlate `8e[2]` bits 6/7 with
   `df/8d` and API `heating_up`/`heat_cool`.

6. **Map `4c` diagnostics.** Where safe, briefly disconnect a floor/external
   sensor and capture the displayed error. Use a controlled low-battery test,
   and restore the installation after each fault.

7. **Exercise unseen tags.** Capture Boost duration, pairing, an external-sensor
   zone, and other Watts entity types to expose `5b`, `5e`, and builder-only
   records without guessing.

8. **Physically verify direction.** Put the SDR close to one endpoint and then
   the central unit, reducing gain. Short/long RSSI should independently confirm
   the address-derived direction.

## References

- [rtl_433 issue #2885](https://github.com/merbanan/rtl_433/issues/2885)
- [Texas Instruments CC110L data sheet](https://www.ti.com/lit/ds/symlink/cc110l.pdf)
- [TI explanation of CC110L CRC coverage](https://e2e.ti.com/support/wireless-connectivity/sub-1-ghz-group/sub-1-ghz/f/sub-1-ghz-forum/1268097/cc110l-how-crc-is-calculated-and-on-which-bytes)
- [Watts BT-D03 thermostat guide](https://www.watts.eu/dfsmedia/0533DBBA-1771-4B1A-B581-AB07A4CBB521/639519-source/638956085080000000/User_guide_BT_D03_all_lang_01_20.pdf)
- [Community Watts Vision integration](https://github.com/pwesters/watts_vision)
- [rtl_433 integrity/MIC discussion](https://github.com/merbanan/rtl_433/issues/1964)
