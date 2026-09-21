# Ecowitt WN34L Water Temperature Sensor

The WN34L is a water temperature sensor capable of measuring temperature from -40°C to +60°C.
There is a switch within the battery compartment to change the display between Fahrenheit and Celsius,
it likely does not change the temperature outputted over RF.

The ID of the sensor recorded is 3BCD, in case that helps with decoding.

| File prefix | Description                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------- |
| 00-powerup  | Signal sent on powerup, same between runs. Some sort of code used to register device with gateway? |
| 14.1C       | Reading of 14.1 degrees C, switch set to Celsius                                                   |
| 25.2C       | Reading of 25.2 degrees C, switch set to Celsius                                                   |
| 60.0C       | Reading of 60.0 degrees C, switch set to Celsius                                                   |
| 83.3F       | Reading of 83.3 degrees F, switch set to Fahrenheit                                                |

Manufacturer page: https://shop.ecowitt.com/en-ca/products/wn34l
