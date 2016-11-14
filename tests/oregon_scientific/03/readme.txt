Owl CM160 Energy sensor

Read data with rtl_433 -a -t -l 12000

Out:

pi@raspbmc:~/owlcm160/rtl_433/build/src$ ./rtl_433 -l 12000 -r gfile003.data
Registering protocol "Silvercrest Remote Control"
Registering protocol "Rubicson Temperature Sensor"
Registering protocol "Prologue Temperature Sensor"
Registering protocol "Waveman Switch Transmitter"
Registering protocol "Steffen Switch Transmitter"
Registering protocol "ELV EM 1000"
Registering protocol "ELV WS 2000"
Registering protocol "LaCrosse TX Temperature / Humidity Sensor"
Registering protocol "Acurite 5n1 Weather Station"
Registering protocol "Acurite 896 Rain Gauge"
Registering protocol "Acurite Temperature and Humidity Sensor"
Registering protocol "Oregon Scientific Weather Sensor"
Registering protocol "Mebus 433"
Registering protocol "Intertechno 433"
Registering protocol "KlikAanKlikUit Wireless Switch"
Registering protocol "AlectoV1 Weather Sensor (Alecto WS3500 WS4500 Ventus W155/W044 Oregon)"
Registering protocol "Cardin S466-TX2"
Registering protocol "Fine Offset Electronics, WH-2 Sensor"
Registering protocol "Nexus Temperature & Humidity Sensor"
Registering protocol "Ambient Weather Temperature Sensor"
Registering protocol "Calibeur RF-104 Sensor"
Registering protocol "X10 RF"
Registering protocol "DSC Security Contact"
Registering protocol "Brennstuhl RCS 2044"
Registering protocol "GT-WT-02 Sensor"
Registering protocol "Danfoss CFR Thermostat"
Registering protocol "Energy Count 3000 (868.3 MHz)"
Registering protocol "Valeo Car Key"
Registering protocol "Chuango Security Technology"
Test mode active. Reading samples from file: gfile003.data
current measurement reading value   = 11
current watts (230v)   = 177
Test mode file issued 1 packets


To test a checksum error:
pi@raspbmc:~/owlcm160/rtl_433/build/src$ ./rtl_433 -l 20000 -r gfile002.data
Registering protocol "Silvercrest Remote Control"
Registering protocol "Rubicson Temperature Sensor"
Registering protocol "Prologue Temperature Sensor"
Registering protocol "Waveman Switch Transmitter"
Registering protocol "Steffen Switch Transmitter"
Registering protocol "ELV EM 1000"
Registering protocol "ELV WS 2000"
Registering protocol "LaCrosse TX Temperature / Humidity Sensor"
Registering protocol "Acurite 5n1 Weather Station"
Registering protocol "Acurite 896 Rain Gauge"
Registering protocol "Acurite Temperature and Humidity Sensor"
Registering protocol "Oregon Scientific Weather Sensor"
Registering protocol "Mebus 433"
Registering protocol "Intertechno 433"
Registering protocol "KlikAanKlikUit Wireless Switch"
Registering protocol "AlectoV1 Weather Sensor (Alecto WS3500 WS4500 Ventus W155/W044 Oregon)"
Registering protocol "Cardin S466-TX2"
Registering protocol "Fine Offset Electronics, WH-2 Sensor"
Registering protocol "Nexus Temperature & Humidity Sensor"
Registering protocol "Ambient Weather Temperature Sensor"
Registering protocol "Calibeur RF-104 Sensor"
Registering protocol "X10 RF"
Registering protocol "DSC Security Contact"
Registering protocol "Brennstuhl RCS 2044"
Registering protocol "GT-WT-02 Sensor"
Registering protocol "Danfoss CFR Thermostat"
Registering protocol "Energy Count 3000 (868.3 MHz)"
Registering protocol "Valeo Car Key"
Registering protocol "Chuango Security Technology"
Test mode active. Reading samples from file: gfile002.data
Checksum error in Oregon Scientific message.  Expected: 4f  Calculated: 31
Message: 00 80 61 01 00 20 3a 5a 30 00 00 f4 17
