The Sensor Systems Watchman Sonic, and Apollo Ultrasonic oil monitor, are 
basically the same device. They consist of an ultrasonic detector which 
measures the fuel level in the oil tank, and a receiver unit which displays
the reading inside the house.

The receiver uses a Si4320 FSK decoder chip, which is the same as the 
HopeRF RFM01 decoder module. The data are sent with a Manchester 
encoding, and framed. The frame starts with three half-bit periods of 
high and then three half-bit periods of low frequency, and the final 
data bit is extended for a further two half-bit periods at the same 
frequency as an end-of-frame marker.

The Si4320 can be used at various frequencies; in the case of this device
it is tuned to 433.9MHz with a bandwidth of 67kHz.

In this directory are 21 captured samples. By converting them to FM
(rtl_433 -m 2 -r gfile001.data -t fm001.data) and then using the
proof-of-concept decoder hack also included in this directory, we get
the following data:

gfile001.data:
At 3.562625: 28 c7 48 0f 81 44 50  (crc ok fb)
    Unit ID: 0x28c7480f flags 0x8144 rebinding countdown 0
At 5.044458: 28 c7 48 0f 81 44 51  (crc ok a5)
    Unit ID: 0x28c7480f flags 0x8144 rebinding countdown 1

gfile002.data:
At 2.314625: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile003.data:
At 2.314292: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile004.data:
At 2.314042: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile005.data:
At 2.313792: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile006.data:
At 2.313792: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile007.data:
At 2.313792: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile008.data:
At 2.314000: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile009.data:
At 2.314250: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile010.data:
At 2.313875: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile011.data:
At 2.314125: 28 c7 48 0f 80 44 3a  (crc ok 4b)
    Unit ID: 0x28c7480f flags 0x8044 height 58

gfile012.data:
At 2.313958: 28 c7 48 0f 80 44 45  (crc ok f2)
    Unit ID: 0x28c7480f flags 0x8044 height 69

gfile013.data:
At 2.314000: 28 c7 48 0f 80 44 40  (crc ok cd)
    Unit ID: 0x28c7480f flags 0x8044 height 64

gfile014.data:
At 2.314042: 28 c7 48 0f 80 44 31  (crc ok 6b)
    Unit ID: 0x28c7480f flags 0x8044 height 49

gfile015.data:
At 2.313875: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile016.data:
At 2.314042: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile017.data:
At 2.314667: 28 c7 48 0f 80 44 2e  (crc ok b7)
    Unit ID: 0x28c7480f flags 0x8044 height 46

gfile018.data:
At 2.314208: 28 c7 48 0f 80 44 3f  (crc ok 74)
    Unit ID: 0x28c7480f flags 0x8044 height 63

gfile019.data:
At 2.313875: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile020.data:
At 2.314292: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile021.data:
At 2.273792: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0
At 5.044667: 28 c7 48 0f 80 44 00  (crc ok 8b)
    Unit ID: 0x28c7480f flags 0x8044 height 0

gfile022.data:
At 2.509125: 28 4e cc 8c 80 54 3b  (crc ok 00)
    Unit ID: 0x284ecc8c flags 0x8054 height 59

gfile023.data:
At 2.520750: 28 4e cc 8c 80 58 3c  (crc ok ce)
    Unit ID: 0x284ecc8c flags 0x8058 height 60

gfile024.data:
At 2.694833: 28 4e cc 8c 80 54 3c  (crc ok 83)
    Unit ID: 0x284ecc8c flags 0x8054 height 60

