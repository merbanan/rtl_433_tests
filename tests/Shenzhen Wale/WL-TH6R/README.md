# Shenzhen Wale WL-TH6R

FCC ID: [2A2X7-WL-TH6R](https://fcc.report/FCC-ID/2A2X7-WL-TH6R)

Typically bundled with Wi-Fi base stations powered by [Tuya](https://www.tuya.com/) like the WL-TH16-R.

AliExpress seller [SMATRUL](https://smatruldoorbell.aliexpress.com/store/1101261049) uses these related product IDs:
- WSD023-WIF-433-W12 for a WL-TH16-R style [base station](https://www.aliexpress.us/item/3256808493034721.html).
- WSD024-W-433 for the sensors (bundled with the base station)

AliExpress seller [ONENUO](https://www.aliexpress.com/store/1103831232) also sells similar and identical looking sensors. For example, this appears to be [the
same base station](https://www.aliexpress.us/item/3256810348959477.html), but with slightly different sensors.
These sensors are also bundled with [this product](https://www.aliexpress.us/item/3256810400966935.html).

According to user [avg-I on GitHub](https://github.com/avg-I), this decoder works with those sensors as well.
He discovered this [manual for the WL-TH6R](https://manuals.plus/m/851951e2e953a4eeb0524095efa5695751c6d04759095ea022b4db18bb58d9f4).

Shenzhen Wale may be the OEM for these other brands.

The sensors operate on 433.92 MHz and the base station acts as a hub connected to the internet via Wi-Fi.
Pairing sensors to the base station requires an internet connection and use of the [SmartLife mobile app](https://smartapp.tuya.com/smartlife), but the sensors operate the same whether they have been paired or not.

The sensors are powered by two AAA batteries.
A red LED on the front lights up during transmissions.
Underneath the cover on the back there is a pairing button, causing the sensor to send 13 transmissions about 400 ms apart.
A pairing bit is set for these transmissions.

In normal operation these sensors take a measurement every 10s, but only transmit an update when there has been a sufficient change in the measurements.
According to an image in the product description this should happen when the temperature changed by 0.2°C or when the humidity changed by 2%, but observation suggests the actual required minimum changes are 0.3°C and 3% instead.
The sensors also appear to be transmitting after 5m 10s when there has not been a sufficient change in the measurements.
The Tuya cloud API ignores readings below -20°C or above 60°C, but the base station will still try to display them.

The battery level is reported in 1% increments, but measurements of the battery level seem much less frequent.
Re-inserting the batteries also doesn't necessarily produce the same reading each time and sometimes differs a lot from previous readings.
The sensor reports a battery percentage of 100% for 3.0V and 0% for 2.3V.
Voltages above 3.0V will be reported as > 100%, with the base station even accepting readings of 255% (8-bit limit), though the Tuya cloud API and mobile app will report at most 100%.
The mobile app will show a notification when the reported battery level drops below 20%.

## Test Files

The provided recordings are artificially created using a [D-LIFE 433.92 MHz transmitter module](https://www.amazon.com/dp/B0BZRRBBNK) and recorded with rtl_433.
Note that the original transmitter shows less overshoot than these recordings.

The table below documents the data in the .cu8 files, the Reported column reflects what the decoder will actually reveal.
Ignored are rows with fewer than 72 or more than 73 bits, rows that occur only once, rows with an incorrect checksum or implausible temperature or humidity values.
If more than one sensor contributes such data the sensor whose (valid) row appears first will get reported.

| Test | Files                                                                  | Sensor ID | Pairing | Cycle | Temperature | Humidity | Battery | Reported |
| ---- | ---------------------------------------------------------------------- | --------- | ------- | ----- | ----------- | -------- | ------- | -------- |
|    1 | [CU8](01/test_1_433.92M_250k.cu8), [JSON](01/test_1_433.92M_250k.json) | AB3456    | No      |     0 |      12.3°C |      45% |     67% |      Yes |
|    2 | [CU8](01/test_2_433.92M_250k.cu8), [JSON](01/test_2_433.92M_250k.json) | AB3456    | Yes     |    43 |     -12.3°C |      12% |    245% |      Yes |
|    3 | [CU8](01/test_3_433.92M_250k.cu8), [JSON](01/test_3_433.92M_250k.json) | F9E8D7    | No      |   100 |       0.0°C |      99% |    100% |      Yes |
|    4 | [CU8](01/test_4_433.92M_250k.cu8), [JSON](01/test_4_433.92M_250k.json) | F9E8D7    | No      |    17 |      33.0°C |      50% |    100% |      Yes |
|    5 | [CU8](01/test_5_433.92M_250k.cu8), [JSON](01/test_5_433.92M_250k.json) | D83976    | No      |    62 |      26.5°C |      20% |     19% |       No |
|      |                                                                        | 907722    | No      |     1 |      -8.4°C |      75% |     80% |      Yes |
|      |                                                                        | FA0605    | No      |    33 |       5.1°C |      89% |    109% |       No |
|      |                                                                        | 361B68    | No      |    19 |      13.9°C |      34% |    101% |       No |
|      |                                                                        | AC8174    | No      |    50 |      34.1°C |      97% |     22% |       No |


__Test 1 & Test 2:__
Basic tests with positive and negative temperatures, pairing mode on and off.

__Test 3:__
The second and fifth row (excluding the preamble) have a flipped bit such that the MIC value is invalid, resulting in a count of 3.
In addition, this test checks handling of a situation that can arise when first powering the sensor on.
The memory used to store the counter doesn't seem to get properly initialized, possibly resulting in the counter exceeding 64 when the batteries are sufficiently charged.
The counter value of 100 in the data should get reported as 64 so that any downstream logic can rely on the counter never exceeding that value.

__Test 4:__
This test validates that the decoder can handle a potential extra bit per row.
The sensor adds an extra pulse after the preamble and each of the five instances of the payload, but it is slightly shorter than the pulse used for 0s and should normally get ignored by rtl_433.
In this test, the extra pulse in the first row (excluding the preamble) has the same length as 0s, which should lead to an extra bit in this row.
There is only one other row with 72 bits.
The decoder should recognize the rows with 73 and 72 bits as having the same data and fullfilling the requirement of having to occur more than once.

In addition, the sensor has a battery level of 19%, and should get an extra battery_ok: 0 output.

__Test 5:__
This test contains valid data from five different sensors at the same time.
Some of the payloads appear intact twice instead of once, and random fragments of the data are also interspersed, testing that the decoder can ignore those incomplete rows.
Only one sensor should have its data reported due to being the first one with a row that occurs more than once.

## Photos

![](image_1_sensor.jpg)
![](image_2_sensor.jpg)
![](image_3_sensor_box.jpg)
![](image_4_station_box.jpg)
