# Cavius door/window sensor

A different, simpler protocol than the smoke/heat/water alarms in the
parent directory: raw FSK_PCM (not Manchester coded), around
868.65-868.70 MHz, 415 us per bit. See
https://github.com/merbanan/rtl_433/issues/2562.

Packet, all following the preamble:

    AA AA AA D3 15 27  UU  II II II II II II  SS  CC

- Preamble: 0xaaaaaa (alternating) then a fixed sync 0xd31527.
- U: 1 byte, varies between transmissions; likely a sequence/retransmission
  counter, not confirmed. Reported as `counter`.
- I: 6 byte device ID, fixed per sensor.
- S: 1 byte state: 0x25 (open) or 0x24 (closed) -- the only two values ever
  observed in the issue thread. Any other value is rejected.
- C: CRC-8 (poly 0x07, init 0x00) over U, I, and S.

Every capture submitted in the two-year-old issue thread was too weak for
rtl_433's automatic pulse detector at default settings (extensively
discussed: wrong tuner, clipping, gain, distance). Two captures here
(`OPEN_g031_868.68M_250k.cu8`, `CLOSE_g036_868.68M_250k.cu8`) do decode,
but only with a lower manual detection level (`-Y level=-14` or similar)
-- a `demod` file supplies that flag to `run_test.py`, so this directory
runs in the normal regression suite. Verify manually:

    rtl_433 -r OPEN_g031_868.68M_250k.cu8 -Y level=-14 -F json
    rtl_433 -r CLOSE_g036_868.68M_250k.cu8 -Y level=-14 -F json

`codes_test.txt`/`codes_test.json` cover two more known-good frames
manually transcribed in the issue thread, for which no `.cu8` capture is
available.
