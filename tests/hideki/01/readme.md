# HIDEKI TS04 Temperature and Humidity sensor

Cheap sensor providing both temperature and humidity, with a small LCD, and 5 channels.

Sensor sold under different brant:

* "Bresser" with ref: "Art. No. 70-09993" http://www.amazon.fr/Bresser-7009993-Thermo-5-Kanal-Station/dp/B0076JGK7U
* "TFA Dostmann"
* ???

Some reverse engineering had been done here:

* http://www.mikrocontroller.net/topic/211884 (in german)
* https://bitbucket.org/fuzzillogic/433mhzforarduino/src/0847a6d8a9173abd5abf9cf571a1539f56588c0e/RemoteSensor/SensorReceiver.cpp?at=default&fileviewer=file-view-default


About the protocol:

* use [differential manchester encoding](https://en.wikipedia.org/wiki/Differential_Manchester_encoding) or `pulse_demod_clock_bits` in rtl_433
* one parity bit after each byte
