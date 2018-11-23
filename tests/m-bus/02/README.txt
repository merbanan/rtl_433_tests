https://github.com/merbanan/rtl_433/issues/617#issuecomment-441168564

raw file from rtl_sdr cmd:
```
rtl_sdr -f 868900000 -s 1600000 - > meters_file_from_rtl_sdr_F86890000_S1600000.raw
```

rtl_wmbus out file from raw file cmd:
```
cat meters_file_from_rtl_sdr_F86890000_S1600000.raw | rtl_wmbus > meters_decoded_from_raw_file_by_rtl_wmbus.txt
```

my analysis file meters_decoded_from_raw_file_by_rtl_wmbus.txt:
```
meters_my_out.txt
```