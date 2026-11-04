"Voltcraft Energy Count 3000" sensor sold by Conrad
aka “Velleman NETBSEM4” 
aka “La Crosse Techology Remote Cost Control Monitor – RS3620”.

This Energy sensor sends FSK modulated packages at 868.3 MHz containing a.o:
- The unique ID for the plug (a 4 character hex number)
- The current power usage (in Watts)
- The maximum usage of the device (in Watts) since the start of the measurements
- The total energy usage (in Wh) since start of the measurements
- The time that the device was ‘on’
- The total time since the start of the measurements

For further details about the exact format of the packages see:
http://forum.jeelabs.net/comment/4972.html#comment-4972 and 
https://github.com/avian2/ec3k/blob/master/ec3k.py (function _decode_packet in class EnergyCount3KState)

Additional (historic) information can be found at:
https://www.tablix.org/~avian/blog/archives/2012/07/energycount_3000_part_2/ 
http://forum.jeelabs.net/comment/4020
https://batilanblog.wordpress.com/2015/02/17/using-ec3k-with-raspberry-pi/

I added several samples for different plugs, as I have quite a few active at the moment I can not give the exact sensor ID and readings that should result from correctly parsing the signal. 
If we can first obtain a bit stream it should be easy to write a parser based on the ec3k software mentioned above.

I will update samples and documentation soon with more details about plug-ID's and readings.
