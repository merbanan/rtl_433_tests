FCC : Data obtained by an IR-reader/sensor is transmitted in form of short bursts 
every 28.5 to 31.5 seconds on 433.92 MHz (single frequency). The carrier is On/Off pulse modulated
 (logic ‘1’: 0.5ms TX-on followed by 2ms TX-off, logic ‘0’: 0.5ms TX- on followed by 4ms TX-off).


Info from https://github.com/CapnBry/Powermon433/blob/master/arduino/Powermon433/Powermon433.ino
ESP8266 port : https://github.com/kissste/ESP8266-Powermon433



Packet is 3 bytes? (CapnBry source, line 493)
Plus preamble

TxWireval has more info, line 224:
     // The header is 11111110 and a short duration pause
     // Which will come out as SS SS SS SS SS SS SS SL*1.5

** Low battery is transmitted apparently
https://github.com/CapnBry/Powermon433/blob/master/arduino/Powermon433/Powermon433.ino line 347


capture:
rtl_433 -S unknown
capture limesdr:
rtl_433 -d "" -g "" -S unknown

analyze:
rtl_433 -A -r g00* -X "name=blueline,modulation=OOK_PPM,short=2000,long=4000,sync=500,gap=7000,reset=58000"


Starting at line 561:

device ID:
g_TxId = decoder.data.raw[1] << 8 | decoder.data.raw[0];

CRC OK:
crc8(decoder.data.raw, 3) == 0

decode, 4 packet types
ID 0
INSTANT power consumption 1
TEMP 2
TOTAL power consumption 3

uint16_t val16 = decoder.data.val16[0];
val16 -= g_TxId;


decodePowermon(val16 & 0xfffc)
  switch (decoder.data.raw[0] & 3)
  {
  case OOK_PACKET_INSTANT: (1)
    // val16 is the number of milliseconds between blinks
    // Each blink is one watt hour consumed
    g_RxWatts = 3600000UL / val16;
    break;

  case OOK_PACKET_TEMP: (2)
    g_RxTemperature = temp_lerp(decoder.data.raw[1]);
    g_RxFlags = decoder.data.raw[0];
    break;

  case OOK_PACKET_TOTAL: (3)
    g_RxWattHours = val16;
    break;