This device is labelled MTRF-REM-15CLED
433.92MHz
rolleaseacmedia.com
FCC ID: VYY-DD5712

This controller operates mains powered roller blinds. I have two of these controllers and have supplied sample files for each.
I have another controller of identical appearance and FCC ID which uses a different (incompatible) protocol to operate battery powered roller blinds, which I will document as a separate project. 

Manual:
https://www.rolleaseacmeda.com/docs/default-source/us/automate-controllers/automate-paradigm-remote-controls/instr-mtrf-rem-v1-2-sept-2016-(003).pdf?sfvrsn=e823ee3c_8

FCC ID: https://fccid.io/VYY-DD5712

# Tests

I have tested commands for blind UP, blind STOP and blind DOWN. The controller appears to be capable of proportional level setting, but my blind motors do not appear to support this function, so I have been unable to test proportional level control.

The controller sends 2 by 40 bit messages for UP and DOWN commands and a single 40 bit message for the STOP command.
I don't know wheter both messages are required for the UP and DOWN commands, but speculate that the controller may be attempting to support two different models of roller blind motors.

Schema of signal is <7 hex byte controller address><1 hex byte compliment of channel number><2 hex byte command>
Up and down commands are sent as a pair of repeated commands.
Stop command is sent as a single repeated command.
The number of repeats received is quite variable, usually between 3 and 7.

40 bit message

    I - id, 28 bits
    N - Number of channel, 4 bit compliment
    C - Command, 8 bits

    IIIIIII N CC

Controllers tested are:
    My downstairs controller is address : 57c5ec9. Flex decoder match={7}0x57c55c9
    My upstairs controller is address   : bf17b48. Flex decoder match={7}0xbf17b48

Channel number is complement of the eigth hex byte. Thus    0xf = channel 0
                                                            0xe = channel 1
                                                                ...
                                                            0x0 = channel 15    

Up commands are:
    Burst of about 6 repeats of:                <7 byte controller address><1 byte channel><0xee>
    followed by a burst of about 6 repeats of:  <7 byte controller address><1 byte channel><0xe1>

Stop commands are:    
    Burst of about 6 repeats of:                <7 byte controler address><1 byte channel><0xaa>

Down commands are:
    Burst of about 6 repeats of:                <7 byte controler address><1 byte channel><0xcc>
    followed by a burst of about 6 repeats of:  <7 byte controler address><1 byte channel><0xc3>

For example, controller address 0x57c5ec9, channel 0
up  : {40}57c5ec9fee, {40}57c5ec9fee, {40}57c5ec9fee
    : {40}57c5ec9fee, {40}57c5ec9fee, {40}57c5ec9fee
    : {40}57c5ec9fe1
    : {40}57c5ec9fe1
    : {40}57c5ec9fe1, {40}57c5ec9fe1, {40}57c5ec9fe1, {40}57c5ec9fe1
stop: {40}57c5ec9faa, {40}57c5ec9faa, {40}57c5ec9faa
down: {40}57c5ec9fcc, {40}57c5ec9fcc, {40}57c5ec9fcc
    : {40}57c5ec9fcc, {40}57c5ec9fcc, {40}57c5ec9fcc
    : {40}57c5ec9fc3
    : {40}57c5ec9fc3
    : {40}57c5ec9fc3, {40}57c5ec9fc3, {40}57c5ec9fc3, {40}57c5ec9fc3

To prepare the first set of test files, I have used this command:
>rtl_433-rtlsdr -X n=DD5712,m=OOK_PWM,s=352,l=725,r=8734,g=0,t=0,y=4249,match={7}0x57c55c9 -s 1024k -S known

The first set of files (in folder 01) are for controller 0x57c55c9:
g081_433.92M_1024k.cu8 Channel 0 up command - first burst.
g082_433.92M_1024k.cu8 Channel 0 up command - second burst.
g083_433.92M_1024k.cu8 Channel 0 stop command.
g084_433.92M_1024k.cu8 Channel 0 down command - first burst.
g085_433.92M_1024k.cu8 Channel 0 down command - second burst.
g075_433.92M_1024k.cu8 Channel 4 up command - first burst.
g076_433.92M_1024k.cu8 Channel 4 up command - second burst.
g077_433.92M_1024k.cu8 Channel 4 stop command.
g078_433.92M_1024k.cu8 Channel 4 down command - first burst.
g079_433.92M_1024k.cu8 Channel 4 down command - second burst.

To prepare the second set of test files, I have used this command:
>rtl_433-rtlsdr -X n=DD5712,m=OOK_PWM,s=352,l=725,r=8734,g=0,t=0,y=4249,match={7}0xbf17b48 -s 1024k -S known

The second set of files (in folder 02) are for controller 0xbf17b48:
g087_433.92M_1024k.cu8 Channel 2 up command - first burst.
g088_433.92M_1024k.cu8 Channel 2 up command - second burst.
g089_433.92M_1024k.cu8 Channel 2 stop command.
g090_433.92M_1024k.cu8 Channel 2 down command - first burst.
g091_433.92M_1024k.cu8 Channel 2 down command - second burst.
g092_433.92M_1024k.cu8 Channel 3 up command - first burst.
g093_433.92M_1024k.cu8 Channel 3 up command - second burst.
g094_433.92M_1024k.cu8 Channel 3 stop command.
g112_433.92M_1024k.cu8 Channel 3 down command - first burst. Note: It took several retries to get signals that looked intact. Still, some repeats are corrupted.
g113_433.92M_1024k.cu8 Channel 3 down command - second burst.
