# Celsia CZC1

Manual available at https://www.celsiasystems.co.uk/wp-content/uploads/2014/03/czc1-user-guide.pdf
A PID thermostat used by various heater manufacturers (e.g. Consort, Energy Products Group, Sunflow)


## Decoding

|       |         |
|-------|---------|
| demod | OOK_PCM |
| short | 1220    |
| long  | 1220    |
| reset | 4880    |

A packet starts with a preamble of {40}cccccccccccccccccccc, followed by a sync
of {32}55555555 signalling the start of the data symbols. The packet is
terminated with {8}f0.  Each symbol is 4 'raw' bits long: 0101(5) = 0, 1010(a)
= 1. Command packets have 5 bytes of data, pairing packets have 4.

```
rtl_433 -X n=CZC1,m=OOK_PCM,s=1220,l=1220,r=4880,preamble=cccccccc55555555
```

## Data layout

Command packet (5 bytes):

- ID:   {16} ID
- Type: {8}  type
- Heat: {8}  heating level 0-255 (little endian unsigned integer)
- CRC:  {8}  CRC-8, poly 0x31, init 0xd7

Pairing packet (4 bytes):

- ID:   {16} ID
- Type: {8}  type
- CRC:  {8}  CRC-8, poly 0x31, init 0xd7


## Samples

| Sample                     | Code       | ID   | Type | Heat      | CRC |
|----------------------------|------------|------|------|-----------|-----|
| g001_433.92M_250k.cu8      | f0d3f0ec0f | f0d3 | heat | 055       | 0f  |
| g047_433.92M_250k.cu8      | f0d3f0aba5 | f0d3 | heat | 213       | a5  |
| g058_433.92M_250k.cu8      | f0d3f000b3 | f0d3 | heat | 000 (off) | b3  |
| g676_433.92M_250k.cu8      | f0d3f0ff1f | f0d3 | heat | 255 (max) | 1f  |
| pair_g002_433.92M_250k.cu8 | f0d30073   | f0d3 | pair | --        | 73  |

### Observed codes (samples not included)

These codes are from monitoring 3 thermostats for a 24 hour
heating cycle, as well as manually pressing the pair button on each.

| Code       | ID   | Type      | Heat      | CRC       |
|------------|------|-----------|-----------|-----------|
| f0d3f000b3 | f0d3 | f0 (heat) | 000 (off) | b3        |
| f0d3f0853c | f0d3 | f0 (heat) | 161       | 3c        |
| f0d3f0aba5 | f0d3 | f0 (heat) | 213       | a5        |
| f0d3f0c0f4 | f0d3 | f0 (heat) | 003       | f4        |
| f0d3f0d611 | f0d3 | f0 (heat) | 107       | 11        |
| f0d3f0ec0f | f0d3 | f0 (heat) | 055       | 0f        |
| f0d3f0ff1f | f0d3 | f0 (heat) | 255 (max) | 1f        |
|            |      |           |           |           |
| 2750f00017 | 2750 | f0 (heat) | 000 (off) | 17        |
| 2750f08598 | 2750 | f0 (heat) | 161       | 98        |
| 2750f0ab01 | 2750 | f0 (heat) | 213       | 01        |
| 2750f0c050 | 2750 | f0 (heat) | 003       | 50        |
| 2750f0d6b5 | 2750 | f0 (heat) | 107       | b5        |
| 2750f0ecab | 2750 | f0 (heat) | 055       | ab        |
| 2750f0ffbb | 2750 | f0 (heat) | 255 (max) | bb        |
|            |      |           |           |           |
| ec46f00087 | ec46 | f0 (heat) | 000 (off) | 87        |
| ec46f08c80 | ec46 | f0 (heat) | 049       | 80        |
|            |      |           |           |           |
| f0d30073   | f0d3 | 00 (pair) | --        | 73        |
| 2750001d   | 2750 | 00 (pair) | --        | 1d        |
| ec460096   | ec46 | 00 (pair) | --        | 96        |
|            |      |           |           |           |
| f0d3f0008  | f0d3 | f0 (heat) | 000 (off) | 08 (Fail) |
| f0d3f000b0 | f0d3 | f0 (heat) | 000 (off) | b0 (Fail) |
| ec46f00080 | ec46 | f0 (heat) | 000 (off) | 80 (Fail) |
