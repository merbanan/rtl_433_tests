# CED7000 Shot timer

The **CED7000 Shot Timer** by [Competitive Edge Dynamics](https://www.cedhk.com) is a shot timer for USPSA / IPSC used in shooting ranges for matches and practice.

It was designed and manufactured by Longmax Industries Ltd.

## Alternatives
CED7000 and CED8000 are two models using the same RF protocol
* EU model works at 434.348Mhz
* US model works at ~314 Mhz

## Documentation
* [Instruction Manual](https://www.cedhk.com/images/CED7000Man08FinalLowRes1.pdf)
* [FCC application for the CED8000](https://fccid.io/SVVCED8000) (identical in RF)

## Data captured
Data captured at room temperature and ambient pressure, triggered using a sharp tap on the device.
Analysis shows that after each shot there is a burst of data for at least 4 values (RFID, Shot, Final, Split)

## Modulation
It seems like a FSK Manchester coding starting with a preamble of {12}0xfcf and  1300us symbol length.

The following rtl_433 options produce a bitstream that could be associated with the values we see on the device screen

```
 rtl_433 -X "n=CED7000,m=FSK_MC_ZEROBIT,s=1300,r=9000,preamble={12}0xfcf" -f 434348000 
```

## Captures

| Name                        	| RFID 	| Shot 	| Final 	| Split 	|
|-----------------------------	|------	|------	|-------	|-------	|
| CED7000-1_434.348M_250k.cu8 	| 0000	| 1    	|   1.92   	|  1.92 	|
| CED7000-2_434.348M_250k.cu8 	| 0000	| 2    	|   5.22	|  3.30 	|
| CED7000-3_434.348M_250k.cu8 	| 0000 	| 3    	|   9.18	|  3.96 	|
| CED7000-4_434.348M_250k.cu8 	| 0000 	| 4    	|  12.55	|  3.37 	|
| CED7000-5_434.348M_250k.cu8 	| 0000 	| 5    	|  15.19	|  2.64 	|
| CED7000-6_434.348M_250k.cu8 	| 0000 	| 6    	|  18.32	|  3.13 	|
| CED7000-7_434.348M_250k.cu8 	| 0000 	| 7    	|  21.45	|  3.13 	|
| CED7000-8_434.348M_250k.cu8 	| 0000 	| 8    	|  24.62	|  3.17 	|
| CED7000-9_434.348M_250k.cu8 	| 0000 	| 9    	|  27.75	|  3.13 	|
| CED7000-10_434.348M_250k.cu8 	| 0000 	| 10   	|  31.57	|  3.82 	|

## Encoding

Data seems to be encoded as LE decimal representations per seven segment digit with the following lenghts:

| Field 	| Length 	            | Description                            	|
|-------	|---------------------- |---------------------------------------	|
| RFID   	| 4 digits (16 bits)    | The unique RFID used to pair receivers 	|
| Shot  	| 2 digits (8 bits)    	| Counter of shots fired                	|
| Final  	| 5 digits (20 bits)  	| Total time from first to last shot (two decimals assumed)       |
| Split 	| 5 digits (20 bits)	| Time between consecutive shots (two decimals assumed)  |