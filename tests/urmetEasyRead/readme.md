# Urmet EasyRead SR_P

Data from the Urmet EasyRead SR_P. The device purpose is Gas 
Telemetry. 
http://www.tlc.urmet.it/wp-content/uploads/pdf/easy_read.pdf
The base Station is the Urmet EasyRead SR, that works 
like an hub for one or more (max 8) SR_P module, collects and sends data 
via SMS or GPRS (and/or on 169Mhz  as specification but not used in my case).
Comunication between SR and SR_P is declared on 868/925Mhz ISM band, 
in my case center frequency is 868.28Mhz. 

- Environment:

In my case the SR works like an hub for a single SR_P and is also directly 
connected to the GPL gas meter, probably reads of measured data are 
invoked by Gas Seller via SMS or GPRS (my versions is equiped with sim card)

The SR_P is wired to the hall sensor of the GPL tank and measures how much 
percentage of Gas is stored. No idea of when data is transmitted, probably 
by Seller request (monthly) and/or when Gas quantity changes are detected. 
(now my receiver is waiting for next transmission)

Data is collected by forcing the SR_P to transmit using the reed sensor on 
the left, it's also possible to take the SR in receiving mode (like a pairing)
with the reed sensor on SR top.

Actually the tank is at 24-25%

- My purpose is to get the communication between SR and SR_P and get tank level .
- First is to get packet "readable" for further investigation

- In folder 01 are stored first grabbed signals at different sample rate 

- In folder 02 are stored the latest files grabbed. Sample rate is 2M 

- In folder 03 there are newest files (grabbed the same of folder 02) but renamed including   timestamp

- In folder tool there are: grc flow chart used for demod, python code for demod, python code for decode (work in progress)
  
A spanish manual of the device can be found at: https://fccid.io/ANATEL/04171-13-04439/Manual-EASY-READ-SRP-BRA/8D3562AD-1F22-4A62-B89C-6C89D599ADB5

Actual data investigation is stuck on clock recovery. I've found a 101010etc 
preamble but no success on detrmine sync word, data and crc

Device make 3 transmission at time, didn't know if all from sender (SR_P) or
also from receiver (SR)

Update 2017-8-12
Transmission are daily
Assuming that packet could contain a timestamp, new data is renamed including creation time. (Tank level is now between 15-20%) 
