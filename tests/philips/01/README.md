# Philips outdoor temperature sensor

gfile001.data: Channel 3, Temperature 24.3 C, Battery OK
gfile002.data: Channel 1, Temperature 25.7 C, Battery OK
gfile003.data: Channel 2, Temperature 25.9 C, Battery OK
gfile004.data: Channel 3, Temperature -0.8 C, Battery LOW
gfile005.data: Channel 3, Temperature  6.3 C, Battery LOW

I've reverse-engineered the protocol and written up a parser; I'll be sending 
a pull request to merbanan/rtl_433 shortly.

