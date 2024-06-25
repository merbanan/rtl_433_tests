
# ARAD / Master Meter Dialog3G Water utility  meter


 [![image](https://github.com/avicarmeli/rtl_433_tests/assets/32562196/f8b5d2ca-9960-4d50-87aa-c5e46b024c86)](https://github.com/avicarmeli/rtl_433_tests/blob/master/tests/arad_ms_meter/Dialog3Gs.png) 

## General Info
Arad/Master Meter Dialog3G water utility meter.

FCC-Id: TKCET-733

Transmit in 916.3Mhz

Prodact [brochure](https://github.com/avicarmeli/rtl_433_tests/blob/master/tests/arad_ms_meter/Dialog-3G-register-information-sheet_Eng-002.pdf)

## Massage Format

Massage is being sent once every 30 second.

The massage look like that:

00000000FFFFFFFFFFFFFFSSSSSSSSXXCCCCCCXXXF?????????XFF

where:

00000000 is preamble.

FFFFFFFFFFFFFF  is fixed in time and the same for other meters in the neighborhood. Probably gearing ratio. The payload is 3e690aec7ac84b.

SSSSSSSS  is Meter serial number.  for instance fa1c9073 =>  fa1c90 = 09444602, little endian 73= 'S'

XX no idea.

CCCCCC is the counter reading little endian for instance a80600= 1704

XXX no idea.

F  is fixed in time and the same for other meters in the neighborhood. With payload of 5.

????????? probably some kind of CRC or checksum - here is where I need help.

X is getting either 8 or 0 same for other meters in the neighborhood.

FF is fixed in time and the same for other meters in the neighborhood.With payload f8.

## Discussion

Here is a [link](https://github.com/merbanan/rtl_433/issues/1992) to discustion about reverse engineering the water meter.

## To Do
- [ ] Find which method is used for message integrity check (MIC).
- [ ] Decode other pasrts of the message

Here is some collected data maybe someone can figure out the MIC:

| Date	 | Hour	| Length	| Payload |	sofix	| mid	| counter	| serial	| prefix	| sync |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19/03/2022	| 13:24:51	| 177	| 000000003e690aec7ac84b80f98b7300030d0000056f9810d018f8	| f8	| 00056f9810d018	| 3331	| 9173376	| 3e690aec7ac84b	| 00000000|
| 19/03/2022	| 13:27:21	| 177	| 000000003e690aec7ac84b80f98b7300030d0000056f9810d018f8	| f8	| 00056f9810d018	| 3331	| 9173376	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:29:51	| 178	| 000000003e690aec7ac84b80f98b7300030d0000056f9810d018fc	| fc	| 00056f9810d018	| 3331	| 9173376	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:25:06	| 178	| 000000003e690aec7ac84b13fe8b73001b050000052880d318f8f8	| f8	| 00052880d318f8	| 1307	| 9174547	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:36:05	| 177	| 000000003e690aec7ac84be20a8c7300a41e00000572730b7d08f8	| f8	| 000572730b7d08	| 7844	| 9177826	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:36:35	| 176	| 000000003e690aec7ac84be20a8c7300a41e00000572730b7d08f 	| f 	| 000572730b7d08	| 7844	| 9177826	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:34:21	| 177	| 000000003e690aec7ac84b27108c73006d060000052d17d1da88f8	| f8	| 00052d17d1da88	| 1645	| 9179175	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:36:21	| 178	| 000000003e690aec7ac84b27108c73006d060000052d17d1da88fc	| fc	| 00052d17d1da88	| 1645	| 9179175	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:36:52	| 177	| 000000003e690aec7ac84b27108c73006d060000052d17d1da88f8	| f8	| 00052d17d1da88	| 1645	| 9179175	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:21:35	| 177	| 000000003e690aec7ac84b3ec68c73009d0e000005cc7333ecf0f8 	| f8	| 0005cc7333ecf0	| 3741	| 9225790	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:22:05	| 177	| 000000003e690aec7ac84b3ec68c73009d0e000005cc7333ecf0f8	| f8	| 0005cc7333ecf0	| 3741	| 9225790	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:34:28	| 177	| 000000003e690aec7ac84b63868d7300de0b0000052ae1686bb0f8	| f8	| 00052ae1686bb0	| 3038	| 9274979	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:36:28	| 177	| 000000003e690aec7ac84b63868d7300de0b0000052ae1686bb0f8	| f8	| 00052ae1686bb0	| 3038	| 9274979	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:31:47	| 178	| 000000003e690aec7ac84b45b48d7300ee110000054b1eef6b68fc	| fc	| 00054b1eef6b68	| 4590	| 9286725	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:32:17	| 178	| 000000003e690aec7ac84b45b48d7300ee110000054b1eef6b68fc	| fc	| 00054b1eef6b68	| 4590	| 9286725	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:31:46	| 178	| 000000003e690aec7ac84b6ec98d7300210a00000514db854b40fc	| fc	| 000514db854b40	| 2593	| 9292142	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:32:16	| 178	| 000000003e690aec7ac84b6ec98d7300210a00000514db854b40fc	| fc	| 000514db854b40	| 2593	| 9292142	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:34:40	| 177	| 000000003e690aec7ac84b9da68e0000a2010000058f1243d568f8	| f8	| 00058f1243d568	| 418	9| 348765	3| e690aec7ac84b	0| 0000000|
| 19/03/2022	| 13:36:10	| 177	| 000000003e690aec7ac84b9da68e0000a2010000058f1243d568f8	| f8	| 00058f1243d568	| 418	9| 348765	3| e690aec7ac84b	0| 0000000|
| 19/03/2022	| 13:36:40	| 176	| 000000003e690aec7ac84b9da68e0000a2010000058f1243d568f 	| f 	| 00058f1243d568	| 418	9| 348765	3| e690aec7ac84b	0| 0000000 |
| 19/03/2022	| 13:17:49	| 177	| 000000003e690aec7ac84bfa1c907300e806000005ea10fef8b8f8	| f8	| 0005ea10fef8b8	| 1768	| 9444602	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:27:05	| 178	| 000000003e690aec7ac84bdff7930000700b000005a6bb965e08fc	| fc	| 0005a6bb965e08	| 2928	| 9697247	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:27:35	| 178	| 000000003e690aec7ac84bdff7930000700b000005a6bb965e08fc	| fc	| 0005a6bb965e08	| 2928	| 9697247	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:29:35	| 178	| 000000003e690aec7ac84bdff7930000700b000005a6bb965e08fc	| fc	| 0005a6bb965e08	| 2928	| 9697247	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:30:05	| 178	| 000000003e690aec7ac84bdff7930000700b000005a6bb965e08fc	| fc	| 0005a6bb965e08	| 2928	| 9697247	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:24:50	| 177	| 000000003e690aec7ac84bcf9dde7340acf803000c10d65c6f48f8	| f8	|000c10d65c6f48	| 260268	| 14589391	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:25:08	| 177	| 000000003e690aec7ac84bcf9dde7340acf803000c10d65c6f48f8	| f8	| 000c10d65c6f48	| 260268	| 14589391	| 3e690aec7ac84b	| 00000000| 
| 19/03/2022	| 13:25:26	| 177	| 000000003e690aec7ac84bcf9dde7340acf803000c10d65c6f48f8	| f8	| 000c10d65c6f48	| 260268	| 14589391	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:25:44	| 176	| 000000003e690aec7ac84bcf9dde7340acf803000c10d65c6f48f	| f 	| 000c10d65c6f48	| 260268	| 14589391	| 3e690aec7ac84b	| 00000000 |
| 19/03/2022	| 13:24:56	| 177	| 000000003e690aec7ac86b68e3de734036430500085d997ed2e0f8	| f8	| 00085d997ed2e0	| 344886	| 14607208	| 3e690aec7ac86b	| 00000000 |
| 19/03/2022	| 13:25:26	| 177	| 000000003e690aec7ac86b68e3de734036430500085d997ed2e0f8	| f8	| 00085d997ed2e0	| 344886	| 14607208	| 3e690aec7ac86b	| 00000000 |

