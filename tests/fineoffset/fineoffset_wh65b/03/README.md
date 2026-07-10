# Fine Offset WH65B

`g200_915M_1000k.cu8` is from https://github.com/merbanan/rtl_433/issues/1220
(posted by @lachesis in 2024), part of the long-running WH24 vs WH65B
misclassification issue. The reporter found the *exact same* physical
transmission decoded correctly as WH65B when replayed from a saved file
(as here) but sometimes decoded as WH24 during live capture -- see the
issue for the fix (a `-R 78:wh65b` override to force the model when the
automatic heuristic gets it wrong).
