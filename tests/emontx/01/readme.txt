This is the emonTx from http://openenergymonitor.org/emon/modules/emonTxV3

It uses the JeeLibs packet format as described at
http://jeelabs.org/2011/06/09/rf12-packet-format-and-design/index.html and
http://jeelabs.org/2011/06/10/rf12-broadcasts-and-acks/index.html

It runs quite fast, so a sample rate of 2500000 was needed to get a 
reasonable capture.

The actual data from the first capture isn't known, although there'll be
a lot of zeroes because few of the sensors were connected.

For gfile002.data the corresponding output on the serial port was:

CT1 CT2 CT3 CT4 VRMS/BATT PULSE                                                 
1156 1 1077 61 24014 1085                                                       

