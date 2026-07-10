# Fine Offset WH24 (mislabeled -- actually a WH65B)

See https://github.com/merbanan/rtl_433/issues/764 (where these samples
were originally collected) and
https://github.com/merbanan/rtl_433/issues/1220 (the long-running WH24 vs
WH65B misclassification issue these samples turned out to be an early
example of).

**Note: `g001.cu8`-`g011.cu8` are actually from a WH65B sensor array**
(part of an Ambient Weather WS-2902A), not a real WH24. WH24 and WH65B
send bit-identical payloads and only differ in overall packet length, so
telling them apart from preamble/postamble bit timing alone is unreliable
-- these samples happen to land on the WH24 side of that heuristic.

As of the fix for #1220, the decoder (protocol 78, "Fine Offset
Electronics, WH25, WH32, ... WH24, WH65B, ...") supports forcing the
correct model when the automatic heuristic gets it wrong:

    rtl_433 -r g001.cu8 -R 78:wh65b

`codes_test.txt`/`codes_test.json` contain the WH24 and WH65B example
frames from the decoder's own doc-comment (`src/devices/fineoffset.c`),
useful as a quick regression check for both the default heuristic and the
`wh24`/`wh65b` override.
