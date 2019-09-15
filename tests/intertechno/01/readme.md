# Intertechno ITT-1500 remote

Test signals off an intertechno ITT-1500 remote sold together with ITR-1500 remote controlled outlets.

PPM Modulation: Pulse 220µs, short gap 350µs, long gap 1400µs
Encoding: Sync pulse, long gap, 64 bit data, repeat 5x

Product page: http://intertechno.at/front/produkte/empfanger/zwischenstecker/it-1500/
Picture: http://intertechno.at/wp-content/uploads/2015/07/IT-1500-K.jpg

Output of `-a -r 1on.cu8`:

```
[00] {65} b4 b4 aa ac d4 d5 4b 2a 80
[01] {65} b4 b4 aa ac d4 d5 4b 2a 80
[02] {65} b4 b4 aa ac d4 d5 4b 2a 80
[03] {65} b4 b4 aa ac d4 d5 4b 2a 80
[04] {65} b4 b4 aa ac d4 d5 4b 2a 80
```
