# Vion C6500 wind sensor — set 01

Recorded with an RTL2832U/R820T dongle at 433.92 MHz, 1024k sample rate
(`rtl_433 -f 433.92M -s 1024k -S all`). The sensor sits at about +290 kHz from the
center frequency (~434.21 MHz).

## Timing

    Pulse width distribution:
     [ 0] count:  103,  width:  277 us [224;280]
     [ 1] count:   65,  width:  142 us [139;146]
     [ 2] count:    4,  width:  414 us [413;415]
    Gap width distribution:
     [ 0] count:   64,  width:  131 us [129;134]
     [ 1] count:  102,  width:  267 us [265;271]
     [ 2] count:    5,  width:  404 us [403;405]
    Frequency offsets [F1, F2]:   19812,      0  (+309.6 kHz, +0.0 kHz)
    Guessing modulation: Pulse Width Modulation with sync/delimiter

Each pulse is followed by a gap of the same width (142+131 us or 277+267 us), so the
gaps carry no extra information. A message is a 5-bit preamble row, then the 82-bit
payload sent twice (the second copy decodes as 81 bits).

Flex decoder (raw bits):

    -X 'n=Vion-C6500,m=OOK_PWM,s=142,l=278,r=1000,g=600,t=60,y=414,bits=82'

## Message layout

Bytes are sent LSB first. After reflecting each byte:

    ID:16h AVG:8d GUST:8d WIND:8d AVG_DIR:8d GUST_DIR:8d DIR:8d FLAGS:8b ?:8h ?:2b

| Field    | Byte | Meaning                                                    |
|----------|------|------------------------------------------------------------|
| ID       | 0-1  | `951c` (raw `a938`), constant on this unit                 |
| AVG      | 2    | average wind speed, 0.5 km/h                               |
| GUST     | 3    | gust speed (max over a sliding window), 0.5 km/h           |
| WIND     | 4    | wind speed, 0.5 km/h                                       |
| AVG_DIR  | 5    | average direction, degrees, low 8 bits                     |
| GUST_DIR | 6    | gust direction, degrees, low 8 bits                        |
| DIR      | 7    | wind direction, degrees, low 8 bits                        |
| FLAGS    | 8    | bit 1: DIR +256, bit 2: GUST_DIR +256, bit 3: AVG_DIR +256 (bit 0 = MSB of the reflected byte) |
| ?        | 8-10 | remaining bits unknown (checksum? battery?)                |

The last bit of byte 9 (raw bit 79) toggles between the two copies of a message.

The decoding was validated against the console display on 24 messages, in all three
display modes, including directions above 255 degrees for each of the three directions.

## Samples

Codes are raw (before reflect). Values decoded with `conf/Vion-C6500.conf`.

| File                     | Raw code (82 bits)          | Wind km/h | Dir ° | Gust km/h | Gust dir ° | Avg km/h | Avg dir ° |
|--------------------------|-----------------------------|-----------|-------|-----------|------------|----------|-----------|
| g002_433.92M_1024k.cu8   | `{82}a9383044b095527410a88` | 6.5       | 46    | 17.0      | 74         | 6.0      | 169       |
| g005_433.92M_1024k.cu8   | `{82}a938305868c222d812e88` | 11.0      | 283   | 13.0      | 68         | 6.0      | 67        |
| g012_433.92M_1024k.cu8   | `{82}a938e018a8b2189614d88` | 10.5      | 105   | 12.0      | 280        | 3.5      | 77        |
| g017_433.92M_1024k.cu8   | `{82}a938e068d027d89514908` | 5.5       | 169   | 11.0      | 283        | 3.5      | 228       |
| g029_433.92M_1024k.cu8   | `{82}a93810180032300a1e888` | 0.0       | 336   | 12.0      | 268        | 4.0      | 332       |

These samples were not recorded at the same time as console readings; the values come
from the validated layout above.

## Reception note

Close to the sensor the signal is very strong. With automatic gain the R820T saturates
and each message shows up as a single 78 ms pulse; any fixed gain works (tested 12.5 to 49.6 dB).
