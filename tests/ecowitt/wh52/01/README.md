**Device:** Ecowitt WH52 (3-in-1 Soil Moisture, Temperature, and EC Sensor)
**Frequency:** 433.92 MHz
**Modulation:** FSK/OOK (Standard Ecowitt protocol, but payload structure is new for 2026)
**Product Page:** https://shop.ecowitt.com/products/wh52?variant=47292226797730

**Description:**
This is a new sensor released in early 2026. It adds Electrical Conductivity (EC) alongside the standard moisture and temperature readings found in older sensors like the WH51. Currently, `rtl_433` does not decode the new payload structure.

**Test File Notes:**
* **File:** `dry_test_1_433.92M_250k.cu8` & `dry_test_2_433.92M_250k.cu8`
    * **Moisture:** 0%
    * **Temperature:** ~80.0 F
    * **EC:** 0
    * **Condition:** Sensor was completely dry sitting on a desk.

* **File:** `wet_test_1_433.92M_250k.cu8` & `wet_test_2_433.92M_250k.cu8`
    * **Moisture:** 100%
    * **Temperature:** ~70.0 F
    * **EC:** Submerged in tap water
    * **Condition:** Sensor prongs were completely submerged in a glass of tap water.
