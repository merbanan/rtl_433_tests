#!/usr/bin/env python

"""Compare actual output lines of rtl_433 with reference json."""

import sys
import os
import argparse

import fnmatch
import subprocess
import json

from deepdiff import DeepDiff


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


def find_json():
    """Find all reference json files recursive."""
    matches = []
    for root, _dirnames, filenames in os.walk('tests'):
        for filename in fnmatch.filter(filenames, '*.json'):
            matches.append(os.path.join(root, filename))
    return matches


def remove_fields(data, fields):
    """Remove all data fields to be ignored."""
    for outline in data:
        for field in fields:
            if field in outline:
                del outline[field]
    return data


def main():
    """Check all reference json files vs actual output."""
    parser = argparse.ArgumentParser(description='Test rtl_433')
    parser.add_argument('-c', '--rtl433-cmd', default="rtl_433",
                        help='rtl_433 command')
    parser.add_argument('-I', '--ignore-field', default=[], action="append",
                        help='Field to ignore in JSON data')
    parser.add_argument('--first-line', default=False, action="store_true",
                        help='Only compare the first outputed line of rtl433'
                             ' with first line of reference json')
    args = parser.parse_args()

    rtl_433_cmd = args.rtl433_cmd
    ignore_fields = args.ignore_field
    first_line = args.first_line

    expected_json = find_json()
    nb_ok = 0
    nb_fail = 0
    for output_fn in expected_json:
        input_fn = os.path.splitext(output_fn)[0] + ".cu8"
        if not os.path.isfile(input_fn):
            print("WARNING: Missing '%s'" % input_fn)
            continue

        ignore_fn = os.path.join(os.path.dirname(output_fn), "ignore")
        if os.path.isfile(ignore_fn):
            print("WARNING: Ignoring '%s'" % input_fn)
            continue

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
        expected_data = []
        with open(output_fn, "r") as output_file:
            try:
                for json_line in output_file.readlines():
                    if not json_line.strip():
                        continue
                    expected_data.append(json.loads(json_line))
            except ValueError as _err:
                print("ERROR: invalid json: '%s'" % output_fn)
                continue
            expected_data = remove_fields(expected_data, ignore_fields)

        # Run rtl_433
        rtl433out, _err, exitcode = run_rtl433(input_fn, samplerate,
                                               protocol, rtl_433_cmd)

        if exitcode:
            print("ERROR: Exited with %d '%s'" % (exitcode, input_fn))

        # get JSON results
        rtl433out = rtl433out.decode('utf8').strip()
        results = []
        for json_line in rtl433out.split("\n"):
            if not json_line.strip():
                continue
            try:
                results.append(json.loads(json_line))
            except ValueError:
                nb_fail += 1
                # TODO: factorise error print
                print("## Fail with '%s': invalid json output" % input_fn)
                print("%s" % json_line)
                continue
        results = remove_fields(results, ignore_fields)

        if first_line:
            if len(results) == 0:
                results.append({})
            if len(expected_data) == 0:
                expected_data.append({})
            expected_data, results = expected_data[0], results[0]

        # Compute the diff
        diff = DeepDiff(expected_data, results)
        if diff:
            nb_fail += 1
            print("## Fail with '%s':" % input_fn)
            for error, details in diff.items():
                print(" %s" % error)
                for detail in details:
                    print("  * %s" % detail)
            print(" Expected: " + str(expected_data))
            print("  But got: " + str(results))
        else:
            nb_ok += 1

    # print some summary
    print("%d records tested, %d have failed" % (nb_ok+nb_fail, nb_fail))
    return nb_fail


if __name__ == '__main__':
    sys.exit(main())
