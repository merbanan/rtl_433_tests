# Watchman Sonic Advanced/Plus

This is sold standalone and as part of the Watchman SENSiT kit.

https://www.kingspan.com/gb/en/products/tank-monitoring/remote-tank-monitoring/watchman-sensit-smart-wifi-tank-level-monitoring-kit/

The WiFi component is an ESP32-based USB dongle which receive transmissions from the tank sensor and uploads it to Kingston's cloud. The mobile app allows you to view the level in the tank. However, the level in the app only updates *once per day*. This is a bit unambitious.

The tank sensor itself transmits every 30 mins. The transmission includes the serial number of the sensor, the depth in cm and the temperature in degrees Celsius, though I haven't yet been able to decode that correctly.

- **g039_433.92M_250k.cu8**  
  Serial: 05261860  
  Temp:	6  
  Depth: 95  
- **g120_433.92M_250k.cu8**  
  Serial: 05261860  
  Temp: 5  
  Depth: 96  
- **g470_433.92M_250k.cu8**  
  Serial: 05261860  
  Temp: 6.5  
  Depth: 95  