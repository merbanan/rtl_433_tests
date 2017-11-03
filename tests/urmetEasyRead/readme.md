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

- In folder 01 are stored grabbed signals from the SR_P when the SR 
  is NOT in listening mode. Acting on the reed sensor I get 15 different 
  signals spaced 1sec each other. 
  - First test is from gfile001 to gfile015 
    - gfile001 seems to be an FSK packet
    - gfile002 to 005 are OOK package (maybe a wakeup signal)
    - gfile006 another FSK package
    - gfile007 OOK package
    - gfile008 and 009 FSK package
    - gfile010 and 011 OOK
    - gfile012 FSK
    - gfile013 and 014 OOK
    - gfile015 FSK
  - Second Test gfile016 to 030
    - all OOK
  - Third Test gfile031 to 045
    - gfile031 OOK
    - gfile032 FSK
    - gfile033 to 042 OOK
    - gfile043 FSK
    - gfile044 OOK
    - gfile045 FSK

- In folder 02 are stored the files when the SR is in receiving/test mode. 
  Every time i've used the reed on the SR_P the SR beeps and i get 
  2 transmissions (before were 15)
  -First Test gfile045 and 046
   - 045 FSK
   - 046 OOK
  -Other Tests
   - 047 to 049 FSK

   - 050 OOK
   - 051 FSK

   - 052 OOK
   - 053 FSK

   - 054 OOK
   - 055 FSK

   - 056 OOK
   - 057 FSK
