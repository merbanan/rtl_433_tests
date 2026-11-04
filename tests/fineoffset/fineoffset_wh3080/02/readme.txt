Sample signals from a WH3080 868.3Mhz model. This needs another
conversion factor regarding the solar radiation value.

const float wm = (get_rawlight(br)*0.00079);

instead of 

const float wm = (get_rawlight(br)/6830);

It seems like this is not decoded properly by rtl_433 (as of 2020-12-08).

