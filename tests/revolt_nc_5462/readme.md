# Revolt NC-5462 Energy Meter



### Sample measurements with no power consumer attached.
no_consumer_433.92M_250k.cu8
```json
{"time" : "@0.828520s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 232, "current_A" : 0.000, "frequency_Hz" : 50, "power_W" : 0.000, "power_factor_VA" : 0.000, "energy_kWh" : 307.120, "button" : 0, "mic" : "CHECKSUM"}
```

### Sample measurements with power consumer with low consumption.
low_power_consumer_433.92M_250k.cu8
```json
{"time" : "@1.413972s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.000, "frequency_Hz" : 50, "power_W" : 0.400, "power_factor_VA" : 1.000, "energy_kWh" : 307.120, "button" : 0, "mic" : "CHECKSUM"}
```

### Sample measurements with power consumer with higher consumption.
with_power_consumer_433.92M_250k.cu8
```json
{"time" : "@0.761732s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.260, "frequency_Hz" : 50, "power_W" : 53.300, "power_factor_VA" : 0.880, "energy_kWh" : 307.120, "button" : 0, "mic" : "CHECKSUM"}
```

### Sample measurements with button pressed. Device sends repeated signals.
button_pressed_433.92M_250k.cu8
```json
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@0.968304s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
{"time" : "@2.034944s", "model" : "Revolt-NC5462", "id" : 545, "voltage_V" : 233, "current_A" : 0.310, "frequency_Hz" : 50, "power_W" : 65.400, "power_factor_VA" : 0.900, "energy_kWh" : 307.130, "button" : 1, "mic" : "CHECKSUM"}
```

