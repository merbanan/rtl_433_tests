# Tests for Microchip HCS200 KeeLoq remotes decoder

Datasheet: DS40138C http://ww1.microchip.com/downloads/en/DeviceDoc/40138c.pdf

Flexible decoder example:

    rtl_433 -R 0 -X 'n=name,m=OOK_PWM,s=370,l=772,r=14000,g=4000,t=152,y=0,preamble={12}0xfff'

Samples:

- BTN1: Button 1 pressed
- BTN2: Button 2 pressed
- BTN3: Button 3 pressed
- BTN1-BOK: Button 1 pressed, battery OK
