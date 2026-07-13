#!/usr/bin/env python3

"""Compare actual output lines of rtl_433 with reference json."""

import sys
import os
import argparse

import fnmatch
import subprocess
import json

from deepdiff import DeepDiff


def run_rtl433(input_fn, protocol=None, config=None, rtl_433_cmd="rtl_433"):
    """Run rtl_433 and return output."""
    args = ['-c', '0']
    if protocol:
        args.extend(['-R', str(protocol)])
    if config:
        args.extend(['-c', str(config)])
    args.extend(['-F', 'json', '-r', input_fn])
    cmd = [rtl_433_cmd] + args
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    # Pass warning messages through
    for line in err.decode("utf-8").split("\n"):
        if "WARNING:" in line:
            print(line)
    return (out, err, p.returncode)


def run_rtl433_y(code, protocol=None, config=None, rtl_433_cmd="rtl_433"):
    """Run rtl_433 -y <code> and return output."""
    args = ['-c', '0']
    if protocol:
        args.extend(['-R', str(protocol)])
    if config:
        args.extend(['-c', str(config)])
    args.extend(['-F', 'json', '-y', code])
    cmd = [rtl_433_cmd] + args
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    for line in err.decode("utf-8").split("\n"):
        if "WARNING:" in line:
            print(line)
    return (out, err, p.returncode)


def find_json(test_path="tests"):
    """Find all reference json files recursive, except codes_test.json
    (handled separately, paired with codes_test.txt rather than a capture)."""
    matches = []
    for root, _dirnames, filenames in os.walk(test_path):
        for filename in fnmatch.filter(filenames, '*.json'):
            if filename == 'codes_test.json':
                continue
            matches.append(os.path.join(root, filename))
    return matches


def find_codes_test(test_path="tests"):
    """Find all codes_test.txt files recursive."""
    matches = []
    for root, _dirnames, filenames in os.walk(test_path):
        if 'codes_test.txt' in filenames:
            matches.append(os.path.join(root, 'codes_test.txt'))
    return matches


def parse_codes_test(path):
    """Return the list of non-blank, non-comment code lines from a codes_test.txt."""
    codes = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            codes.append(line)
    return codes


def remove_fields(data, fields):
    """Remove all data fields to be ignored."""
    for outline in data:
        for field in fields:
            if field in outline:
                del outline[field]
    return data


def extract_results(rtl433out, expected_model, false_positives, input_fn):
    """Parse rtl_433's json-lines output, splitting out lines whose model
    doesn't match the expected one into false_positives (tracked by actual
    model seen), returning the remaining (matching or model-less) results."""
    results = []
    rtl433out = rtl433out.decode('utf8').strip()
    for json_line in rtl433out.split("\n"):
        if not json_line.strip():
            continue
        try:
            data = json.loads(json_line)
            if "model" in data:
                actual_model = data["model"]
                if actual_model != expected_model:
                    if actual_model not in false_positives:
                        false_positives[actual_model] = dict()
                        false_positives[actual_model]["count"] = 1
                        false_positives[actual_model]["models"] = set()
                        false_positives[actual_model]["models"].add(expected_model)
                    else:
                        false_positives[actual_model]["count"] += 1
                        false_positives[actual_model]["models"].add(expected_model)
                    continue
            results.append(data)
        except ValueError:
            print("## Fail with '%s': invalid json output" % input_fn)
            print("%s" % json_line)
            results.append(None)  # caller counts this as a failure
    return results


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
    parser.add_argument('-t', '--test-path', default="tests",
                        help='path to the tests location')
    args = parser.parse_args()

    rtl_433_cmd = args.rtl433_cmd
    config_path = args.config_path
    ignore_fields = args.ignore_field
    first_line = args.first_line
    test_path = args.test_path

    expected_json = find_json(test_path)
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
        rtl433out, _err, exitcode = run_rtl433(input_fn,
                                               protocol, config, rtl_433_cmd)

        if exitcode:
            print("ERROR: Exited with %d '%s'" % (exitcode, input_fn))

        # get JSON results
        expected_model = expected_data[0]["model"] if expected_data else None
        results = extract_results(rtl433out, expected_model, false_positives, input_fn)
        nb_fail += results.count(None)
        results = [r for r in results if r is not None]
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

    # codes_test.txt / codes_test.json: dense corpora of already-demodulated
    # {N}<hex> codes fed through `-y`, one code per expected json line.
    for codes_fn in find_codes_test(test_path):
        output_fn = os.path.join(os.path.dirname(codes_fn), "codes_test.json")
        if not os.path.isfile(output_fn):
            print("WARNING: Missing '%s'" % output_fn)
            continue

        ignore_fn = os.path.join(os.path.dirname(codes_fn), "ignore")
        if os.path.isfile(ignore_fn):
            print("WARNING: Ignoring '%s'" % codes_fn)
            continue

        protocol = None
        protocol_fn = os.path.join(os.path.dirname(codes_fn), "protocol")
        if os.path.isfile(protocol_fn):
            with open(protocol_fn, "r") as protocol_file:
                protocol = protocol_file.readline().strip()

        config = None
        if protocol and os.path.isfile(os.path.join(config_path, protocol)):
            config = os.path.join(config_path, protocol)
            protocol = None

        codes = parse_codes_test(codes_fn)

        expected_lines = []
        with open(output_fn, "r") as output_file:
            try:
                for json_line in output_file.readlines():
                    if not json_line.strip():
                        continue
                    expected_lines.append(json.loads(json_line))
            except ValueError:
                print("ERROR: invalid json: '%s'" % output_fn)
                continue
        expected_lines = remove_fields(expected_lines, ignore_fields)

        if len(codes) != len(expected_lines):
            nb_fail += 1
            print("## Fail with '%s': %d codes but %d expected lines in '%s'"
                  % (codes_fn, len(codes), len(expected_lines), output_fn))
            continue

        for i, (code, expected_data) in enumerate(zip(codes, expected_lines)):
            label = "%s [%d] '%s'" % (codes_fn, i, code)

            rtl433out, _err, exitcode = run_rtl433_y(code, protocol, config, rtl_433_cmd)
            if exitcode:
                print("ERROR: Exited with %d '%s'" % (exitcode, label))

            results = extract_results(rtl433out, expected_data.get("model"), false_positives, label)
            nb_fail += results.count(None)
            results = [r for r in results if r is not None]
            results = remove_fields(results, ignore_fields)
            result = results[0] if results else {}

            diff = DeepDiff(expected_data, result)
            if diff:
                nb_fail += 1
                print("## Fail with '%s':" % label)
                for error, details in diff.items():
                    print(" %s" % error)
                    for detail in details:
                        print("  * %s" % detail)
                print(" Expected: " + str(expected_data))
                print("  But got: " + str(result))
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
