# NEXA LMST-606 Magnetic sensor

![NEXA LMST-606](https://github.com/LinuxChristian/rtl_433_tests/blob/79afdf7ff1f9528cccc54212f703ca171042e960/tests/nexa_LMST-606/nexa_magnetic_sensor.jpg "NEXA LMST-606")

Protocol
Very similar to the Proove magnetic door and window sensor. The Proove
device will however only decode the OFF-state since NEXA sends 64-bits when off
while it sends 72-bits to signal the ON-state.

Nexa OFF packet structure (32 bits):  
HHHH HHHH HHHH HHHH HHHH HHHH HHGO CCEE  
H = The first 26 bits are transmitter unique codes, and it is this code that the reciever learn recognize.  
G = Group code. Set to 0 for on, 1 for off.  
O = On/Off bit. Set to 0 for on, 1 for off.  
C = Channel bits.  
E = Unit bits. Device to be turned on or off. Unit #1 = 00, #2 = 01, #3 = 10.

Physical layer.
Every bit in the packets structure is sent as two physical bits.
Where the second bit is the inverse of the first, i.e. 0 -> 01 and 1 -> 10.
Example: 10101110 is sent as 1001100110101001
The sent packet length is thus 64 bits.

The ON packet structure is very similar but encoded 72-bits.

## Files

Two examples are included using the same sensor,

* gfile001.data : OPEN-state
* gfile002.data : CLOSED-state

## External information

* Product webpage: https://www.nexa.se/vara-produkter/system-nexa/sensorer/lmst-606#tab-id-1
* General NEXA protocol: http://elektronikforumet.com/wiki/index.php/RF_Protokoll_-_Nexa_sj%C3%A4lvl%C3%A4rande
