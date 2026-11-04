# TPMS Hyundai Elantra 2012

## From FCC website

This transmitter is a transmitter device with tire valve, which is mounted in the valve hole of the wheel rim and transmits the pressure and temperature inside the tire, the battery voltage of the transmitter, and the tire identification code (ID) at normal and abnormal condition with the radio wave (RF) that conforms to the used area. Also this device has a countermeasure function such as the random delay of transmission time so that the RF signal from each tire will not interfere due to the simultaneous transmission. The transmitter device also has a Low Frequency (LF) receiver. This receiver supports Low Frequency (LF) magnetic field communications allowing the changing of measurement/monitoring states of the transmitter by commands sent via the TPM diagnostic tool. The RF signal operates at 315 MHz and uses FSK Manchester code modulation. 225816-101 transmits 4 RF packets every 200 seconds.

### Operations

Storage Mode:
No transmission. Measures temperature & pressure
4 words when activation occurs with TPM diagnostic tool

Normal Mode:
Measures temperature and pressure. Transmits periodically. Enters this mode from storage when pressure goes above threshold.
- 4 words every 210 seconds
- 4 words when activation occurs with TPM diagnostic tool

Alert Mode:
Transmits when:
a) significant pressure delta detected b) high temperature is detected
8 words every 4 seconds for 1 minute

## Decoding

    PPTT IDID IDID FFCC

- Pressure in hex(One byte PP) to dec +60 = pressure in kPa
- Temperature hex(One byte TT) to dec -50 = temp in C
- ID in hex(2 Words = 4 bytes)
- Flags (FF) = ???? ?SBT (Missing Acceleration, market - Europe/US/Asia, Tire type, Alert Mode, park mode, High Line vs Low Line etc)
  - S=Storage bit
  - B=Battery low bit
  - T=Triggered bit
  - C0 =1100 0000 = Battery OK, Not Triggered
  - C1 =1100 0001 = Battery OK, Triggered
  - C2 =1100 0010 = Battery Low, Not Triggered
  - C3 =1100 0011 = Battery Low, Triggered
  - C5 =1100 0101 = Battery OK, Triggered, Storage Mode
  - E1 =1110 0001 = Mx Sensor Clone for Elantra 2012 US market ? Low Line
  - C1 = Mx Sensor Clone for Genesis Sedan 2012 US market ? High Line
- CC = CRC8, poly 0x07, init 0x00
