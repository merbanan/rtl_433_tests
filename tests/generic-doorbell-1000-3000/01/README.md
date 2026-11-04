# Generic 433 MHz wireless doorbell button

Capture from https://github.com/merbanan/rtl_433/issues/1706 (originally
posted by @Ocean-85).

https://www.amazon.de/dp/B01M1KB4UM -- no brand/model name could be
confirmed from the listing.

OOK PWM, 1000 us short pulse, 3000 us long pulse, 2000 us gap, ~4000 us
sync bit, per @zuckschwerdt's flex analysis in the issue
(`-X 'n=door,m=OOK_PWM,s=1000,l=3000,g=2000,r=10000,match=689b,bits>=16'`).
Only one button was ever captured, and the code never varied across
repeats, so no id/data field split could be confirmed; the
`../../../conf/generic-doorbell-1000-3000.conf` decoder matches the fixed
code directly and just reports an event count.

A second, unrelated doorbell (different timing: 228/660/742 us) was also
posted later in the same issue thread by @okridgway, but isn't
represented here.
