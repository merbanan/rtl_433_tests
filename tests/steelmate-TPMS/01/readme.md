Steelmate TPMS

A google search indicates Steelmate uses infineon as their supplier of TPMS chips:
http://www.chinaseniorsupplier.com/Automobiles_Motorcycles/Vehicle_Tools/60319882933/2015_SteelmateTP_S1_I_infineon_tpms_for_car_tpms_system_accessories_of_keys.html

infineon TPMS (SP37) datasheets:
http://www.infineon.com/dgdl/SP37_RF_v1.0.pdf?fileId=db3a30433899edae0138c2ade4bb01cf
http://www.infineon.com/export/sites/default/cn/product/promopages/ATV_Symposium/China_ATV_Symposium_TPMS.pdf

Technical details:
	315 or 433.92MHz frequency
	ASK or FSK modulation
	Manchester/Biphase encoding

As Steelmate's UK website has only one SKU for replacment sensors, they are probably all encoded identically 
for the various receivers they sell. As per 
 http://www.aliexpress.com/store/product/Steelmate-T8209-two-way-Touch-Screen-Car-alarm-USB-Charger-FSK-Technology-Long-Distance-Trunk-Release/1330454_32310580802.html
FSK is most likely the modulation they use, at least for the 433.92MHz model they sell in the UK.


The 'a' file was created running 'rtl_433 -a' with the 'A' file created by running 'rtl_433 -A', and redirecting the output
to the text file. The capture files themselves were created running 'rtl_433 -a -t'


While chip has an 125KHz LF receiver, this may not have been enabled by Steelmate, therefore as the documentation 
states the vehicle speed must exceed 20KM/h for the sensors to turn on, the capture information was generated 
by driving through the city, and may have picked up data from other transmitters, including other cars using 
OOK or ASK encoding. These "false" datapackets should be discarded. The car receiver showed values of between 34 and 39 PSI.

As per above, its possible Steelmate TPMS devices uses infineon SP37, or similar, FSK on 433.92Mhz and Manchester encoding.
