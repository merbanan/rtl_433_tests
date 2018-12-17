# Digitech XC0346

These samples are all from a single Digitech XC0346, which is a rebadged Fine Offset WH1050 using 433.92MHz.

https://www.jaycar.com.au/wireless-weather-station-with-rain-gauge-and-forecasting/p/XC0346

All .json output files produced by: `rtl_433 -G -r $a -F json` with patch for Digitech XC0346 applied (see https://github.com/merbanan/rtl_433/pull/922).

Difference between this model and the WH1050 (as supported in rtl_433) seems to be the Digitech sends a 7 bit preamble instead of 8 bits (maybe one bit of preamble is consumed by the radio module as it wakes up?)

Weather station unit transmits every ~48 seconds. Alternates between sending one packet and two packets each time (the two packets are identical)

* g001..g003 were taken with transmitter unit approx 3 metres from RTL-SDR.

* g001..g904 and g960..g964 are two consecutive sessions taken with transmitter approx 25 metres from RTL-SDR, behind two buildings.

A homemade 433MHz half wave dipole antenna was used for these captures.
