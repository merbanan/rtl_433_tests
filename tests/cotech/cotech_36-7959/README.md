# Cotech 36-7959 weatherstation

Believe the weatherstation is a branded version of [UNIT CONNECTION TECHNOLOGY's model _FT020](http://www.uctechnologyltd.com/prod_view.aspx?TypeId=29&Id=265&FId=t3:29:3).

Flexcoder
```
rtl_433 -X n=cotech-36-7959,m=OOK_MC_ZEROBIT,s=488,r=1200,preamble={12}014
```

Running _reveng_ to reverse engineer the CRC calculation
```
reveng -w 8 -s [samples from flexcoder]
 Result: width=8  poly=0x31  init=0xc0  refin=false  refout=false  xorout=0x00  check=0x0d  residue=0x00  name=(none)
```

## Data mappings

- 4 bits = Never changes
- 8 bits = Changes when replacing batteries or when resetting device, probably an id
- **1 bit**  = 0 = Ok battery, 1 = Low battery
- **1 bit**  = Wind direction is defined by a byte later on in the sequence. When degrees are over 255 (byte max value) this value is set to 1 and the wind direction starts from 1 again. So when this is = 1 it basically means "wind direction value + 255"
- **1 bit**  = Wind and gust are also defined by a byte later on in the sequence. Specification states it can show wind strength up to 50m/s. Guessing this bit works same as previous bit for wind direction i.e. if this is set to 1 wind (or gust) is equal to (wind value + 255) / 10
- **1 bit**  = same as above. Don't know which is which... need to bring out the compressor and manually create some strong wind.
- **8 bits** = Wind, decimal value / 10 to get m/s
- **8 bits** = Gust, decimal value / 10 to get m/s
- **8 bits** = Wind direction, decimal value for degrees
- **4 bits** = Always the same, 4 zeros, no clue... might belong to the following rain value
- **_12 bits_** = Rain value / 10 => mm. Don't know if this is actually 12 bits, if it cycles or how it works. So far I have only seen this value increasing (exept for when device was reset). Might also contain the previous 4 bits
- 4 bits = Always the same, 1000, no clue
- **12 bits** = Temperature. This value is given in fahrenheit with the formula: (value - 400) / 10
- **8 bits** = Humidity, decimal value giving the percentage
- 24 bits = Always the same, crc-padding?
- **8 bits** = CRC8 Checksum (width=8  poly=0x31  init=0xc0  refin=false  refout=false  xorout=0x00  check=0x0d  residue=0x00)