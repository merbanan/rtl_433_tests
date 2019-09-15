# ThermoPro TP-11 Wireless Meat Thermometer

[Product page](https://itronicsmall.com/products/thermopro-tp-11)
[Discussion](https://groups.google.com/d/msg/rtl_433/KgKEs6rg9u0/kxeF0Ym1AQAJ)

## Data capture log

	*** signal_start = 1859191, signal_end = 1930266
	signal_len = 71075,  pulses = 135
	Iteration 1. t: 124    min: 123 (68)    max: 125 (67)    delta 10
	Iteration 2. t: 123    min: 122 (30)    max: 124 (105)    delta 2
	Iteration 3. t: 123    min: 122 (3)    max: 124 (132)    delta 0
	Distance coding: Pulse length 123
	
	Short distance: 119, long distance: 359, packet distance: 851
	
	p_limit: 123
	bitbuffer:: Number of rows: 4 
	[00] {33} db 41 57 c2 80 : 11011011 01000001 01010111 11000010 1
	[01] {33} db 41 57 c2 80 : 11011011 01000001 01010111 11000010 1
	[02] {33} db 41 57 c2 80 : 11011011 01000001 01010111 11000010 1
	[03] {32} db 41 57 c2 : 11011011 01000001 01010111 11000010 
	signal_bszie = 262144  -      sg_index = 1048576
	start_pos    = 452658  -   buffer_size = 3145728
	*** Saving signal to file gfile001.data
	*** Writing data from 452658, len 262144

## Analysis

The data repeats 4 times. The nibbles can be grouped into three fields:

* db4: probably device ID, does not seem to change very much
* 157: temperature in 0.1C units with zero at -20C (e.g. (0x157-200)/10 = 14.3C)
* c2:  validation code

Validation code seems to be computed from the first three bytes. The function F
that computes the code seems to be linear in this sense: F(x^y) = F(x)^F(y)

The following snippet validates the code for the two known sensors (with
device IDs 0xdb4 and 0xb34), but most likely will not work for others.

	bool valid(int b0, int b1, int b2, int b3) {
	  static int t[] = {0x04,0x08,0x10,0x20,
	                    0x40,0x80,0x51,0xa2,
	                    0x15,0x2a,0x54,0xa8,
	                    0x00,0x00,0xed,0x00,
	                    0x00,0x00,0x00,0x37,
	                    0x00,0x00,0x00,0x00};
	  int x = (b0 << 16) + (b1 << 8) + b2;
	  for(int i = 0; i<24; i++) {
	    if (x & (1<<i)) b3 ^= t[i];
	  }
	  return b3 == 0;
	}
