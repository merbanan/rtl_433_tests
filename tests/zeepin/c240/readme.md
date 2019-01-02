# Zeepin TPMS - C240

Each sensor sends data every 5min.


## Decoding

For now best decoding seems to be: 
```
$ rtl_433 -s 1024k -S all -X 'n=zeepin,m=OOK_MC_ZEROBIT,s=50,l=50,r=1000,invert'
```
i.e. OOK with manchster encoding (invert is not sure)



## Records session 01

Very first tests, sample rate at 1024k seems needed.


## Records session 02

- Only one sensor (other have battery removed)
- sensor plugged on a bike tire with only 0.1bar (2psi) (this is not an error)

g010_433.92M_1024k.cu8
time    : 2018-12-28 23:00:47
data    : 11°C 0.1bar 
{85}f80005656491b84422dd60
{80}ffffacac923708845bac

g059_433.92M_1024k.cu8
time      : 2018-12-28 23:35:39
data     : 19°C 0.1bar
{84}f0000c4c4814ff09c43c4
{80}ffffc4c4814ff09c43c4

g073_433.92M_1024k.cu8
time      : 2018-12-28 23:40:37
data      : 19°C 0.1bar
{84}f0000c4c4814ff09c43c4
{80}ffffc4c4814ff09c43c4

g086_433.92M_1024k.cu8
time      : 2018-12-28 23:50:34
data      : 20°C 0.1bar
{81}80005e5e4523fc4a25de0
{80}ffffbcbc8a47f8944bbc

g100_433.92M_1024k.cu8
time      : 2018-12-28 23:55:33
data      : 20°C 0.1bar
{89}ff80005e5e4523fc4a25de0
{80}ffffbcbc8a47f8944bbc

g113_433.92M_1024k.cu8
data      : 20°C 0.1bar
time      : 2018-12-29 00:00:31
{94}fffc0002f2f2291fe2512ef0
{80}ffffbcbc8a47f8944bbc

g152_433.92M_1024k.cu8
time      : 2018-12-29 00:10:29
data      :  9°C 0.1bar
{82}c000282826cac51e19a80
{80}ffffa0a09b2b147866a0

g177_433.92M_1024k.cu8
time      : 2018-12-29 00:20:28
data      :  3°C 0.1bar
{86}fc0003838155af52e09b80
{80}ffffe0e0556bd4b826e0

