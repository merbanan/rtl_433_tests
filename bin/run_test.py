#!/usr/bin/env python3

"""Compare actual output lines of rtl_433 with reference json."""

import sys
import os
import argparse

import fnmatch
import shlex
import subprocess
import json

from deepdiff import DeepDiff


def run_rtl433(input_fn=None, test_data=None, protocol=None, demod_args=None,
                config=None, rtl_433_cmd="rtl_433"):
    """Run rtl_433 on a file (input_fn) or a literal bitbuffer code
    (test_data, via -y) and return its output."""
    args = ['-c', '0']
    if protocol:
        args.extend(['-R', str(protocol)])
    if demod_args:
        args.extend(demod_args)
    if config:
        args.extend(['-c', str(config)])
    args.extend(['-F', 'json'])
    if test_data is not None:
        args.extend(['-y', test_data])
    else:
        args.extend(['-r', input_fn])
    cmd = [rtl_433_cmd] + args
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    # Pass warning messages through
    for line in err.decode("utf-8").split("\n"):
        if "WARNING:" in line:
            print(line)
    return (out, err, p.returncode)


def find_json(test_path="tests"):
    """Find all reference json files recursive."""
    matches = []
    for root, _dirnames, filenames in os.walk(test_path):
        for filename in fnmatch.filter(filenames, '*.json'):
            # codes_test.json is handled separately, by find_codes_test()
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


def parse_codes_test(codes_fn):
    """Parse a codes_test.txt file into a list of {N}<hex> bitbuffer codes,
    stripping blank lines and comments (a bare '#' and anything after it)."""
    codes = []
    with open(codes_fn, "r") as codes_file:
        for line in codes_file:
            line = line.split('#', 1)[0].strip()
            if line.startswith('{'):
                codes.append(line)
    return codes


def read_protocol(dirname, config_path):
    """Read a directory's optional 'protocol' file, resolving it to either
    a -R protocol arg or a -c config file path."""
    protocol = None
    protocol_fn = os.path.join(dirname, "protocol")
    if os.path.isfile(protocol_fn):
        with open(protocol_fn, "r") as protocol_file:
            protocol = protocol_file.readline().strip()

    config = None
    if protocol and os.path.isfile(os.path.join(config_path, protocol)):
        config = os.path.join(config_path, protocol)
        protocol = None

    return protocol, config


def read_demod_args(dirname):
    """Read a directory's optional 'demod' file: extra rtl_433 args (e.g.
    '-Y minmax' or '-Y level=-14') needed to demodulate its capture(s),
    for signals the default pulse detector can't recover on its own."""
    demod_fn = os.path.join(dirname, "demod")
    if not os.path.isfile(demod_fn):
        return None
    with open(demod_fn, "r") as demod_file:
        return shlex.split(demod_file.read())


def read_repeat_count(dirname):
    """Read a directory's optional 'repeat' file: how many identical rows
    each codes_test.txt code must be expanded to before decoding, for
    decoders that require multiple repeated rows to trust a message
    (e.g. bitbuffer_find_repeated_prefix with min_repeats > 1). A single
    {N}<hex> code is exactly one row, so such decoders never trigger on
    it unless it's repeated here first."""
    repeat_fn = os.path.join(dirname, "repeat")
    if not os.path.isfile(repeat_fn):
        return 1
    with open(repeat_fn, "r") as repeat_file:
        return int(repeat_file.read().strip())


def remove_fields(data, fields):
    """Remove all data fields to be ignored."""
    for outline in data:
        for field in fields:
            if field in outline:
                del outline[field]
    return data


