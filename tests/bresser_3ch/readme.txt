Test data for the wireless Temperature/Humidity outdoor sensor
Bresser Thermo-/Hygro-Sensor 3CH

Art. Nr.: 7009994
EAN: 4007922031194
http://www.bresser.de/Wetter/BRESSER-Thermo-Hygro-Sensor-3CH-passend-fuer-BRESSER-Thermo-Hygrometer.html

Bresser also has two other Thermo-/Hygro-Sensors types most likely using different protocols:

- Bresser Thermo-/Hygro-Sensor 5CH (7009993)
- Bresser Thermo-/Hygro-Sensor 3CH (7009994)
- Bresser Thermo-/Hygro-Sensor 3CH for Temeo (7009995)


The sensor sends 15 identical packages of 40 bits each ~60s.
The bits are PWM modulated with On Off Keying.
Transmissions also include channel code, sync id, batt-low, and test/sync.

 +----+  +----+  +--+    +--+      high
 |    |  |    |  |  |    |  |
 |    |  |    |  |  |    |  |
-+    +--+    +--+  +----+  +----  low
 ^       ^       ^       ^       ^  clock cycle
 |   1   |   1   |   0   |   0   |  translates as
 Each transmission is 40 bits long (i.e. 29 ms, 36 incl. preamble)
 Data is transmitted in pure binary values, NOT BCD-coded.
 Temperature is given in Centi-Fahrenheit and offset by 900.

Burst length is ~36ms (41 pulses + 8 syncs) * 750us.

CH1 has a period of 57 s
CH2 has a period of 67 s
CH3 has a period of 79 s

A short pulse of 250 us followed by a 500 us gap is a 0 bit,
a long pulse of 500 us followed by a 250 us gap is a 1 bit,
there is a sync preamble of pulse, gap, 750 us each, repeated 4 times.
Actual received and demodulated timings might be 2% shorter.


The data is grouped in 5 bytes / 10 nibbles

 1111 1100 | 0001 0110 | 0001 0000 | 0011 0111 | 0101 1001 0  65.1 F 55 %
 iiii iiii | bscc tttt | tttt tttt | hhhh hhhh | xxxx xxxx

- i: 8 bit random id (changes on power-loss)
- b: battery indicator (0=>OK, 1=>LOW)
- s: Test/Sync (0=>Normal, 1=>Test-Button pressed / Sync)
- c: Channel (MSB-first, valid channels are 1-3)
- t: Temperature (MSB-first, Big-endian)
     12 bit unsigned fahrenheit offset by 90 and scaled by 10
- h: Humidity (MSB-first) 8 bit relative humidity percentage
- x: checksum (byte1 + byte2 + byte3 + byte4) % 256
     Check with e.g. (byte1 + byte2 + byte3 + byte4 - byte5) % 256) = 0
