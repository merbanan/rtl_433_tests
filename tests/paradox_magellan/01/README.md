# Paradox Magellan samples

Signals generated from the Paradox Magellan protocol with made-up serials and transmitted by a
Flipper Zero as RAW files, recorded with an RTL-SDR at 433.92 MHz, 250 kHz, RSSI about -12 dB,
SNR about 21-22 dB. Three repeats per file.

OOK PWM, 1 = 200 us pulse + 400 us gap, 0 = 400 us pulse + 200 us gap. 800 us header pulse,
13 short pulses, 1200 us start pulse, 32 bits (16 bit serial, 8 bit event, CRC-8 poly 0x31),
fields sent LSB first.

| File | Serial (id) | Event | Meaning | On air |
|---|---|---|---|---|
| `door_sealed_433.92M_250k.cu8` | `1234` | `10` | door, sealed | `2C480805` |
| `door_alarm_tamper_433.92M_250k.cu8` | `1234` | `13` | door, alarm and tamper | `2C48C842` |
| `door_batt_low_433.92M_250k.cu8` | `fffe` | `19` | door, battery low | `7FFF989F` |
| `motion_sealed_433.92M_250k.cu8` | `a5c3` | `20` | motion, sealed | `C3A504A1` |
| `smoke_alarm_433.92M_250k.cu8` | `0001` | `31` | smoke, alarm | `80008CD2` |

Flex decoder (raw bits only, row after the sync pulse):

    -X 'n=Paradox-Magellan,m=OOK_PWM,s=200,l=400,y=1000,r=1000'

For `door_sealed` it gives `{13}fff8, {33}2c4808058` (preamble row, then data and the stop bit).
