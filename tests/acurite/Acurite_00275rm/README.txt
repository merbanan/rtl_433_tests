This is test data, screenshots and code for the Acurite sensors 00275rm and 00276rm, with
and without their associated optional probes.


DIRS AND FILES

#  Output from 'rtl_433 -a -t' for various configurations
data/
    # 00275rm (External Sensor)
    ext.data                  - just the sensor, no probe
    ext-lowbattery.data       - just the sensor, with low battery
    ext-soilprobe.data        - sensor with soil probe
    ext-spotprobe.data        - sensor with spot probe
    # 00276rm (Internal Sensor)
    int.data                  - just the sensor, no probe
    int-lowbattery.data       - just the sensor, with low battery
    int-waterprobe-dry.data   - sensor with water probe, no water detected
    int-waterprobe-wet.data   - sensor with water probe, water detected


#  Json output from submitted code , one for each data file above.
#  It records temperature, humidity, etc for each data file.
./json:
    ext.data.json
    ext-lowbattery.data.json
    ext-soilprobe.data.json
    ext-spotprobe.data.json
    int.data.json
    int-lowbattery.data.json
    int-waterprobe-dry.data.json
    int-waterprobe-wet.data.json

.:

#  Screenshots from Acurite web site, including photos.
./screenshots
    external.png
    internal.png
    soil_probe.png
    spot_probe.png
    water_probe.png