def parse_results(raw_out, ignore_fields, expected_data, false_positives):
    """Parse rtl_433's json-lines stdout into a list of dicts, splitting
    off any output whose model doesn't match one of expected_data's models
    into false_positives instead. Returns (results, nb_invalid_json)."""
    expected_models = {d["model"] for d in expected_data if "model" in d}
    results = []
    nb_invalid = 0
    for json_line in raw_out.decode('utf8').strip().split("\n"):
        if not json_line.strip():
            continue
        try:
            data = json.loads(json_line)
        except ValueError:
            nb_invalid += 1
            print("## Fail: invalid json output")
            print("%s" % json_line)
            continue
        if "model" in data:
            actual_model = data["model"]
            if actual_model not in expected_models:
                expected_model = expected_data[0]["model"]
                fp = false_positives.setdefault(actual_model, {"count": 0, "models": set()})
                fp["count"] += 1
                fp["models"].add(expected_model)
                continue
        results.append(data)
    return remove_fields(results, ignore_fields), nb_invalid


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
        dirname = os.path.dirname(output_fn)
        input_exts = ['.cu8', '.cs8', '.cs16', '.ook']
        for input_ext in input_exts:
            input_fn = os.path.splitext(output_fn)[0] + input_ext
            if os.path.isfile(input_fn):
                break
        else:
            print("WARNING: Missing for '%s'" % output_fn)
            continue

        ignore_fn = os.path.join(dirname, "ignore")
        if os.path.isfile(ignore_fn):
            print("WARNING: Ignoring '%s'" % input_fn)
            continue

        protocol, config = read_protocol(dirname, config_path)
        demod_args = read_demod_args(dirname)

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
        rtl433out, _err, exitcode = run_rtl433(input_fn, protocol=protocol,
                                               demod_args=demod_args, config=config,
                                               rtl_433_cmd=rtl_433_cmd)

        if exitcode:
            print("ERROR: Exited with %d '%s'" % (exitcode, input_fn))

        results, nb_invalid = parse_results(rtl433out, ignore_fields, expected_data, false_positives)
        nb_fail += nb_invalid

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

    # codes_test.txt / codes_test.json: each line is an independent
    # {N}<hex> bitbuffer code fed to rtl_433 via -y, one code per expected
    # json line. Directories where the two counts don't match are skipped
    # (can't be aligned automatically) rather than guessed at.
    for codes_fn in find_codes_test(test_path):
        dirname = os.path.dirname(codes_fn)

        ignore_fn = os.path.join(dirname, "ignore")
        if os.path.isfile(ignore_fn):
            print("WARNING: Ignoring '%s'" % codes_fn)
            continue

        json_fn = os.path.join(dirname, "codes_test.json")
        if not os.path.isfile(json_fn):
            print("WARNING: Missing codes_test.json for '%s'" % codes_fn)
            continue

        codes = parse_codes_test(codes_fn)
        with open(json_fn, "r") as json_file:
            try:
                expected_lines = [json.loads(l) for l in json_file if l.strip()]
            except ValueError:
                print("ERROR: invalid json: '%s'" % json_fn)
                continue
        expected_lines = remove_fields(expected_lines, ignore_fields)

        if len(codes) != len(expected_lines):
            print("WARNING: %s has %d codes but %d expected json lines, skipping"
                  % (codes_fn, len(codes), len(expected_lines)))
            continue

        protocol, config = read_protocol(dirname, config_path)
        demod_args = read_demod_args(dirname)
        repeat = read_repeat_count(dirname)

        for i, (code, expected) in enumerate(zip(codes, expected_lines)):
            rtl433out, _err, exitcode = run_rtl433(test_data=code * repeat, protocol=protocol,
                                                   demod_args=demod_args, config=config,
                                                   rtl_433_cmd=rtl_433_cmd)
            if exitcode:
                print("ERROR: Exited with %d '%s' code #%d" % (exitcode, codes_fn, i))

            results, nb_invalid = parse_results(rtl433out, ignore_fields, expected_lines, false_positives)
            nb_fail += nb_invalid

            if len(results) != 1:
                nb_fail += 1
                print("## Fail with '%s' code #%d: expected 1 output line, got %d"
                      % (codes_fn, i, len(results)))
                print(" code: %s" % code)
                print(" Expected: " + str(expected))
                print("  But got: " + str(results))
                continue

            diff = DeepDiff(expected, results[0])
            if diff:
                nb_fail += 1
                print("## Fail with '%s' code #%d:" % (codes_fn, i))
                for error, details in diff.items():
                    print(" %s" % error)
                    for detail in details:
                        print("  * %s" % detail)
                print(" Expected: " + str(expected))
                print("  But got: " + str(results[0]))
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
