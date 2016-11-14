Springfield PreciseTemp Wireless Temperature and Soil Moisture Station
http://www.amazon.com/Springfield-Digital-Moisture-Meter-Freeze/dp/B0037BNHLS

Data is transmitted in the following form:

Nibble
 0-1   Power On ID
  2    Flags and Channel - BTCC
          B - Battery 0 = OK, 1 = LOW
          T - Transmit 0 = AUTO, 1 = MANUAL (TX Button Pushed)
         CC - Channel 00 = 1, 01 = 2, 10 = 3
 3-5   Temperature Celsius X 10 - 3 nibbles 2s complement
  6    Moisture Level - 0 - 10
  7    Checksum of nibbles 0 - 6 (simple xor of nibbles)
  8    Unknown
  

springfield.1.data
{"time" : "@1.572864s", "model" : "Springfield Temperature & Moisture", "sid" : 212, "channel" : 1, "battery" : "LOW", "transmit" : "AUTO", "temperature_C" : 20.600, "moisture" : 0}
springfield.2.data
{"time" : "@1.572864s", "model" : "Springfield Temperature & Moisture", "sid" : 212, "channel" : 1, "battery" : "OK", "transmit" : "AUTO", "temperature_C" : 20.800, "moisture" : 0}
springfield.3.data
{"time" : "@1.572864s", "model" : "Springfield Temperature & Moisture", "sid" : 212, "channel" : 1, "battery" : "OK", "transmit" : "MANUAL", "temperature_C" : 20.800, "moisture" : 0}
springfield.4.data
{"time" : "@1.572864s", "model" : "Springfield Temperature & Moisture", "sid" : 212, "channel" : 1, "battery" : "OK", "transmit" : "AUTO", "temperature_C" : 21.600, "moisture" : 8}
