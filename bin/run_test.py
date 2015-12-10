#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
import argparse

import fnmatch
import subprocess
import json

from deepdiff import DeepDiff

def run_rtl433(input_fn, rtl_433_cmd="rtl_433"):
    cmd = [rtl_433_cmd, '-F', 'json', '-r', input_fn]
    #print(" ".join(cmd))
    p = subprocess.Popen(cmd,
          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return (out, err)

def find_json():
    matches = []
    for root, dirnames, filenames in os.walk('tests'):
        for filename in fnmatch.filter(filenames, '*.json'):
            matches.append(os.path.join(root, filename))
    return matches

def remove_fields(data, fields):
    for field in fields:
        if field in data:
            del data[field]
    return data

def main():
    parser = argparse.ArgumentParser(description='Test rtl_433')
    parser.add_argument('-c', '--rtl433-cmd', default="rtl_433",
                   help='rtl_433 command')
    parser.add_argument('-I', '--ignore-field', default=[], action="append",
                   help='Field to ignore in JSON data')
    args = parser.parse_args()

    rtl_433_cmd = args.rtl433_cmd
    ignore_fields = args.ignore_field

    expected_json = find_json()
    nb_ok = 0
    nb_fail = 0
    for output_fn in expected_json:
        input_fn = os.path.splitext(output_fn)[0] + ".data"
        if not os.path.isfile(input_fn):
            print("WARNING: Missing '%s'" % input_fn)
            continue

        # Open expected data
        with open(output_fn, "r") as output_file:
            try:
                expected_data = json.load(output_file)
            except ValueError as err:
                print("ERROR: invalid json: '%s'" % output_fn)
                continue
            expected_data = remove_fields(expected_data, ignore_fields)

        # Run rtl_433
        rtl433out, err = run_rtl433(input_fn, rtl_433_cmd)

        # get JSON results, keep only first line for now
        rtl433out = rtl433out.strip()
        rtl433out = rtl433out.split("\n")[0]
        results = json.loads(rtl433out)
        results = remove_fields(results, ignore_fields)


        # Compute the diff
        diff = DeepDiff(expected_data, results)
        if(diff):
            nb_fail += 1
            print("## Fail with '%s':" % input_fn)
            for error, details in diff.items():
                print(" %s" %error)
                for detail in details:
                    print("  * %s" %detail)
        else:
            nb_ok += 1

    # print some summary
    print("%d records tested, %d have fail" % (nb_ok+nb_fail, nb_fail))

if __name__ == '__main__':
    sys.exit(main())
