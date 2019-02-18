# bcf-0019x2

Chungear Industrial Co Ltd Fan/Light Remote Controller

https://fccid.io/KUJCE9001/User-Manual/User-Manual-171498.pdf

rtl_433 -f 305064400 -R 0 -X 'n=bcf-0019x2,m=OOK_PWM,s=252,l=484,r=8500,g=500,t=100,get=id:@9:{4},get=button:@1:{6}:[47:light_on-off 55:light_dimmer 62:fan_button_0 61:fan_button_1 59:fan_button_2 31:fan_button_3 63:no_button]' bcf-0019x2/*.cu8

repeats of 13 short (252 us) or long (484 us) pulses. Packet gap is 8188 us.

g004_305M_250k.cu8  dip switch 3
g005_305M_250k.cu8  dip switch 4
g006_305M_250k.cu8  dip switch 2
g007_305M_250k.cu8  dip switch 1

12345678 12345

11011111 10111  light on/off
11101111 10111  light dimmer
11111101 10111  fan button 0
11111011 10111  fan button 1
11110111 10111  fan button 2
10111111 10111  fan button 3

xxxxxxxx x0xxx  dip sw 1
xxxxxxxx xx0xx  dip sw 2
xxxxxxxx xxx0x  dip sw 3
xxxxxxxx xxxx0  dip sw 4
