Ambient Weather F007TH temperature/humidity sensor.

Sample output :

$ rtl_433 -r f007th.data
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: Generic RTL2832U OEM
Found Rafael Micro R820T tuner
Exact sample rate is: 250000.000414 Hz
Sample rate set to 250000.
Sample rate decimation set to 0. 250000->250000
Bit detection level set to 10000.
Tuner gain set to Auto.
Test mode active. Reading samples from file: f007th.data

Sensor Temperature Event:
protocol      = Ambient Weather
temp          = 67.8
humidity      = 35
channel       = 5
id            = 37

Sensor Temperature Event:
protocol      = Ambient Weather
temp          = 45.3
humidity      = 41
channel       = 4
id            = 180

Sensor Temperature Event:
protocol      = Ambient Weather
temp          = 53.4
humidity      = 44
channel       = 2
id            = 226

Sensor Temperature Event:
protocol      = Ambient Weather
temp          = 66.8
humidity      = 39
channel       = 1
id            = 254

Sensor Temperature Event:
protocol      = Ambient Weather
temp          = 54.0
humidity      = 59
channel       = 3
id            = 134
Test mode file issued 10 packets
Filter coeffs used:
a: 32768 31754
b: 506 506

