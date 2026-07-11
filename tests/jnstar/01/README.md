# JNStar / JNWR driveway infrared beam alarm

Captures from https://github.com/merbanan/rtl_433/issues/1689 and
https://github.com/merbanan/rtl_433_tests/pull/391 (originally posted by
@whiteduck22).

https://www.ebay.co.uk/itm/Solar-Dual-Beam-Driveway-Alarm-20m-Wireless-Infrared-Dual-Beams-JNStar-JNWR-6/303120336342

Fixed 25-bit code, OOK PWM, per @zuckschwerdt's flex suggestion
(`-X 'n=jnstar,m=OOK_PWM,s=180,l=390,r=4000,g=500'`). Only one unit was
tested, so no id/data split within the 25 bits could be confirmed; the
`../../../conf/JNStar-Beam.conf` decoder matches that unit's fixed code
directly and just reports an event count.
