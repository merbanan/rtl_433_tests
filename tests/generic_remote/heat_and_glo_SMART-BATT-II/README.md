This directory has samples from a Heat&Glo(tm) remote, model SMART-BATT-II,
FCC ID ULERF-5AN.

It has a single button on it, so the files listed are the transitions between
different modes (e.g. off -> on, on -> themostat mode, thermo mode -> off).

Note that the decoder assumes that there are 16 bits dedicated to addresses
and 8 to the data command. This is only valid for certain chips that the
decoder supports. This transmitter claims 2^20 addresses, so it uses 20 
bits for address and 4 for command. 
