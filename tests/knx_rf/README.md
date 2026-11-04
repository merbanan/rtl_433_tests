# KNX RF

**File generation:**
```
rtl_433 -f 868.32M -s 1024k -S all
```
Remote button for specific light 'ON' pressed several times.
Receiving unit is 'Hager TR210'

## KNX RF technical

There are several variations of KNX RF, this system is from 2005 - and it should be using the oldest spec.

## Signal data

- Frequency: **868.3MHz**
- Modulation: **FSK Manchester**
- Baud rate: Assumed to be **16.384kbps**

## Data information

Wireless M-BUS is compatible with KNX RF, decoding with the m_bus (Mode S) module not successful. (with 16.4kbps modification)
Also no success with 32.768kbps.
More information: https://weinzierl.de/images/download/references/KnxRf_WirelessConf_2006_10_18.pdf
Only security to distinguish from neighboring installations is a 6 byte domain address.

The recordings should be a unicast transmission (with possible reply from receiver?)

