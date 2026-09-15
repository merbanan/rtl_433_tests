# Device Information: Renault Sandero Stepway Remote Keyless Entry (RKE)

## Description
* **Brand/Vehicle:** Renault Sandero Stepway
* **Device Type:** 2-Button Remote Key Fob (Lock / Unlock)
* **Operating Frequency:** 433.92 MHz
* **Modulation:** FSK (Frequency Shift Keying)
* **Pulse Style:** PWM (Pulse Width Modulation) with rolling code.

## Flex Decoder Parameters (from pulse analyzer)
    rtl_433 -f 433.92M -X 'n=Renault_RKE,m=FSK_PWM,s=52,l=100,r=680'

## Captured Sample Payloads

### 1. LOCK Button (Closed Lock Icon)
* **Press 1 (IQ File: renault_lock_01.cu8):** `{96}fffd55caf9ef7e79dfeaaef7`
* **Press 2 (IQ File: renault_lock_02.cu8):** `{93}fffd55caf9ef7e7aed6fc2f0`

### 2. UNLOCK Button (Open Lock Icon)
* **Press 1 (IQ File: renault_unlock_01.cu8):** `{92}fffd55caf9eefd72b5276eb`
* **Press 2 (IQ File: renault_unlock_02.cu8):** `{98}fffd55caf9eefe77bdfd7befc`

## Notes
The remote broadcasts multiple sequential frames per button press. Preamble remains steady, while trailing bits alter dynamically due to rolling code encryption. Nearby native Renault/Citroen TPMS decoders triggered concurrently during testing.
