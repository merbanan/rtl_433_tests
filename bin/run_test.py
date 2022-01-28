#!/usr/bin/env python3

"""Compare actual output lines of rtl_433 with reference json."""

import sys
import os
import argparse

import fnmatch
import subprocess
import json

from deepdiff import DeepDiff


def run_rtl433(input_fn, samplerate=None, protocol=None, config=None, rtl_433_cmd="rtl_433"):
    """Run rtl_433 and return output."""
    args = ['-c', '0']
    if protocol:
        args.extend(['-R', str(protocol)])
    if config:
        args.extend(['-c', str(config)])
    if samplerate:
        args.extend(['-s', str(samplerate)])
    args.extend(['-F', 'json', '-r', input_fn])
    cmd = [rtl_433_cmd] + args
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    # Pass warning messages through
    for line in err.decode("utf-8").split("\n"):
        if "WARNING:" in line:
            print(line)
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
    parser.add_argument('-C', '--config-path', default="../conf",
                        help='rtl_433 command')
    parser.add_argument('-I', '--ignore-field', default=[], action="append",
                        help='Field to ignore in JSON data')
    parser.add_argument('--first-line', default=False, action="store_true",
                        help='Only compare the first outputed line of rtl433'
                             ' with first line of reference json')
    args = parser.parse_args()

    rtl_433_cmd = args.rtl433_cmd
    config_path = args.config_path
    ignore_fields = args.ignore_field
    first_line = args.first_line

    expected_json = find_json()
    nb_ok = 0
    nb_fail = 0
    false_positives = dict()
    for output_fn in expected_json:
        input_fn = os.path.splitext(output_fn)[0] + ".cu8"
        inook_fn = os.path.splitext(output_fn)[0] + ".ook"
        if not os.path.isfile(input_fn):
            if os.path.isfile(inook_fn):
                input_fn = inook_fn
            else:
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
                protocol = protocol_file.readline().strip()

        config = None
        if protocol and os.path.isfile(os.path.join(config_path, protocol)):
            config = os.path.join(config_path, protocol)
            protocol = None

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
                                               protocol, config, rtl_433_cmd)

        if exitcode:
            print("ERROR: Exited with %d '%s'" % (exitcode, input_fn))

        # get JSON results
        rtl433out = rtl433out.decode('utf8').strip()
        results = []
        for json_line in rtl433out.split("\n"):
            if not json_line.strip():
                continue
            try:
                data = json.loads(json_line)
                if "model" in data:
                    expected_model = expected_data[0]["model"]
                    actual_model = data["model"]
                    if actual_model != expected_model:
                        if actual_model not in false_positives:
                            false_positives[actual_model] = dict()
                            false_positives[actual_model]["count"] = 1
                            false_positives[actual_model]["models"] = set()
                            false_positives[actual_model]["models"].add(expected_model)
                        else:
                            false_positives[actual_model]["count"]  += 1
                            false_positives[actual_model]["models"].add(expected_model)
                        continue
                results.append(data)
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

    for model, values in false_positives.items():
        count = values["count"]
        models = values["models"]
        print(f"WARNING: {model} generated {count} false positive(s) in other decoders: {models}")

    # print some summary
    print("%d records tested, %d have failed" % (nb_ok+nb_fail, nb_fail))
    return nb_fail


if __name__ == '__main__':
    sys.exit(main())
