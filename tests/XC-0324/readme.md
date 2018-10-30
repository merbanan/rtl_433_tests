# XC-0324 Weather Station Transmitter
http://www.jaycar.com.au/spare-thermometer-sensor-to-suit-xc0322/p/XC0324

Receiver also pictured, XC0322
http://www.jaycar.com.au/wireless-in-out-thermometer-and-hygrometer/p/XC0322

* Outdoor (stronger signal) was around 10.3-10.2 degrees C
* Indoor (weaker signal) was around 20.6 degrees C

![XC-0324 on left](IMG_20160726_221502.jpg)
![XC0322 on right](IMG_20160726_221449.jpg)


# Updated October 2018

* Existing sampled .cu8 files moved to XC-0324/01/ subdirectory.
* Additional sample .cu8 files created in 02/, and 03/
  subdirectories.
* The 02 subdirectory contains "good" data,

  + some lower temperatures (8.4, 85. 8.6 C),
  + some values around 11.2 C (where the 3rd nibble in the temperature
    value becomes important)
  + a run of medium temperatures (14.1 - 16.0 C), and
  + a higher temperature (21.6 C).

* The 03 subdirectory contains "damaged" but still useable samples

  + one or more of the three repeats of the message has a checksum error.
* Two different sensors (ids 56 and 64) are represented in the samples.
  Transmissions from each sensor are interspersed in the sample
  directories.
* Each subdirectory contains a ReferenceValues.csv file, containing the
  "correct" temperature value corresponding to each sample file.

These newer samples are from two separate XC-0324 transmitters.

The oldest sensor transmits a "clean" pulse (ie a captured pulse,
examined using Audacity, has pretty stable I and Q values, ie little
phase wandering)

The newer sensor transmissions seems less stable (ie within a single
pulse, the I and Q components of the pulse signal appear to "rotate"
through several cycles).  Some of the sampled transmissions from the
newer sensor are too corrupted to be decoded.

The `-a -t -D -D` output correctly guesses the older sensor's modulation
and gap parameters, but mistakes the newer transmitter as pulse width
modulation with "far too many" very short pulses.

There is a prototype decoder for the XC-0324 transmitter almost ready
for submission.  A version of that was used to create the
ReferenceValues.csv files mentioned above.

The "correct" values in the 02/ and 03/ Reference.csv files have
been validated manually against records taken as the samples were
recorded.

The values in the 01/ ReferenceValues.csv agree very closely with the
values reported in the original version of this readme.md file.


