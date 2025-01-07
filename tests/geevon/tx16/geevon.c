/** @file
    Geevon TX16-3 Remote Outdoor Sensor with LCD Display

    Contributed by Matt Falcon (with significant contribution from ChatGPT)

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
*/

#include "decoder.h"

/**
Decode Geevon TX16-3.
The following packet represents:
- channel 1
- battery OK
- temperature of 62.6 Fahrenheit or 17 Celsius
- 43% relative humidity.

Byte 0   Byte 1   Byte 2   Byte 3   Byte 4   Byte 5   Byte 6   Byte 7   Byte 8   Byte 9
xxxxxxxx BxCCxxxx TTTTTTTT TTTT0000 HHHHHHHH IIIIIIII IIIIIIII IIIIIIII CCCCCCCC xxxxxxxx
   87       00       29       e0       2b       aa       55       aa       e8       40

x - Ignored
B - Battery status (0 = good, 1 = low battery)
C - Channel (0, 1, 2 as channels 1, 2, 3)
T - Temperature - represented as ((degrees C * 10) + 500)
H - Relative humidity - represented as percentage %
I - Integrity check - 3 bytes are always 0xAA 0x55 0xAA
C - Checksum (unknown algorithm)
*/

static int geevon_callback(r_device *decoder, bitbuffer_t *bitbuffer)
{
    data_t *data;
    uint8_t *b;
    int battery_low;
    int channel;
    int r;
    float temperature_c;
    float temperature_f;
    float humidity;
    int integrity_check;
    int checksum;

    // not entirely sure why "-a 4" always returns a correct bitbuffer, but not how to implement its findings
    //   when decoded in triq.org or implemented as such as PWM, it ends up inverting all the bits.
    //   sloppy hack fix, thus:
    bitbuffer_invert(bitbuffer);

    // in lieu of knowing the checksum algorithm, simply find the most common row
    r = bitbuffer_find_repeated_row(bitbuffer, bitbuffer->num_rows > 5 ? 5 : bitbuffer->num_rows, 64);
    if (r < 0) {
        r = bitbuffer_find_repeated_row(bitbuffer, 2, 64); // 65
    }
    if (r < 0) {
        return DECODE_ABORT_LENGTH;
    }

    // work with the best/most repeated capture
    b = bitbuffer->bb[r];

    // Check if the packet has the correct number of bits
    if (bitbuffer->bits_per_row[r] != 73){
        return DECODE_ABORT_LENGTH;
    }

    // Check if the integrity check bytes are correct
    if (b[5] != 0xAA || b[6] != 0x55 || b[7] != 0xAA) {
        return DECODE_FAIL_MIC;
    }

    // Extract the data from the packet
    battery_low = (b[1] & 0x80)?0:1; // battery good: 1; bad: 0
    channel = ((b[1] & 0x30) >> 4) + 1; // channel: 1, 2, 3
    temperature_c = ((float)((b[2] << 4) | b[3] >> 4)  - 500) / 10.0; // temperature is ((degrees c + 500) * 10)
    humidity = (float)b[4];
    integrity_check = (b[5] << 16) | (b[6] << 8) | b[7]; // always AA 55 AA
    checksum = b[8];

    // Convert to Fahrenheit
    temperature_f = temperature_c * 9.0 / 5.0 + 32.0;

/*
    // Print the decoded data
    bitbuffer_print(bitbuffer);
    fprintf(stdout, "Battery Good: %d\n", battery_low);
    fprintf(stdout, "Channel: %d\n", channel);
    fprintf(stdout, "Temperature: %.1f C / %.1f F\n", temperature_c, temperature_f);
    fprintf(stdout, "Humidity: %.1f%%\n", humidity);
    fprintf(stdout, "Integrity check: 0x%06X\n", integrity_check);
    fprintf(stdout, "Checksum: 0x%02X\n", checksum);
*/

    // Store the decoded data in a data_t structure
    data = data_make(
        /* clang-format off */
        "model",           "",                DATA_STRING,                        "Geevon TX16-3",
        "battery",         "Battery Good",    DATA_INT,                           battery_low,
        "channel",         "Channel",         DATA_INT,                           channel,
        "temperature_C",   "Temperature",     DATA_FORMAT, "%.1f C", DATA_DOUBLE, temperature_c,
        "humidity",        "Humidity",        DATA_FORMAT, "%.1f%%", DATA_DOUBLE, humidity,
        NULL);
        /* clang-format on */

    decoder_output_data(decoder, data);

    return 1;
}

static char *output_fields[] = {
    "model",
    "battery",
    "channel",
    "temperature_C",
    "temperature_F",
    "humidity",
    "integrity_check",
    "checksum",
    NULL
};

r_device geevon = {
    .name           = "Geevon TX16-3",
    .modulation     = OOK_PULSE_PWM,
    .short_width    = 252,
    .long_width     = 476,
    .sync_width     = 728,  // sync pulse is 728 us + 728 us gap
    .gap_limit      = 625,  // long gap (with short pulse) is ~472 us, sync gap is ~728 us
    .reset_limit    = 1700, // maximum gap is 1250 us (long gap + longer sync gap on last repeat)
    .decode_fn      = &geevon_callback,
    .fields         = output_fields
};
