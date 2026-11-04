# Schrader Electronics SMD3MA4 Tire Pressure Monitoring Transmitter

This TPMS model is found on certain Subaru vehicles.

## Observations

Does not normally transmit when idle. Transmits when moving or when pressure change exceeds threshold.
Can be stimulated to transmit by deflating, inflating, or tapping a finger gently on the valve stem at about 6HZ

## Protocol Information

Frame consists of a preamble followed by Manchester encoded ASK data for FLAGS, ID, and PRESSURE. There is no TEMPERATURE or CRC transmitted.

FCC ID: MRXSMD3MA4

https://fccid.io/MRXSMD3MA4/Test-Report/Test-Report-1131214

https://fccid.io/MRXSMD3MA4/Operational-Description/Description-2-1131211

Related project with diagrams:

https://github.com/JoeSc/Subaru-TPMS-Spoofing

## rtl_433 Status

Flag bits field (3-bits) is not documented and is output raw. The following values have been observed:

0x5 seems to correspond to "Wake Mode" (first transmission after long idle)

0x7 seems to correspond to "Drive Mode" (transmission every ~60 seconds when driving)

0x3 seems to correspond to "Pressure Remeasure" (pressure differs from previous sample)
