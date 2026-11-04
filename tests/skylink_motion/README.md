# Skylink-HA-434TL motion sensor

This device is an inexpensive indoor/outdoor motion sensor.  Details of the actual device are available heartbeats

https://www.amazon.ca/Skylink-HA-434TL-Household-Protection-Accessory/dp/B003CWGDTK/ref=sr_1_1?s=hi&ie=UTF8&qid=1538094741&sr=1-1&keywords=Skylink+HA-434TL+Wireless+Long+Range+Household+Alert+%26+Alarm+Home+Garage+Driveway+Business+Office+Security+Protection+Indoor+Outdoor+Infrared+Motion+Detector+Sensor+Accessory

The device sends motion events when detected, and does not support an all clear message.  When testing, battery level monitoring did not seem to be supported, but it did send a heartbeat roughly every 2 hours.  So when implementing a client, have a 2 hour watchdog for the heartbeat message, and if you don't receive it, say battery low or not responding.

JSON Message received

{"time" : "2018-09-27 19:28:26", "model" : "Skylink motion sensor", "motion" : "true", "id" : "1e3e8", "raw" : "be3e8"}

The raw field is the raw data received from the sensor.
