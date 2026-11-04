Noisy watchman trace in gfile023.data needs signficant smoothing in order to
decode it. See fskdemod.c for a hack which demonstrates the problems.

It decodes if we apply two kinds of smoothing to the FM signal:
 - Eliminate noise by operating on the mean of 8 (FM) samples at a time
 - Tweak the 0/1 bit threshold depending on the current detected level

rtl_433 -r gfile023.data -m 2 -t gfile023.fm && ./fskdemod gfile023.fm

....

gfile455 looks like a failure of the auto-level detection, and starts in
the middle of a packet.

gfile668 has an emonTx packet *and* a watchman packet in it.
