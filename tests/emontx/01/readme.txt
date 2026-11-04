This is the emonTx from http://openenergymonitor.org/emon/modules/emonTxV3

It uses the JeeLibs packet format as described at
http://jeelabs.org/2011/06/09/rf12-packet-format-and-design/index.html and
http://jeelabs.org/2011/06/10/rf12-broadcasts-and-acks/index.html

It runs quite fast, so a sample rate of 2500000 was needed to get a 
reasonable capture. Note that gfile001.data actually needs short_limit
set to 5.1 (which is kind of hard, as it's an integer) in order to decode
properly...


