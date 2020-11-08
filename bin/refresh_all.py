#!/usr/bin/env python3

"""Refresh rtl_433 JSON outputs."""

import argparse
import sys
import os
import fnmatch
import subprocess
import json

def run_rtl433(input_fn, samplerate=None, protocol=None, rtl_433_cmd="rtl_433"):
    """Run rtl_433 and return output."""
    args = ['-c', '0']
    if protocol:
        args.extend(['-R', str(protocol)])
    if samplerate:
        args.extend(['-s', str(samplerate)])
    args.extend(['-F', 'json', '-r', input_fn])
    cmd = [rtl_433_cmd] + args
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return (out, err, p.returncode)


def get_model_from_json(json_str):
    try:
        decoded = json.loads(json_str)
        return decoded["model"]
    # TODO: what exceptions can we expect?
    except Exception as e:
        print("ERROR: exception:", e)
    return None


def matches_model(expected_model, data):
    model = get_model_from_json(data)
    return model == expected_model


def convert(root, filename, rtl_path):
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
            protocol = protocol_file.readline().strip()

    # Open expected data
    old_data = []
    with open(output_fn, "r") as output_file:
        old_data = output_file.read().splitlines()

    expected_model = None
    if len(old_data) > 0:
        expected_model = get_model_from_json(old_data[0])

    # Run rtl_433
    out, _err, exitcode = run_rtl433(input_fn, samplerate, protocol, rtl_path)

    if exitcode:
        print("ERROR: Exited with %d '%s'" % (exitcode, input_fn))

    # get JSON results
    out = out.decode('ascii')
    new_data = out.splitlines()

    new_data_without_false_positives = []
    if expected_model:
        for item in new_data:
            if matches_model(expected_model, item):
                new_data_without_false_positives.append(item)
            else:
                # This is a false positive
                pass
    if len(new_data_without_false_positives) > 0:
        false_positives = len(new_data) - len(new_data_without_false_positives)
        if false_positives:
            print(f"INFO: {input_fn} ({expected_model}) generated {false_positives} false positives")
        new_data = new_data_without_false_positives

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
    parser = argparse.ArgumentParser(description='Update reference json files')
    parser.add_argument('-c', '--rtl433-cmd', default='rtl_433',
            help='rtl_433 command')
    args = parser.parse_args()

    rtl_433_cmd = args.rtl433_cmd

    for root, _dirnames, filenames in os.walk('tests'):
        for filename in fnmatch.filter(filenames, '*.json'):
            convert(root, filename, rtl_433_cmd)


if __name__ == '__main__':
    sys.exit(main())
