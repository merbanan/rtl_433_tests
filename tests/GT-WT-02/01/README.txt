SENSOR: GT-WT-02 (ALDI, Globaltronics..)
outputfile
*** signal_start = 113970967, signal_end = 114212857
signal_len = 241890, pulses = 240
Iteration 1. t: 135 min: 129 (239) max: 141 (1) delta 9
Iteration 2. t: 135 min: 129 (239) max: 141 (1) delta 0
Distance coding: Pulse length 135
Short distance: 519, long distance: 1028, packet distance: 2257
p_limit: 135
[00] {0} 00 : 00000000 
[01] {37} 34 00 ed 47 60 : 00110100 00000000 11101101 01000111 01100000 
[02] {1} 00 : 00000000 
[03] {37} 34 00 ed 47 60 : 00110100 00000000 11101101 01000111 01100000 
[04] {1} 00 : 00000000 
[05] {37} 34 00 ed 47 60 : 00110100 00000000 11101101 01000111 01100000 
[06] {1} 00 : 00000000 
[07] {37} 34 00 ed 47 60 : 00110100 00000000 11101101 01000111 01100000 
[08] {1} 00 : 00000000 
[09] {37} 34 00 ed 47 60 : 00110100 00000000 11101101 01000111 01100000 
[10] {1} 00 : 00000000 
[11] {37} 34 00 ed 47 60 : 00110100 00000000 11101101 01000111 01100000 
[12] {0} 00 : 00000000

/* 2 examp les
/* [01] {37} 34 00 ed 47 60 : 00110100 00000000 11101101 01000111 01100000
/* code, BatOK,not-man-send, Channel1, +23,7°C, 35%
/*
/* [01] {37} 34 8f 87 15 90 : 00110100 10001111 10000111 00010101 10010000
/* code, BatOK,not-man-send, Channel1,-12,1°C, 10%

/* SENSOR: GT-WT-02 (ALDI Globaltronics..)
/* TYP AAAAAAAABCDDEFFFFFFFFFFFFGGGGGGGxxxxx
/* BIT 0000000001111111111222222222233333333
/* BIT 1234567890123456789012345678901234567
/* 
/* TYPDescriptian
/* A = Rolling Device Code, Change after battarie
/* B = Batt 0=OK 1=LOW
/* C = Manual Send Button Pressed 0=not pressed 1=pressed
/* D = Channel 00=CH1, 01=CH2, 11=CH3
/* E = Temp 0=positiv 1=negativ
/* F = PositivTemp = 12 Bit bin2dez Temp, 
/* F = negativ Temp = 4095+1- F (12Bit bin2dez) , Factor Divid F / 10 (1Dezimal)
/* G = Humidity = 7Bit bin2dez 00-99, Display LL=10%, Display HH=110% (Range 20-90%)
/* x = checksum
       bin2dez(Bit1;Bit2;Bit3;Bit4)+ #rolling code
       bin2dez(Bit5;Bit6;Bit7;Bit8)+ #rolling code
       bin2dez(Bit9;Bit10;Bit11;Bit12)+ #send, bat , ch
       bin2dez(Bit13;Bit14;Bit15;Bit16)+ #temp1
       bin2dez(Bit17;Bit18;Bit19;Bit20)+ #temp2
       bin2dez(Bit21;Bit22;Bit23;Bit24)+ #temp3
       bin2dez(Bit25;Bit26;Bit27;Bit28)+ #hum1
       bin2dez(Bit29;Bit30;Bit31;Bit=„0“) = #hum2
       bin2dez(Bit32;Bit33;Bit34;Bit35;Bit36;Bit37) #checksum
       checksum = sum modulo 64
