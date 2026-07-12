# Ecowitt WN38 Black Globe Thermometer

Black globe thermometer, the WBGT (wet bulb globe temperature) component of
Ecowitt's weather station ecosystem. Measures -40 to 125 °C at 0.1 °C
resolution, powered by a single AA battery, transmits roughly once per
minute. This is the 868.3 MHz (EU) version, FSK PCM with 58 µs bit width.

Product page: https://shop.ecowitt.com/products/wn38
Manual: https://oss.ecowitt.net/uploads/20251128/WN38AN-UserManual.pdf

Captured with `rtl_433 -f 868.3M -S unknown` at 1000k sample rate. All five
captures are from the same device (id 0x002885) at different globe
temperatures; every decoded temperature was confirmed to match the sensor's
own LCD display exactly.

## Frame layout

Byte-identical to the Fine Offset WN34 layout (`src/devices/fineoffset_wn34.c`
in rtl_433) but with family code 0x38: preamble `aa..aa`, sync word `2dd4`,
then a 9-byte payload:

    YY II II II ST TT BB XX AA

- `YY`{8}: family code, 0x38
- `II`{24}: device id (0x002885 for this unit)
- `S`{4}: subtype, 4 = temperature at scale 10 with no -40 offset (as WN34D)
- `T`{12}: temperature, scale 10
- `B`{7}: battery voltage in 20 mV units
- `XX`{8}: CRC-8, poly 0x31, init 0, over bytes 0..6
- `AA`{8}: sum of bytes 0..7

Example bitbuffer code (g001):

    {137}aaaaaaaaaaa2dd43800288540f5414ca780

## Samples

| file                  | payload (after sync) | temperature | battery |
|-----------------------|----------------------|-------------|---------|
| g001_868.3M_1000k.cu8 | 3800288540f5414ca7   | 24.5 °C     | 1300 mV |
| g002_868.3M_1000k.cu8 | 38002885410741cb39   | 26.3 °C     | 1300 mV |
| g003_868.3M_1000k.cu8 | 38002885411d414bcf   | 28.5 °C     | 1300 mV |
| g005_868.3M_1000k.cu8 | 38002885412a4157e8   | 29.8 °C     | 1300 mV |
| g006_868.3M_1000k.cu8 | 380028854136418d2a   | 31.0 °C     | 1300 mV |

Battery byte is 0x41 = 65 in all five samples, 65 x 20 mV = 1300 mV
(fresh AA cell).

## Photos

- `front.jpg`: sensor with LCD display
- `back.jpg`: label side ("Model No.: WN38, Frequency: 868MHz, Power: 1 AA
  battery, Designed by Fine Offset")
- `id.jpg`: ID sticker reading "ID : 2885", matching the transmitted device
  id 0x002885
