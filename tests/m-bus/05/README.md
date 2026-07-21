# Wireless M-Bus: ELL-wrapped real captures

Real captures at 868.6 MHz, `-g 20`, showing the ELL-unwrap fix in
`m_bus.c` against live traffic (not just the earlier fixtures' original
recordings):

- `g001`/`g003`: a KAM Cold Water meter (id 74433908) whose ELL is
  *not* encrypted and unwraps to CI `0x79` -- EN 13757-3 "compact frame,
  no header". Not decoded further: compact frames reference a
  previously-transmitted format definition (a DIF/VIF sequence cached
  by manufacturer/type/format-signature, per wmbusmeters) that this
  decoder doesn't track across telegrams. Correctly left as raw hex
  rather than guessed at.
- `g002`: the KAW Cold Water meter from the other fixtures here, still
  AES-128 CTR encrypted at the ELL layer, same as before.
