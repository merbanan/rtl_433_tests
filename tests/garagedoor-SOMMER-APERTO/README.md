# SOMMER garage door

Manufacturer: SOMMER
Model: APERTO 868 L

These are signals from a garage door opener. They are measured at 868.683 MHz. The files are definitely FSK, as can be seen when opened in Audacity.

## First attempt at decoding

`rtl_433 -c remote-decoder.conf -M newmodel -A -v -G -r gfile.cu8`

remote.conf

```
decoder {
  name=remote,
  modulation=FSK_PWM,
  short=392,
  long=780,
  reset=15900,
}
```

Note that version `18.12-176-g4256075 branch master at 201903312227` will not detect the start of the cu8 files correctly. The front of the files needs to be chopped off (using e.g. Audacity) to decode them to something useful.

```
time      : @0.004100s
model     : remote       count     : 1             num_rows  : 1             rows      : 
len       : 219          data      : fff821cd8279f2040843ffe0873609e7c810211fff821cd8279f204
codes     : {219}fff821cd8279f2040843ffe0873609e7c810211fff821cd8279f204
```

It seems like the codes always start with fff, but I'm not sure about the rest.
