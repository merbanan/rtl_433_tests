Tests for Microchip HCS200 KeeLoq remotes decoder

Datasheet: DS40138C http://ww1.microchip.com/downloads/en/DeviceDoc/40138c.pdf

Flexible decoder example:

rtl_433 -R 0 -X 'n=name,m=OOK_PWM,s=370,l=772,r=14000,g=4000,t=152,y=0,preamble={12}0xfff'

Samples:

01 - Button 1 pressed
02 - Button 2 pressed
03 - Button 3 pressed
04 - Button 1 pressed, battery OK
