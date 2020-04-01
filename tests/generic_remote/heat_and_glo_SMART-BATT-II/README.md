This directory has samples from a Heat&Glo(tm) remote, model SMART-BATT-II,
FCC ID ULERF-5AN.

It has a single button on it, so the files listed are the transitions between
different states (e.g. flame off -> flame on, flame on -> thermo mode flame on, 
thermo mode flame on -> flame off, etc).

Note that the decoder assumes that there are 16 bits dedicated to addresses
and 8 to the data command. This is only valid for certain chips that the
decoder supports. This transmitter claims 2^20 addresses, so it uses 20 
bits for address and 4 for command. 

The filenames have text descriptions and the command in their names.

If the decoder is ever updated to distinguish addr/data modes, the
actual commands would be 1, 2, 3, and 4 instead of 97, 98, 99, and 100,
respectively.

State Diagram:

FLAME OFF ----> 97 ----> FLAME ON

FLAME ON ----> 98 ----> THERMO MODE, FLAME OFF (temp controlled)

FLAME ON ----> 97 ----> THERMO MODE, FLAME ON (temp controlled)

THERMO MODE, FLAME OFF ----> 98 ----> THERMO MODE, FLAME OFF (every 2 minutes)

THERMO MODE, FLAME OFF ----> 97 ----> THERMO MODE, FLAME ON (temp controlled)

THERMO MODE, FLAME OFF ----> 99 ----> OFF

THERMO MODE, FLAME ON ----> 100 ----> THERMO MODE, FLAME ON (every 2 minutes)

THERMO MODE, FLAME ON ----> 98 ----> THERMO MODE, FLAME OFF (temp controlled)

THERMO MODE, FLAME ON ----> 99 ----> OFF

THERMO MODE, FLAME ON ----> 99 ----> FLAME OFF
