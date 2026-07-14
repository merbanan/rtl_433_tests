Eberle Instat 868r1 Thermostat

https://www.eberle.de/products/underfloor-heating/hydronic/instat-868-r1?language=en

What I know about this item, mainly by analysis using URH and logging data by wire directly into an Arduino
  
868MHz, 2-FSK
Manchester encoded
Thermostat sends normally only on/off information to receiver unit, to switch heating. Fuzzy logic / timer etc is in controller chip of sender.

each protocol of 52 Bit is send in 3 repetitions, typical protocol:
0000000000001111111000000011000110011001010110101001100110101010011001010101010110

beginning is atypical for FSK:
000000000000111111100000001100

this is code part:
0110011001010110101001100110101010011001010101010110

I'm not sure that a protocol is adequalty captured in uploaded files, because of FSK seems not identified well. This is for version 0204 at the moment, I have also a sender with version 0101 having a different (smaller) delta in FSK and different, but also atypical beginning before code part

A sender has to be learned in to the receiver before use, and 3 modes of sending have been identified:
- learn
- reset
- switch on / switch off

What I suppose to found out is in protocol.txt, further protocols are uploaded
