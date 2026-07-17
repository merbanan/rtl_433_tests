# Cotech FT0203 / 18-3676 anemometer

See https://github.com/merbanan/rtl_433/issues/2569 -- a 27-comment,
multi-year thread where zuckschwerdt, klohner, ProfBoc75 and
GreatAlbatross collaboratively reverse-engineered the CRC-8 (poly 0x31,
init 0xc0) and byte layout, but no working decoder was ever committed.

No real IQ capture exists for this device (the one attached `.cu8` was
confirmed by ProfBoc75 to be a different, unrelated signal), so the
decoder ships `.disabled = 1`.

`codes_test.txt`/`codes_test.json` hold all 50 unique hex codes
transcribed across the thread. The 15 with an annotated reading
independently verify direction (all 8 compass points) and average/gust
wind speed (scale x0.1) against the values the issue reporters observed
on their display; the rest are checksum-only or confirm the id/battery
change across a battery replacement (id 1251 -> 1261, battery_ok 0 -> 1).
The gust/avg MSB bits are inferred by analogy with the related
Cotech-367959 protocol and were never observed set in any sample from
the thread.
