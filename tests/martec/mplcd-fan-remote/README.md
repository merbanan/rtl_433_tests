Martec MPLCD fan remote

This model holds the state in the remote and sends a complete new state setting to the fan for each button press.
e.g. the remote knows (assumes) that the light is on and fan is off. If the fan speed button is pressed once to set the fan to 'high', the remote sends the command for light:on and fan:high.
If the remote's assumption about the fan state is incorrect, such as when the wall switch has been cycled, the remote will just 
send its assumed state to the fan and it is up to the user to press buttons to get the fan back into the state they desire.
This mostly shows up when entering a room and turning on the wall switch which turns on the light. The user then presses the remote fan speed switch to also turn on the fan and the light unexpectedly turns off because the remote had an assumed state of light: off.

Timings
short_width:  292
long_width:   648
reset_limit: 9732
sync_width:     0

Flex decoder
-X 'n=name,m=OOK_PWM,s=292,l=648,r=9732,g=792,t=142,y=0'

Data layout:

    22 bits
    PPPP IIII DDDDDDD SS U CCCC

- P: 4 bit fixed preamble 0x8
- I: 4 bit channel ID - reflected and inverted
- D: 7 bit dimmer - 0 is off, 1-41 is on with 1 being full brightness
- S: 2 bit speed - 0: off, 1: high, 2: medium, 3: low
- U: 1 bit unknown
- C: 4 bit simple checksum

Format string:

    xxxx ID:4h LIGHT:7h FAN:2h x CRC:4b

Checksum is simple sum over 4 nibbles starting from bit 2

Commands are repeated four times

A short press on the dimmer button toggles the light on or off. A long press on the dimmer button progressively dims or brightens the light. For each brightness dot on the remote's LCD the remote sends a sequence of 6 dim or brighten increments.

Samples
g002_433.92M_250k.cu8 - channel:8, light:off,  fan:medium
g005_433.92M_250k.cu8 - channel:2, light:off,  fan:off
g008_433.92M_250k.cu8 - channel:1, light:2->3, fan:off
