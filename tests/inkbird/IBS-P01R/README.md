# Inkbird IBS-P01R
A 433MHz FSK wireless pool temperature sensor plus receiver station.

https://www.ink-bird.com/products-smart-sensor-ibsp01series.html

## Notes

Samples are decoded successfully using the fork from ehagan:

https://github.com/ehagan/rtl_433/tree/feat-inkbird_ith20r

Included JSON files are based on this fork.

The `temperature2` and `humidity` values are extraneous for this
device, they seem to be set to fixed values to be ignored. I'm not sure
if it's possible to differentiate between this and other Inkbird
devices, perhaps based on the unused sensor values?
