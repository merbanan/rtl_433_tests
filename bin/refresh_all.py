#!/usr/bin/env python

"""Refresh rtl_433 JSON outputs."""

import sys
import os
import fnmatch
import subprocess
import json


def run_rtl433(input_fn, samplerate=None, protocol=None, rtl_433_cmd="rtl_433"):
    """Run rtl_433 and return output."""
    args = ['-c', '0', '-M', 'newmodel']
    if protocol:
        args.extend(['-R', str(protocol)])
    if samplerate:
        args.extend(['-s', str(samplerate)])
    args.extend(['-F', 'json', '-r', input_fn])
    cmd = [rtl_433_cmd] + args
    # print(" ".join(cmd))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return (out, err, p.returncode)


def convert(root, filename):
    output_fn = os.path.join(root, filename)

    input_fn = os.path.splitext(output_fn)[0] + ".cu8"
    if not os.path.isfile(input_fn):
        print("WARNING: Missing '%s'" % input_fn)
        return

    ignore_fn = os.path.join(os.path.dirname(output_fn), "ignore")
    if os.path.isfile(ignore_fn):
        print("WARNING: Ignoring '%s'" % input_fn)
        return

    samplerate = 250000
    samplerate_fn = os.path.join(os.path.dirname(output_fn), "samplerate")
    if os.path.isfile(samplerate_fn):
        with open(samplerate_fn, "r") as samplerate_file:
            samplerate = int(samplerate_file.readline())

    protocol = None
    protocol_fn = os.path.join(os.path.dirname(output_fn), "protocol")
    if os.path.isfile(protocol_fn):
        with open(protocol_fn, "r") as protocol_file:
            protocol = int(protocol_file.readline())

    # Open expected data
    old_data = []
    with open(output_fn, "r") as output_file:
        old_data = output_file.read().splitlines()

    # Run rtl_433
    out, _err, exitcode = run_rtl433(input_fn, samplerate, protocol)

    if exitcode:
        print("ERROR: Exited with %d '%s'" % (exitcode, input_fn))

    # get JSON results
    out = out.decode('ascii')
    new_data = out.splitlines()

    if len(old_data) != len(new_data):
        print("\nWARNING: Different data for '%s'" % (input_fn))
        print('\n'.join(old_data))
        print("vs.")
        print('\n'.join(new_data))

    with open(output_fn, "w") as output_file:
        output_file.write('\n'.join(new_data))
        output_file.write('\n')


def main():
    """Process all reference json files."""

    for root, _dirnames, filenames in os.walk('tests'):
        for filename in fnmatch.filter(filenames, '*.json'):
            convert(root, filename)


if __name__ == '__main__':
    sys.exit(main())
