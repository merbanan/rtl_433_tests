Schrader FSK Manchester TPMS, as fitted to the Hyundai i20 2021.
Vendor: Schrader Electronics (Sensata). One decoder covers two factory part numbers:
  52940-BV100 / AFFPA4 / FCC MRXAFFPA4 (IC 2546A-AFFPA4)
  52940-E2100 / BG6FD4 / FCC MRXBG6FD4 (IC 2546A-BG6FD4)

RF: FSK, Manchester coded (52.18 us half-bit), polarity inverse of IEEE 802.3.
9-byte frame, additive checksum sum(b0..b7) & 0xFF == b8.
Fields: 32-bit id, pressure (PSI, 0.25 per count, no offset), temperature (C),
byte7 transmit-mode/status (partial enumeration: 0x1c rolling, 0x01 pressure-change
alert on rapid fall or rise), burst counter, sequence.

Captures (433.92 MHz, 1 Msps CU8):
  g001 - BG6FD4 sensor 9187740a, rolling burst (4 frames)
  g002 - BG6FD4 sensor 9187740a, pressure alert (byte7=0x01), deliberate deflation.
         This capture is a single ~1.2 s burst, so pressure reads steady across its
         frames; deflation lowers pressure only over tens of seconds, which one short
         capture does not span. (byte7=0x01 is what this sample demonstrates.)
  g003 - AFFPA4 sensor 861cd397, rolling burst (4 frames) -- confirms one decoder
         handles both part numbers

Captures (433.92 MHz, 250 ksps CU8), recorded in the car during a controlled
deflation/inflation test (pressure alert bursts, byte7=0x01, also while stationary):
  g004 - AFFPA4 sensor 861cd61b, alert while the tire is deflated (30 PSI)
  g005 - AFFPA4 sensor 861cd397, alert while the tire is emptied (12.5 PSI)
  g006 - AFFPA4 sensor 861cd397, alert with the tire empty: raw pressure 0 (0 PSI)
  g007 - AFFPA4 sensor 861cd397, alert while the tire is re-inflated (19.25 PSI):
         the alert also fires on a pressure rise

Photos (regulatory label, read as is from the physical sensors):
  sensor_new_BG6FD4.jpg - 52940-E2100 / BG6FD4, FCC MRXBG6FD4, IC 2546A-BG6FD4,
                          ID 9187740A (the sensor recorded in g001/g002)
  sensor_old_AFFPA4.jpg - 52940-BV100 / AFFPA4, FCC MRXAFFPA4, IC 2546A-AFFPA4,
                          ID 861CD414. This is the original front-left sensor, which
                          was damaged and replaced (hence photographed off the wheel);
                          it does not appear in the recordings. It documents the AFFPA4
                          model, the same model as sensors 861cd397/861cd61b (g003-g007).

FCC filings (public - internal photos, test reports; independently confirm FSK
modulation, frame/burst structure and 433.92 MHz operation):
  AFFPA4:  https://fccid.io/MRXAFFPA4
  BG6FD4:  https://fccid.io/MRXBG6FD4
Grantee: Schrader Electronics (FCC grantee code MRX, IC 2546A; now Sensata).
