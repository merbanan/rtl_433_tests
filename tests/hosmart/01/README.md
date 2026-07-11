# Hosmart HS002 rechargeable driveway alert

Captures from https://github.com/merbanan/rtl_433/issues/1689 and
https://github.com/merbanan/rtl_433_tests/pull/391 (originally posted by
@whiteduck22).

https://www.amazon.co.uk/Rechargable-Weatherproof-Driveway-Wireless-Detector-1-receiver-Sensor/dp/B07DSB5HYJ

Also sold as eMacros. Protocol reverse engineered by @sbalabanov (see the
issue): FSK PWM, inverted, 25-bit message with id/model_id/channel/
battery_ok fields:
`-X "n=Hosmart-HS002,m=FSK_PWM,s=416,l=1248,r=14240,g=1252,t=332,y=0,bits=25,invert,get=id:@0:{12},get=model_id:@12:{8},get=channel:@20:{4},get=battery_ok:@24:{1}:[0:1 1:0]"`
