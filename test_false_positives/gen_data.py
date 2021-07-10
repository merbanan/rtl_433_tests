#!/usr/bin/python3
"""
Generates test data for rlt_433 to detect zero pkt bug


    gen_zero.py [bit_pat] [MAX_DATA_LEN]

    Optional Args:
        bit_pat : test bit pattern, default 00
        MAX_DATA_LEN : max length for test data, default 400


    Example:
        python3 gen_zero.py > 0x00_data.txt

        rtl_433 -y @0x00_data.txt

        python3 gen_zero.py FF > 0xFF_data.txt

"""
#    Copyright (C) 2021 Peter Shipley
#
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.

import sys


# how far should we go ?
# Insteon pkts can be 896bit and i am sure it is not the longest
# but then the odds of consecutive zeros drops quicly with length


MAX_DATA_LEN = 400
PKT_PATTERN = '00'

if len (sys.argv) > 1:
    x = sys.argv[1]
    if x.startswith('0x'):
        PKT_PATTERN = x[2:]
    else:
        PKT_PATTERN = x

if len (sys.argv) > 2:
    MAX_DATA_LEN = int(sys.argv[2])

def main():
    """
        Generate test data
    """

    patt_len = len(PKT_PATTERN)
    patt_bit_len = patt_len * 4

    # print("patt_len", patt_len, patt_bit_len)

    tot_bytes = 1
    for bits in range(1, MAX_DATA_LEN):
        data_sample = "{{{}}}{}".format(bits, PKT_PATTERN * tot_bytes)
        print(data_sample)
        print( (data_sample + " ") * 10)

        if bits % patt_bit_len == 0:
            tot_bytes += 1


if __name__ == "__main__":
    main()
