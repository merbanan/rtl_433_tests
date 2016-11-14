There are 5 SL109H sensors, but the 3 of relevance are Ids 134, 140, and 188 (the 38-bit messages from the sensors end in 218, 230, and 2f0, respectively).
The data are in the <seconds-past-the-epoch>.gfile.data files.
The reference data are in the <seconds-past-the-epoch>.text files; they consist of 2 Acurite Temperature/Relative-Humidity sensors

Most of the message has been decoded, but there is some uncertainty for portions of it.

bits 0:3 are the checksum: add up bits 6:37; then add the channel bit pattern; then mod 16
bits 4:5 are the channel: channels 1,2,3 correspond to bit patterns 1,2,0
bits 6:13 are the BCD relative humidity percentage
bits 14:25 is a 12-bit signed integer representation of the temperature in hundredths of degrees Celsius
bits 26:29 presumably some sort of status message; uncertain as to what each bits means; however, some observations:
                1st bit on correlates with rising temperature
                2nd bit on correlates with falling temperature
                    (both seem to go back to 0 after approximately an hour of no temperature change)
                presumably, one of the other 2 bits is battery status
                relative humidity changes don't appear to have influence; but that's uncertain
bits 30:37 rolling ID code (changes on battery change or reset button press)
