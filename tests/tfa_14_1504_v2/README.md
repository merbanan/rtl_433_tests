# Tests for TFA Dostmann 14.1504.V2 (30.3254.01) Radio-controlled grill and meat thermometer
CAUTION: Do not confuse with TFA Dostmann 14.1504 (30.3201) which had a completely different protocol => [71] Maverick ET-732/733 BBQ Sensor

On the product page, select style/variant: "from/ab 02/2022"

Product page: https://www.tfa-dostmann.de/en/product/wireless-bbq-meat-thermometer-kuechen-chef-14-1504/

Datasheet   : https://com-tradebyte-core-tbone-media-live.s3.eu-central-1.amazonaws.com/media/1768/26554-627bb5df19d9a.pdf

Flexible decoder example:

    rtl_433 -R 0 -X 'n=TFA-141504v2,m=FSK_PCM,s=360,l=360,r=4096,preamble={24}aaaa5c'

Captured samples and decoded output:
* See the .cu8 and .json files

Reverse engineering of the 16-bit LFSR integrity check:
* See "samples.txt" and run revdgst16 on it (last 4 nibbles are the checksum): https://github.com/triq-org/revdgst/
