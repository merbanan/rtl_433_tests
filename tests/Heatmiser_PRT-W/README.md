#Heatmiser PRT-W thermostat
These are thermostats principally designed to control underfloor heating systems although they also can be used to control radiators.

The thermostat transmits to a receiver which controls physical valves to provide heat to the zone where the thermostat is. I think the receiver also has a hard wire link to the boiler to tell it to wake up and get heating when this happens, as I've detected no signal to suggest it's wireless.

The thermostats all transmit on or around 869.01Mhz

##Modes
Normal
Temperature Set
Temperature Hold
Frost Protect
Holiday

##Optional Settings
01 - Temperature format: C/F
02 - Switching differential
03 - Frost protection
04 - Frost protect temperature
05 - Output delay
06 - UH1-W or RC1-W receiver
07 - Receiver Address
08 - Zone number
09 - UFW or Radiators
10 - Fail safe
11 - Up/Down Temperature limit
12 - Air sensor selection (remote sensor)
13 - not used
14 - Optimum start
15 - Rate of change (info only)
16 - Programming mode - weekday/weekend vs 7 day.

##Decode
`rtl_433 -Y classic -R 0 -X "name=Heatmiser_PRT-W, modulation=FSK_PCM, s=416, l=416, r=20000, bits>=120, preamble=aaaa2dd4, get=@8:{8}:Thermostat ID:[136:L02-Living-Room 137:L00-Dining-Room],get=@16:{8}:heat:[49:ON 33:OFF]" -f 869.01Mhz -F "mqtt://192.168.1.150,retain=1,devices=sensors/rtl_433/P[protocol]/C[channel]"`

`rtl_433 -Y classic -R 0 -X "name=Heatmiser_PRT-W, modulation=FSK_PCM, s=416, l=416, r=20000, bits>=120, preamble=aaaa2dd4" -f 869.01Mhz -F csv:HeatmiserOvernight.csv `

###Live with conf file
`rtl_433 -Y classic -R 0 -c /home/russ/.config/rtl_433/HeatmiserPRT-W.conf -f 869.01Mhz `


##L02 Stat
###Option settings
01 = 00 - Temperature format: 	C
02 = 01 - Switching differential: 	1C
03 = 01 - Frost protection:		Enabled
04 = 11 - Frost protect temperature:	11C
05 = 00 - Output delay:		0 minutes
06 = 00 - Receiver:			UH1-W
07 = 08 - Receiver address:		08
08 = 01 - Zone number:			01
09 = 00 - UFW or Rads			UFW
10 = 01 - Fail safe			Enabled 
11 = 00 - Up/Down limit:		00C Default
12 = 00 - Sensor selection:		Built in
13 = 28 - not used
14 = 00 - Preheat setting		00 hours
15 = 20 - rate of change		20
16 = 00 - Programming mode		5/2 day

##Bitstream analysis
Bits  Notes
0-7   Constant
8-15  Receiver address - 88=L02, 89=L00
16-19 Heat Call: 3=On, 1=Off
20-23 Thermostat ID
24-31 Constant
32-39 Constant
40+   Not sure yet......

The heatmiser's bit stream at bit no. 8 gives the receiver address for 8 bits, the next 4 bits is the on/off command and the next 4 is the thermostat ID number. The consequence of all this is that to get a meaningful unique ID we need both the receiver and the stat ID. I don't know how to concatenate the first 8bits, skip 4 and then add a further 4. To keep things simple, I just took the entire 16 bits, but this means we end up with two values for each thermostat - one for the on state and one for the off state. Thus on my system both 0x8821 and 0x8831 relate to the Living room thermostat. I then just aliased both bitwise outputs to the same text string: Living_Room. This seems to work ok, but feels like a bit of hack.

## L02 Living Room
### Heat OFF
`c9 88 21 02 64 83 31 38 00 00`
### Heat ON
`c9 88 31 02 64 82 f4 38 00 00`

## L00 Dining Stat
### Heat OFF
`c9 89 21 02 64 82 cd 38 00 00`
### Heat ON
`c9 89 31 02 64 83 08 38 00 00`

## L00 Kitchen
### Heat OFF
`c9 89 22 02 64 72 cd 38 00 00`
### Heat On
`c9 89 32 02 64 73 08 38 00 00`

## L00 Hallway
### Heat OFF
`c9 89 23 02 64 23 0d 38 00 00'
### Heat ON
`c9 89 33 02 64 22 c8 38 00 00`

