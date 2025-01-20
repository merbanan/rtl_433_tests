# Captures
WEN shop air cleaner
Remote is 3410-029RF-01

433MHz OOK/PWM

3 buttons

2 bytes
Preamble 3C

OFF - 1001 0001  = 0x6e = 110d
ON -  1001 1110  = 0x61 = 97d
TIME  0011 0111  = 0xC8 = 200d


get=@00:{8}:event:[6e:off 61:on ce:time]


rtl_433 off.cu8 -X 'n=WEN,m=OOK_PWM,s=316,l=944,r=9156,g=968,t=253,y=0,preamble=3c,get=@0:{8}:event:[110:off 61:on ce:speed]'
