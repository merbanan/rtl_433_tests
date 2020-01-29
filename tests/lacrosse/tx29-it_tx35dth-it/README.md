# TX29-IT & TX35DTH-IT

Captured signals for LaCrosse compatible TX29-IT, made by Conrad 868 Mhz temperature. The TX9U-IT version is 915MHz, dont know if it use the same protocol. Also work for LaCrosse TX35 IT+ which use the same protocol, with humidty. Also compatible with StarMétéo sensor.

## Device Info

* Buy it online : http://www.conrad.fr/ce/fr/product/646282/
* Owner's Manual : FR : http://www.lacrossetechnology.fr/donnees/documents/produits/TX29IT+/PDF-fr-TX29IT+.pdf
* EAN: 4016138439489
* https://www.amazon.fr/Crosse-Technology-TX35-Capteur-temp%C3%A9rature/dp/B008MUSSNQ

## Device Notes

* Random Device ID - When the device is powered up (batteries are
  changed) it will generate a random ID byte that it will send with
  all transmissions.
* Messages are sent once.
* There is temperature and humidty in the same message. If (humidity & 0x7F == 0x6A) it meens there is no humidity sensor.

## Protocol Documentation

A nice page documenting how to decode the protocol is available here http://fredboboss.free.fr/articles/tx29.php/

Basically : 

* carrier frequency : 868.2 MHz
* modulation OOK
* transmit every 4 or 5 seconds.
* 64-bit messages (8 bytes, including preamble and crc)
* CRC is a CRC-8 with the polynom x8 + x5 + x4 + 1 (poly=0x31, int=0, final xor=0) of bytes 4 to 7
```
Example Data (gfile-tx29.data) : 
   a    a    2    d    d    4    9    2    8    4    4    8    6    a    e    c
Bits :
1010 1010 0010 1101 1101 0100 1001 0010 1000 0100 0100 1000 0110 1010 1110 1100
Bytes num :
----1---- ----2---- ----3---- ----4---- ----5---- ----6---- ----7---- ----8----
~~~~~~~~~ 1st byte
preamble, always "0xaa"
          ~~~~~~~~~~~~~~~~~~~ bytes 2 and 3
brand identifier, always 0x2dd4
                              ~~~~ 1st nibble of bytes 4
datalength (always 9) in nibble, including this field and crc
                                   ~~~~ ~~ 2nd nibble of bytes 4 and 1st and 2nd bits of byte 5
Random device id (6 bits)
                                          ~ 3rd bits of byte 5
new battery indicator
                                           ~ 4th bits of byte 5
unkown, unused
                                             ~~~~ ~~~~ ~~~~ 2nd nibble of byte 5 and byte 6
temperature, in bcd *10 +40
                                                            ~ 1st bit of byte 7
weak battery
                                                             ~~~ ~~~~ 2-8 bits of byte 7
humidity, in%. If == 0x6a : no humidity sensor
                                                                      ~~~~ ~~~~ byte 8
crc8 of bytes
```
CRC computing :
See http://www.sunshine2k.de/coding/javascript/crc/crc_js.html with custom with
Polynomial = 0x31
init = 0x00
final xor value = 0x00
On the previous example, CRC is calculated with bytes 4 to 7 (0x92 0x84 0x48 0x6a). Result is 0xec and must be equal to byte 8.

## Files

gfile gfile-tx29.data
Data : aa 2d d4 92 84 48 6a ec
Sensor : LaCrosse TX29 or TX35
Temperature : 4.8°C
Humidity : N/A (0x6a)
Newbatt : 0
Weakbatt : 0
CRC computed : 0xec
CRC received : 0xec

gfile gfile002-TX35DTH-IT.data
data : aa 2d d4 96 a6 41 22 50
Sensor : LaCrosse TX29 or TX35
Temperature : 24.1°C
Humidity : 34 
Newbatt : 1
Weakbatt : 0
CRC computed : 0x50
CRC received : 0x50

