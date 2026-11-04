# Excelvan Wireless Weather Station 433MHz (transmitter model WH2A)

Here is a sample of rtl_433 signal recordings from the transmitter model WH2 of the Excelvan Wireless Weather Station. The transmitter provides temperature and humidity.

Link to [Wireless weather station webpage at vendor site](http://www.excelvan.com/product-g_93.html)

Note, readings from day 3 may be of higher quality: command issued rtl_433 -G -a -t to load all 102 device decoding protocols and very accurate observation of external temperature sensor readings versus captured files.

A pattern in the filesize of the samples is easily observable: every two files of 131072 bytes are followed by one file that doubles the filesize, 262144 bytes. This pattern occurs with the readings in any day 1, 2 or 3.

Excelvan wireless weather station is supposed/enforced to be the only piece of harware transmitting in 433MHz.

## Readings from day 1:

```bash
pi@raspberrypi:~/excelvan_signals $ ls -al
total 2312
drwxr-xr-x  2 pi pi   4096 Jul 11 00:13 .
drwxr-xr-x 27 pi pi   4096 Jul 11 00:11 ..
-rw-r--r--  1 pi pi 262144 Jul 11 00:04 g001_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:04 g002_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:05 g003_433.92M_250k.cu8
-rw-r--r--  1 pi pi 262144 Jul 11 00:06 g004_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:07 g005_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:08 g006_433.92M_250k.cu8
-rw-r--r--  1 pi pi 262144 Jul 11 00:08 g007_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:09 g008_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:10 g009_433.92M_250k.cu8
-rw-r--r--  1 pi pi 262144 Jul 11 00:11 g010_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:12 g011_433.92M_250k.cu8
-rw-r--r--  1 pi pi 131072 Jul 11 00:12 g012_433.92M_250k.cu8
-rw-r--r--  1 pi pi 262144 Jul 11 00:13 g013_433.92M_250k.cu8
```

In g001 Humidity 60% Temperature 30.7 Celsius

```
[00] {55} 01 6b 3d 99 87 dd a8
[01] {55} 01 6b 3d 99 87 dd a8
[02] {55} 01 6b 3d 99 87 dd a8
```

In  g004,g007,g010,g013 Humidity 60% Temperature 30.8 Celsius

```
[00] {55} 01 6b 3d 97 86 80 4a
[01] {55} 01 6b 3d 97 86 80 4a
[02] {55} 01 6b 3d 97 86 80 4a
```

Small size files, 131072 bytes, seem to be broken as per output "... Maximum number of rows reached. Message is likely truncated."

## Redings from day 2:

In g003 Humidity 61% Temperature 28.5 Celsius
```
[00] {55} 01 6b 3d c5 84 dc d2
[01] {55} 01 6b 3d c5 84 dc d2
[02] {58} 01 6b 3a 91 61 23 9a 40
```

In g006 Humidity 61% Temperature 28.6 Celsius
```
[00] {55} 01 6b 3d c3 84 86 7a
[01] {55} 01 6b 3d c3 84 86 7a
[02] {55} 01 6b 3d c3 84 86 7a
```

In g009 Humidity 61% Temperature 28.7 Celsius
```
[00] {55} 01 6b 3d c1 85 6f 60
[01] {55} 01 6b 3d c1 85 6f 60
[02] {55} 01 6b 3d c1 85 6f 60
```

In g012 Humidity 61% Temperature 28.7 Celsius
```
[00] {55} 01 6b 3d c1 85 6f 60
[01] {55} 01 6b 3d c1 85 6f 60
[02] {55} 01 6b 3d c1 85 6f 60
```

## Readings from day 3:

In g002 Humidity 60% Temperature 29.1 Celsius
```
[00] {55} 01 6b 3d b9 87 00 ec
[01] {55} 01 6b 3d b9 87 00 ec
[02] {55} 01 6b 3d b9 87 00 ec
```

In g005 Humidity 60% Temperature 29.1 Celsius
```
[00] {55} 01 6b 3d b9 87 00 ec
[01] {55} 01 6b 3d b9 87 00 ec
[02] {55} 01 6b 3d b9 87 00 ec
```

In g008 Humidity 61% Temperature 29.2 Celsius
```
[00] {55} 01 6b 3d b7 84 3e 26
[01] {55} 01 6b 3d b7 84 3e 26
[02] {55} 01 6b 3d b7 84 3e 26
```
