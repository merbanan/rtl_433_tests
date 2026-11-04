IBIS vehicle information beacon, which is used in public transportation.

It's a continuous UHF beacon with vehicle information not the selective VHF
Transit signal priority (TSP) signal.

The packet is 28 manchester encoded bytes with a Preamble of 0xAAB and 16-bit
CRC, containing a company ID, vehicle ID, door-opening-counter, and various flags.

The packets are randomly spaced with an average around 90 packets per minute.
Use a samplerate of 1024k for reliable detection as the pulses are rather short.

The sample contains two packets recorded at 2560k.
