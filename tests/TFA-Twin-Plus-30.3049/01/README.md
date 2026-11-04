# TFA Twin Plus 30.3049 thermo/hygrometer

Hi!
I've created little bash script to support TFA Twin Plus 30.3049 thermo/hygrometer protocol:

rtl_433 -f 433920000 -l 500 -a -g 18 2>&1 |mawk -W interactive -F ":" '/[01] {36}/{print $2}' | sed -u 's/ //g'| stdbuf -oL rev | mawk -W interactive '{ printf"ibase=2; %s\n",substr($0,6,7) ; printf"ibase=2; %s\n", substr($0,16,9) }' | bc | mawk -W interactive 'NR==1{ print"----------------------------\n" ; system("date") ; printf"Humidity\t: %s\n",$1-28 } NR==2{ printf"Temperature\t: %s\n",$1/10 ; NR=0 }'

Here is some sample data:
[04] {36} e4 4b 70 73 00 : 111001000100 101101110 000 0111001 10000 ---> temp/hum:23.7/50
temp num-->13-21bit(9bits) in reverse order in this case "011101101"=237
positive temps ( with 000 in bits 22-24) : temp=num/10 (in this case 23.7 C)
negative temps (with 111 in bits 22-24) : temp=(512-num)/10
negative temps example:
[03] {36} e4 4c 1f 73 f0 : 111001000100 110000011 111 0111001 11111 temp: -12.4

Humidity:
hum num-->25-32bit(7bits) in reverse order : in this case "1001110"=78
humidity=num-28 --> 78-28=50


*** signal_start = 7663357, signal_end = 7818281
signal_len = 154924,  pulses = 149
Iteration 1. t: 170    min: 169 (69)    max: 172 (80)    delta 1
Iteration 2. t: 170    min: 169 (10)    max: 171 (139)    delta 1
Iteration 3. t: 170    min: 169 (10)    max: 171 (139)    delta 0
Distance coding: Pulse length 170

Short distance: 440, long distance: 957, packet distance: 2178

p_limit: 170
bitbuffer:: Number of rows: 5
[00] {0} :
[01] {36} e4 0f 70 2b e0 : 11100100 00001111 01110000 00101011 1110
[02] {36} e4 0f 70 2b e0 : 11100100 00001111 01110000 00101011 1110
[03] {36} e4 0f 70 2b e0 : 11100100 00001111 01110000 00101011 1110
[04] {36} e4 0f 70 2b e0 : 11100100 00001111 01110000 00101011 1110
signal_bszie = 393216  -      sg_index = 0
start_pos    = 2660432  -   buffer_size = 3145728
*** Saving signal to file gfile001.data
*** Writing data from 2660432, len 393216
