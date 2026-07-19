# Mercator ceiling fan remote control

See https://github.com/merbanan/rtl_433/issues/2200 for the original request.

Flex decoder config: `conf/Mercator.conf` in the main rtl_433 repo, reverse
engineered by @klohner and confirmed working against these real captures by
the original reporter.

OOK_PCM, 43 bit message, 3-chip symbols, fixed 20 bit sync word after a 1 bit
preamble. Button is a 6 bit one-hot field at bit offset 6.

- 01/ - one real capture from the original reporter (g001=MED). Uses a
  `protocol` file pointing at `Mercator.conf` since this is a flex-decoder
  config, not a compiled-in decoder.
- codes_test.txt/json - all 5 buttons (g001=MED, g002=LOW, g003=OFF,
  g004=HI, g005=LIGHT), as raw pre-symbol-decode frames captured from all 5
  real files posted in the issue (not just the one kept as a full .cu8
  above). Verified with
  `rtl_433 -R 0 -c conf/Mercator.conf -y '<code>' -F json`. Also uses a
  top-level `protocol` file pointing at `Mercator.conf`, same reason as
  `01/`'s.
