# TS-FT002 Wireless Ultrasonic Tank Liquid Level Meter With Temperature Sensor

| FileName | Temp | Depth
| g001_433.92M_250k.cu8 | 21.4 (Celcius) | 1.30 (meters)
| g152_433.92M_250k.cu8 | 21.1 (Celcius) | 1.06 (meters)
| g274_433.92M_250k.cu8 | 22.3 (Celcius) | 1.30 (meters)
| g307_433.92M_250k.cu8 | 21.9 (Celcius) | 1.30 (meters)
| g474_433.92M_250k.cu8 | 20.6 (Celcius) | 1.30 (meters)
| g496_433.92M_250k.cu8 | 20.2 (Celcius) | 1.30 (meters)

PPM with 500 us pulse, 464 us short gap (0), 948 us long gap (1), 1876 us packet gap, two packets per transmission.

E.g. rtl_433 -R 0 -X 'n=TS-FT002T,m=OOK_PPM,s=464,l=948,g=1200,r=2000,bits>=70'

Bits are sent LSB first(!), full packet is 9 bytes (1 byte preamble + 8 bytes payload)

| Nibble | Function
| 0, 1   | Sync 0xfa / 0x5f
| 2, 3   | ID
| 4, 5   | Message tpye (0x11)
| 6- 9   | Depth HH,HL, LH,LL  (Value in hex *100 Fill with 5DC on invalid, range 0-15M)
| 10     | Transmit Interval ( Bit 7=0 180S,   Bit 7 =1  30S,  bit 4-6=1 5S)
| 11- 13 | Temp H, M, L (in hex *10, Max 1000, with 400 offset) If invalid read, filled with 3E8
| 14, 15 | Rain H, L (Value 0-256) I assume not used in XC-0331
| 16, 17 | CRC (include sync/preamble)
