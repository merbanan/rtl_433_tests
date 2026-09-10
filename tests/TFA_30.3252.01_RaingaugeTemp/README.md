# TFA 30.3252.01 rain gauge and temperature sensor
Sensor is sold together with a base unit as TFA 47.3006.01 V2.
# Sample data
Sample data was recorded using a Nooelec NESDR SMArt v5 without antenna with the sensor placed approximately 10 cm away.
Nightly rfl_433 was used (file date of zip 14.07.2026) with command: `rtl_433 -S unknown`

|filename|T on base|RR on base|comment|
|---|---|---|---|
|g021_433.92M_250k.cu8|23.0|0.9|last standard message before battery replacement|
|g022_433.92M_250k.cu8|22.9|0.9|first message after battery replacement|
|g023_433.92M_250k.cu8|22.9|0.9|second message after battery replacement (message is repeated 4 more times in 3s intervalls)|
|g027_433.92M_250k.cu8|22.9|0.9|Suspicious in analysis: repeat as the one above, but data of first of 6 rows slightly different|
|g035_433.92M_250k.cu8|23.0|12.8|Message after "bit-overflow" of rain value|
|g004_433.92M_250k.cu8|--.-|--.-|Suspicious in analysis: First message after battery replacement, some additional {0} rows decoded in-between rows (possibly sensor was not yet right to receiver)|
|g017_433.92M_250k.cu8|23.0|0.0|Suspicious in analysis: Additional {0} row decoded after first row|

Samples marked with _Suspicious in analysis:_ showed different behaviour then _usual_ messages when analysed with: 
`./rtl_433 -X 'n=test,m=OOK_PWM,s=244,l=480,y=720,r=720,invert'`.
