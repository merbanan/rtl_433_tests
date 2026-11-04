#!/usr/bin/python3
"""
Generates test data for rlt_433 to detect zero pkt bug


    gen_zero.py [-pre] [bit_pat [MAX_DATA_LEN] ]

    Optional Args:
        bit_pat : test bit pattern, default 00
        MAX_DATA_LEN : max length for test data, default 400


    Example:
        python3 gen_zero.py > 0x00_data.txt

        rtl_433 -y @0x00_data.txt

        python3 gen_zero.py FF > 0xFF_data.txt

        python3 gen_zero.py -pre FF > 0x55FF_data.txt

"""
# Copyright (C) 2021 Peter Shipley
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

# from __future__ import absolute_import
import sys


# how far should we go ?
# Insteon pkts can be 896bit and i am sure it is not the longest
# but then the odds of consecutive zeros drops quicly with length


PREAMBLE = '5555'
WITH_PREAMBLE = 0
MAX_DATA_LEN = 400
PKT_PATTERN = '00'

args = sys.argv[1:]

# print("args",  args, args[0] ,args[0][0])

if args and args[0][0] == '-':
    x = args.pop(0)
    if x.startswith('-pre'):
        WITH_PREAMBLE = 1
    elif x.startswith('-nop'):
        WITH_PREAMBLE = 0

# print("args",  args)

if args:
    x = args.pop(0)
    if x.startswith('0x'):
        PKT_PATTERN = x[2:]
    else:
        PKT_PATTERN = x

if args:
    MAX_DATA_LEN = int(args[0])

# print("PAT={}\tLEN={}\tPRE={}".format(PKT_PATTERN, MAX_DATA_LEN, WITH_PREAMBLE))


def main():
    """
        Generate test data
    """

    patt_len = len(PKT_PATTERN)
    patt_bit_len = patt_len * 4

    pre_bit_len = 0
    preamble = ''
    # print("patt_len", patt_len, patt_bit_len)
    if WITH_PREAMBLE:
        pre_bit_len = len(PREAMBLE) * 4
        preamble = PREAMBLE

    tot_bytes = 1
    for bits in range(1, MAX_DATA_LEN):
        data_sample = "{{{}}}{}".format(bits + pre_bit_len, preamble + PKT_PATTERN * tot_bytes)
        print(data_sample)
        print((data_sample + " ") * 10)

        if bits % patt_bit_len == 0:
            tot_bytes += 1


if __name__ == "__main__":
    main()
