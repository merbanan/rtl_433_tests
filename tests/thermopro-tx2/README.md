# ThermoPro TX2 Remote Sensor

The ThermoPro TX2 Remote Sensor is sold with various ThermoPro thermometer/hygrometer devices (TP60S/TP62/TP63/TP63A/TP65A/TP67A) and also as a standalone accessory.

This folder contains the following samples:

- tx2_ch_1_433.92M_250k.cu8 : Channel=1; Temperature=26.6; Humidity=50%
- tx2_ch_2_433.92M_250k.cu8 : Channel=2; Temperature=26.2; Humidity=51%
- tx2_ch_3_433.92M_250k.cu8 : Channel=3; Temperature=26.3; Humidity=51%
- tx2_ch_1_battery_low_433.92M_250k.cu8 : Channel=1; Temperature=27.0; Humidity=51%; Battery=LOW
- tx2_ch_1_tx_button_433.92M_250k.cu8 : Channel=1; Temperature=26.3; Humidity=51%
- tx2_ch_1_reset_button_433.92M_250k.cu8 : Channel=1; Temperature=26.8; Humidity=53%

The corresponding temperature and humidity values were read from a Thermopro TP60S.

Note: Pressing the reset button on the TX2 causes it to generate a new id value which is included in the next transmission.
