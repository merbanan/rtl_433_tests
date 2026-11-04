# Acurite 6045M (06045M) Lightning Detector

Lighting detector, with temperature and humidity sensor.

Notes from rct, Sept 2016.   Last Update: April 2018.

Protocol 39 (Shared with 5-n-1 and 592TXR Tower sensor)

Model Numbers: 06045M

Manufacturer's link:
- https://www.acurite.com/lightning-detector-with-temperature-and-humidity.html


## Data files

* acurite_6045_001.data - 75% humidity, 95 strikes, distance 10?, other bits t.b.d.
* acurite_6045_002.data - 75% humidity, 95 strikes, distance 10?, other bits t.b.d.


## General Notes

* Sends (according to Acurite docs):
  * Lightning strike count
  * Estimated Distance to storm front
  * Temperature
  * Humitidy
  * Status Infomration transmitted (based on display capabilities)
    * low battery, interference (RFI detected)

* Specs Per Acurte user manual 06045-instructions.pdf
  * Lighting detection range 1 to 25 miles, (1.6 to 40 KM)
    * "detects cloud-to-cloud, cloud-to-ground, and intra-cloud"
  * Temp. range   -40 to 158 F  / -40 to 70 C
  * Temperature accuracy (not specified in manual
    * From elsewhere: Temperature accuracy +/- 2 F
  * Humidity Range 1% to 99% relative
    * Accuracy?
  * Transmits every 24 seconds during "normal" mode.
    * This maps to standby/low power mode of the sensor
  * Transmits every 8 seconds during "active" mode.
    * There is a bit in the message to indicate active
    * could also be inferred by the frequency of transmissions.

* Acurite compatible displays.
  * 06047M display (part of 01021 / 06047 Rain Gauge Station with Lightning Detection)
    * Outside sensors are rain guage and lightning sensor.
    * lightning sensor provides the temperature and humidity.
    * Notes from manual:
      * Temperature is integer only, so max accuracy is 1 F or 1 C
      * Strike count shows in image as 186.  So possible 3 digits or '1' + 2 digits.
      * Distance shows 26 miles (but range is 25?)
      * Has interference indicator and low battery indicator.
      * Doesn't show any fractions for temperature, so max. resolution is +/- 1 F.
      * can display in either miles or km.
    * More notes from manual
      * Interference Indicator - flashes when interference is detected.
      * strike counter. most recent total (today, this week, this month)
      * Lightning Strike Indicator (big center icon) - strike occurred within 25 miles.
      * Lightning sensor low battery
      * Estimated distance to storm front - updates with latest lightning strike detected today.
  * 6058M HD Display - newer display that supports 5-n-1 and Lightning detector
    * From web page:
      * "Lightning strike counter displays running total of lightning strikes detected, plus weekly and monthly totals"
      * "Get alerted to lightning strikes with an audible alarm and on-screen alert"
      * "Provides an estimated distance to lightning-producing storm (miles or kilometers)"
    * Need to check manual for what lightning status bits might be decoded.


* Power:
  * uses 4 x AA batteries, but still 3Vdc, 2 pairs are parallel
    for higher current.
  * powers up at ~ 2.20-2.25 Vdc. (meter accuracy?)
    * small chirps/clicks if power/current too low.
  * Low Battery testing, more sensitive to low current than low voltage.

* Sensors/Chips/Teardown info
  * Based on Franklin AS3935 Lightning sensor IC. http://www.meteorange.fr/scripts/AS3935.pdf
    * See teardown thread in wxforum.net's Acurite forum.
  * Austria Micro is the name on the data sheet.
  * Temperature/Humidity sensor: T.B.D.
  * lightning sensor antenna is near holes next to red panel on the back of the PCB.
    * *Should orient the back towards direction storms come from for better sensitivity*
  * Notes from data sheet:
    * High noise condition (how the data sheet describes interference)
    * distance to head of storm 1 km to 40 km.
    * Chip modes:  power down, listening, and active  (8 second mode?)
    * power consumption varies from 60 - 350 uA listening vs. signal verification (active?)
    * Lightning Detection lookup table, 42 elements, alternating bits (gray code-ish?)
    * analog frent end (AFE) gain should be set for indoor or outdoor.
      Would guess that acurite has tuned for outdoor (?)
      
* Message format
  * Current understanding in rtl_433/src/devices/acurite.c
  * (Not replicating here since it will get out of date.)

* Observations
  * strike count can take one or more cycles after beep, before count increases.
    * This could be due to waiting to compute distance d?
    * There seems to be a status bit that might indicate validity of distance
  * Some beeps are for distance updates, no strike count.
  * No bit in message indicating when sensor is in flashing red state.

* Data field decoding as of April 2018.
  * *Strike Count* - rolling 7 bit counter of the number of "strike events" detected.
    * Non-volative (persists across power-ups)
    * Wraps at 127.  Does not reset, so consumer must decide what is a new storm
  * *Storm Distance* - See AS3935 datasheet, Estimate of distance to edge of storm
    * Units sent by Acurite / conversion formula to miles/kilometers TBD.
    * 5 bits available, 0-31.  0x1F == invalid.
  * *Active Mode* - Sensor is actively listening and transmitting every 8 seconds.
  * *RFI Detected* - Sent when sensor detects RFI (sensor uses RFI for detection)
    * This somehwat correlates to the Yellow Status LED on the device.
    * Short bursts of RFI detected are normal
    * Continuous periods of RFI on indicates interference that needs to be resolved in order for the sensor to work.
  * *USSB1* - (Unknown) Strike Status Bit 1
    * Toggles during strike events.
    * May indicate validity of distance measurement.
    * Resets to off when "beep" is first heard

