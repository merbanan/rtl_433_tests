"""Derive rtl_433 frequency/sample-rate arguments for a sample file.

Frequency and sample rate are read from the sample filename, e.g.
``name_915M_1000k.cu8`` -> 915 MHz, 1000 kS/s.  Passing the real frequency
matters because rtl_433's FSK pulse-detector auto-selection switches to the
min/max slicer above 800 MHz (``FSK_PULSE_DETECTOR_LIMIT``); without ``-f`` a
file replay defaults to 433.92 MHz and always uses the classic slicer, so the
min/max code path was never exercised by the test suite.

Per-directory ``frequency`` / ``samplerate`` override files take precedence
over the filename when present (one integer in Hz on the first line).
"""

import os
import re

# Match a trailing "_<num>M" / "_<num>k" token (followed by "_" or the
# extension dot), allowing a decimal part, e.g. _915M_, _303.3M_, _1000k.
_FREQ_RE = re.compile(r'_(\d+(?:\.\d+)?)M(?=[._])')
_RATE_RE = re.compile(r'_(\d+(?:\.\d+)?)k(?=[._])')

DEFAULT_SAMPLERATE = 250000


def parse_params(input_fn):
    """Return (frequency_hz, samplerate_hz) for a sample file.

    frequency is None when the filename carries no (non-zero) frequency, in
    which case rtl_433's default applies and the classic slicer is used.
    samplerate falls back to DEFAULT_SAMPLERATE.
    """
    base = os.path.basename(input_fn)
    directory = os.path.dirname(input_fn)

    freq = None
    found = _FREQ_RE.findall(base)
    if found:
        hz = round(float(found[-1]) * 1e6)
        if hz > 0:
            freq = hz

    rate = None
    found = _RATE_RE.findall(base)
    if found:
        rate = round(float(found[-1]) * 1e3)

    freq_fn = os.path.join(directory, "frequency")
    if os.path.isfile(freq_fn):
        with open(freq_fn) as fh:
            line = fh.readline().strip()
        if line:
            freq = int(line)

    rate_fn = os.path.join(directory, "samplerate")
    if os.path.isfile(rate_fn):
        with open(rate_fn) as fh:
            line = fh.readline().strip()
        if line:
            rate = int(line)

    if rate is None:
        rate = DEFAULT_SAMPLERATE
    return freq, rate


def rtl433_args(input_fn):
    """Build the ``-f``/``-s`` argument list for an rtl_433 invocation."""
    freq, rate = parse_params(input_fn)
    args = []
    if freq:
        args.extend(["-f", str(freq)])
    if rate:
        args.extend(["-s", str(rate)])
    return args
