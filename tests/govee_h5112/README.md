# Govee H5112 Dual-Probe Thermometer

https://www.govee.com/products/govee-h5112-refrigerator-thermometer

Battery-powered dual-probe thermometer that communicates via sub-GHz RF
(~912.375 MHz FCC nominal) to a separate Govee gateway hub. Shares the
RF sync word, CRC-16/AUG-CCITT, and 128-byte XOR key with the H5059 water
leak detector and H5310 pool/spa thermometer.

Probe 1 carries both temperature and humidity sensors; probe 2 is
temperature-only. The two probe connectors are physically keyed and cannot
be swapped.

## Capture notes

- Tuned frequency: 912.375 MHz (the FCC nominal; deviating by even 100 kHz
  pushes the signal to the filter edge at 250k sample rate and kills decodes).
- Sample rate: 250k is the correct value for H5112. The H5059/H5310 family
  normally needs ≥1 MS/s, but H5112 uses a narrower FSK deviation.
- Modulation: FSK_PULSE_PCM, short/long width 100 µs, reset_limit 2000 µs.

## Frame types

| File | Type     | id_wire      | Notes |
|------|----------|--------------|-------|
| g001 | Periodic | `0x04069cb2` | Autonomous 10-minute broadcast (msg_class 0x13). Includes 10-record history buffer. Both probes at room temperature; display-confirmed 23.6 °C on both probes at capture time. |
| g002 | Triggered | `0x08139cb2` | Gateway-triggered status response (msg_class 0x71). Sent in reply to a 0x70 network-test command. No history buffer. |
| g003 | Periodic | `0x0b279cb2` | Autonomous 10-minute broadcast, second physical unit (id_wire high-word 0x0b27). Probe 1 in refrigerator (~2.3 °C), probe 2 physically in a freezer at approximately −24 °C, read correctly as `temperature_2_C` ≈ −24.0 °C directly from the frame. |

## Probe 2 temperature encoding

Both probe temperatures and humidity are packed by the device's firmware into
one 32-bit little-endian word (`dec[6..9]`): an 11-bit field for probe 2, an
11-bit field for probe 1, and a 10-bit field for humidity, each at 0.1
units/count, zero-anchored at −40 °C for the temperature fields. Probe 2 is
read directly as an absolute value -- no per-device state, no wrap-count
tracking, no cold-start dependency. This is confirmed bit-exact against the
device's dumped/disassembled firmware (which contains the identical packing
function) as well as against real app-displayed readings spanning multiple
25.6 °C bands; see merbanan/rtl_433 PR #3568 for the full derivation.

## Device IDs

The low 16 bits of id_wire (`0x9cb2`) are a gateway pairing token shared by
all sensors bound to the same Govee gateway. The high 16 bits identify the
individual device and change on re-pairing. `id` is id_wire with its two
16-bit halves byte-swapped (the app-facing representation).
