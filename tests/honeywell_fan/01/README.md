# Honeywell Fan Remote

The Honeywell Salermo fan (made by Intertek) transmits on  314.92 MHz.
This decoder used a remote with FCC id A25-TX0005R. These signals were captured 
on or around 314.92 MHz.

The remote has three buttons with 1, 2, and 3 dots on them, a 0/1 power button,
and a 'star' button. The 0/1 power button and the dotted buttons control the fan
(mostly) and the 'star' button controls the lights.

Momentarily pressing any button does what you expect - the 0/1 button turns the
fan off (never on), and the dotted buttons select low/med/hi fan speed. The 'star'
button turns the light on and off.

Pressing the 'star' button continuously dims or brightens the light. Pressing the
0/1 power button for 4 seconds (!) sets a 1 minute timer that turns the light off
when it expires.

Pressing 1+3 for 5 seconds sends a 'learn mode' command to the fan that associates
this remote with any fans that have power.

There's a small DIP switch in the battery compartment that controls whether or not
the dim/brighten function works - in the 'CFL' position dimmming is inhibited. In
the 'D' position dimming works.

The associated decoder is called honeywell_fan.conf.
