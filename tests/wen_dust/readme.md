# Captures
WEN 3410 3-Speed Remote-Controlled Air Filtration System (300/350/400 CFM)
Remote is 3410-029RF-01

433MHz OOK/PWM

3 buttons

2 bytes
Preamble 3C/SYNC

OFF - 1001 0001  = 0x6e = 110d
ON -  1001 1110  = 0x61 = 97d
TIME  0011 0111  = 0xC8 = 200d


This matches the actual individual packets
```
rtl_433 off.cu8 -X 'n=WEN3410,m=OOK_PWM,s=316,l=944,r=9156,g=968,t=253,preamble=3c,get=@0:{8}:CMD:[110:OFF 97:ON 200:TIME],unique,repeats=3'
```

This will make the whole transmission 1 packet with 4 rows - 1 row for match,
3 for actual data (duplicated)
```
rtl_433 off.cu8 -X 'n=WEN3410,m=OOK_PWM,s=316,l=944,r=11000,g=1100,match={25}ffffff8,preamble=3c,get=@0:{8}:CMD:[110:OFF 97:ON 200:TIME],unique'
```