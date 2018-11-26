Two TPMS measured with "professional" tool. This tool always report Batt: ok and G: ok but status in rtl_433 is changing.

Status wake appear when the tool send wake up signal probably on 115kHz.

Inside my PMV-C210 is Infineon SP37 450kPa - SP37DL.

On the 20AEF4A can be compared status normal and wake.

On b9f6d5 could we try to read air loss and battery?

Status 128 is normal/idle pressure report after move/accelerate.
Status 132 appear after fast air loss i did not catch that signal.
Status 176 is probably low battery or some kind of that. It appears few times when you cut off battery and then put in back and when voltage is below 1.9V (probably sensor reset). Reads with status 176 was forced by wake singal.
Status 160 is Wake. Status after send Wake up signal.

0b9f6d5-low-battery.cu8
Press: 0.0Bar Temp: 17C ID: 0b9f6d5 Status: Wake Bat: ok G: ok
Voltage< 1.9V Status in rtl_433: 176 
{"time" : "@0.000000s", "model" : "Toyota", "type" : "TPMS", "id" : "f0b9f6d5", "status" : 176, "pressure_kPa" : 1.724, "temperature_C" : 17.000, "mic" : "CRC"}

0b9f6d5-wake.cu8
Press 0.0Bar Temp: 17C ID: 0b9f6d5 Status: Wake Bat: ok G: ok
Voltage 3.08V Status in rtl_433: 160
{"time" : "@0.000000s", "model" : "Toyota", "type" : "TPMS", "id" : "f0b9f6d5", "status" : 160, "pressure_kPa" : 1.724, "temperature_C" : 17.000, "mic" : "CRC"}

0b9f6d5-idle.cu8
Press: 0.0Bar Temp: 16C ID: 0b9f6d5 Bat: ok G: ok
Voltage: 3.08V Status: 128
{"time" : "@0.000000s", "model" : "Toyota", "type" : "TPMS", "id" : "f0b9f6d5", "status" : 128, "pressure_kPa" : 1.724, "temperature_C" : 16.000, "mic" : "CRC"}

20AEF4A-wake.cu8
Press: 0.0Bar Temp: 18C ID: 20AEF4A Status: Wake Bat: ok G: ok Status: 160
{"time" : "@0.000000s", "model" : "Toyota", "type" : "TPMS", "id" : "f20aef4a", "status" : 160, "pressure_kPa" : 1.724, "temperature_C" : 18.000, "mic" : "CRC"}

20AEF4A-idle.cu8
Press 0.0Bar Temp: 18C ID: 20AEF4A StATUS: normal  Bat: ok G: ok Status: 128
{"time" : "@0.000000s", "model" : "Toyota", "type" : "TPMS", "id" : "f20aef4a", "status" : 128, "pressure_kPa" : 1.724, "temperature_C" : 18.000, "mic" : "CRC"}



