/* Primitive Si4320/Watchman decoder.
 * © 2015 David Woodhouse <dwmw2@infradead.org>
 * Released under GNU General Public License v2 or later.
 *
 * Usage:
 * rtl_fm -f 433900000 -s 48000 -l 160 -r 24000 -E deemp | watchman-demod
 */

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <time.h>
#ifndef SFREQ
#define SFREQ 1000000
#endif
int debug = 0;
int infd = 0; /* stdin */
/*
 * 1Wire CRC8 as described at
 * https://www.maximintegrated.com/en/app-notes/index.mvp/id/27
 */
unsigned char crc8tab[] = {
	0x00, 0x5e, 0xbc, 0xe2, 0x61, 0x3f, 0xdd, 0x83,
	0xc2, 0x9c, 0x7e, 0x20, 0xa3, 0xfd, 0x1f, 0x41,
	0x9d, 0xc3, 0x21, 0x7f, 0xfc, 0xa2, 0x40, 0x1e,
	0x5f, 0x01, 0xe3, 0xbd, 0x3e, 0x60, 0x82, 0xdc,
	0x23, 0x7d, 0x9f, 0xc1, 0x42, 0x1c, 0xfe, 0xa0,
	0xe1, 0xbf, 0x5d, 0x03, 0x80, 0xde, 0x3c, 0x62,
	0xbe, 0xe0, 0x02, 0x5c, 0xdf, 0x81, 0x63, 0x3d,
	0x7c, 0x22, 0xc0, 0x9e, 0x1d, 0x43, 0xa1, 0xff,
	0x46, 0x18, 0xfa, 0xa4, 0x27, 0x79, 0x9b, 0xc5,
	0x84, 0xda, 0x38, 0x66, 0xe5, 0xbb, 0x59, 0x07,
	0xdb, 0x85, 0x67, 0x39, 0xba, 0xe4, 0x06, 0x58,
	0x19, 0x47, 0xa5, 0xfb, 0x78, 0x26, 0xc4, 0x9a,
	0x65, 0x3b, 0xd9, 0x87, 0x04, 0x5a, 0xb8, 0xe6,
	0xa7, 0xf9, 0x1b, 0x45, 0xc6, 0x98, 0x7a, 0x24,
	0xf8, 0xa6, 0x44, 0x1a, 0x99, 0xc7, 0x25, 0x7b,
	0x3a, 0x64, 0x86, 0xd8, 0x5b, 0x05, 0xe7, 0xb9,
	0x8c, 0xd2, 0x30, 0x6e, 0xed, 0xb3, 0x51, 0x0f,
	0x4e, 0x10, 0xf2, 0xac, 0x2f, 0x71, 0x93, 0xcd,
	0x11, 0x4f, 0xad, 0xf3, 0x70, 0x2e, 0xcc, 0x92,
	0xd3, 0x8d, 0x6f, 0x31, 0xb2, 0xec, 0x0e, 0x50,
	0xaf, 0xf1, 0x13, 0x4d, 0xce, 0x90, 0x72, 0x2c,
	0x6d, 0x33, 0xd1, 0x8f, 0x0c, 0x52, 0xb0, 0xee,
	0x32, 0x6c, 0x8e, 0xd0, 0x53, 0x0d, 0xef, 0xb1,
	0xf0, 0xae, 0x4c, 0x12, 0x91, 0xcf, 0x2d, 0x73,
	0xca, 0x94, 0x76, 0x28, 0xab, 0xf5, 0x17, 0x49,
	0x08, 0x56, 0xb4, 0xea, 0x69, 0x37, 0xd5, 0x8b,
	0x57, 0x09, 0xeb, 0xb5, 0x36, 0x68, 0x8a, 0xd4,
	0x95, 0xcb, 0x29, 0x77, 0xf4, 0xaa, 0x48, 0x16,
	0xe9, 0xb7, 0x55, 0x0b, 0x88, 0xd6, 0x34, 0x6a,
	0x2b, 0x75, 0x97, 0xc9, 0x4a, 0x14, 0xf6, 0xa8,
	0x74, 0x2a, 0xc8, 0x96, 0x15, 0x4b, 0xa9, 0xf7,
	0xb6, 0xe8, 0x0a, 0x54, 0xd7, 0x89, 0x6b, 0x35,
};

unsigned char w1crc(unsigned char *addr, int len)
{
	unsigned char crc = 0;
	int i;

	for (i=0; i < len; i++)
		crc = crc8tab[crc ^ addr[i]];
	return crc;
}

int framepos = -2;
int framestart;
/* If badly tuned we sometimes get inverted input */
int invertframe;
unsigned char frame[8];

#define SET_BIT(pos, level) do { if (level == invertframe) frame[(pos)/8] |= (1<<(7-((pos)&7)));} while(0)
#define SMULT 967.5

void transition(int level, int samples, int halfbits)
{
	//	printf("%s %s %f %d\n", __func__, level?"high":"low", (float)samples/SFREQ, halfbits);
	if (framepos == -2) {
		if (halfbits >= 3) {
			if (debug)
				printf("Frame started (%s). %d high HB ends at %f\n",  level? "normal":"inverted", halfbits, (float)samples/SFREQ);
			invertframe = !level;
			framestart = samples;
			framepos = -1;
			memset(frame, 0, sizeof(frame));
		}
		return;
	} else if (framepos == -1) {
		if (level == invertframe) {
			if (halfbits == 3) {
				if (debug)
					printf("Low frame preamble ends at %f (%f)\n", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ);
				framepos = 0;
			} else if (halfbits == 4) {
				framepos = 1;
				if (debug)
					printf("Low frame preamble ends at %f (%f) with 1 hb\n", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ);
				frame[0] = 0;
			} else {
				if (debug)
					printf("Low frame preamble not found at %f (%f) (%d hb)\n", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ, halfbits);
				framepos = -2;
			}
		} else {
			if (debug)
				printf("Low frame preamble not found at %f (%f) (high for %d hb?!)\n", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ, halfbits);
			framepos = -2;
		}
	} else if (halfbits > 2) {
		if (framepos == 127 && halfbits == 3) {
			uint8_t crc = w1crc(frame, 7);
			int i;
			if (infd)
				printf("At %f:", (float)samples/SFREQ);
			else {
				time_t now = time(NULL);
				char timebuf[80];
				strftime(timebuf, sizeof(timebuf), "%F %T", gmtime(&now));
				printf("At %s: ", timebuf);
			}
			for (i=0;i<7;i++)
				printf(" %02x", frame[i]);
			if (frame[7] == crc)
				printf("  (crc ok %02x)\n", crc);
			else
				printf("  (CRC FAIL: %02x != %02x)\n", frame[7], crc);
			if (frame[4] & 1)
				printf("    Unit ID: 0x%02x%02x%02x%02x flags 0x%02x%02x rebinding countdown %d\n",
				       frame[0], frame[1], frame[2], frame[3], frame[4], frame[5] & 0xfc,
				       frame[6] & 15);
			else
				printf("    Unit ID: 0x%02x%02x%02x%02x flags 0x%02x%02x height %d\n",
				       frame[0], frame[1], frame[2], frame[3], frame[4], frame[5] & 0xfc,
				       (((int)frame[5] & 3) << 8) + frame[6]);
		}
		framepos = -2;
	} else if (halfbits == 1) {
		framepos++;
		if (debug)
			printf("Transition %s at %f (%f) (fp %d) after 1 hb\n", level?"high":"low ", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ, framepos);
		if (framepos > 127) {
			printf("Frame overrun at %f (%f) (fp %d)!\n", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ, framepos);
			framepos = -2;
		} else if (framepos & 1)
			SET_BIT(framepos/2, level);
	} else if (halfbits == 2) {
		framepos += 2;
		if (debug)
			printf("Transition %s at %f (%f) (fp %d) after 2 hb\n", level?"high":"low ", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ, framepos);
		if (framepos > 127) {
			printf("Frame overrun at %f (%f) (fp %d)!\n", (float)samples/SFREQ, (float)(samples-framestart)*SMULT/SFREQ, framepos);
			framepos = -2;
		} else
			SET_BIT(framepos/2, level);
	} else {
		/* This can never happen but be defensive */
		framepos = -2;
	}
}

#define SAMPLES(x) (x * (SFREQ/24000))

int main(int argc, char **argv)
{
	unsigned char b[2];
	int hi_bits = 0, lo_bits = 0;
	int s = 0, this = 0;
	int laststable = 0;
	int prev[8] = { 0,0,0,0,0, 0, 0, 0 };

	if (argc > 1) {
		if (!strcmp(argv[1], "-d")) {
			debug=1;
			argv++;
			argc--;
		}
	}
	if (argc == 2) {
		infd = open(argv[1], O_RDONLY);
		if (infd == -1) {
			perror("open sample file");
			exit(1);
		}
	} else if (argc > 2) {
		fprintf(stderr, "Usage: watchman-demod [-d] [filename]\n"
			"   or:    rtl_fm -f 433900000 -s 48000 -l 160 -r 24000 | watchman-demod\n");
	}

	while (read(infd, b, 2) == 2) {
		int thresh = -2200;
		s++;
		prev[0] = prev[1];
		prev[1] = prev[2];
		prev[2] = prev[3];
		prev[3] = prev[4];
		prev[4] = prev[6];
		prev[5] = prev[6];
		prev[6] = prev[7];
		prev[7] = (int16_t)(b[0] + (b[1] << 8));
		if (lo_bits && prev[7] > 4000)
			prev[7] = prev[0];
		if (hi_bits && framepos != -2 && prev[7] < -5000)
			prev[7] = prev[0];
		this = (prev[0] + prev[1] + prev[2] + prev[3] + prev[4] + prev[5] + prev[6] + prev[7]) / 4;
		//		printf("%d: (%f): %d (%d,%d)\n", s, (float)s/SFREQ, this, (int16_t)(b[0] + (b[1] << 8)), prev[7]);

		if (hi_bits)
			thresh = -1650;
		else thresh = -820;
		if (this > thresh) {
			hi_bits++;
			if (!laststable && hi_bits >= SAMPLES(18))
				laststable = s;
			if (lo_bits >= SAMPLES(18)) {
				transition(0, s, (lo_bits + SAMPLES(10)) / SAMPLES(25));
				laststable = s;
			} else if (lo_bits && framepos != -2 && s - laststable > SAMPLES(5)) {
				if (debug)
					printf("Unstable reset at %f\n", (float)s/SFREQ);
				framepos = -2;
			}
			lo_bits = 0;
		} else {
			lo_bits++;
			if (!laststable && lo_bits >= SAMPLES(18))
				laststable = s;
			if (hi_bits >= SAMPLES(18)) {
				transition(1, s, (hi_bits + SAMPLES(10)) / SAMPLES(25));
				laststable = s;
			} else if (hi_bits && framepos != -2 && s - laststable > SAMPLES(5)) {
				if (debug)
					printf("Unstable reset at %f\n", (float)s/SFREQ);
				framepos = -2;
			}
			hi_bits = 0;
		}
		//		printf("%d: (%f): %d h %d l %d ls %d\n", s, (float)s/SFREQ, this, hi_bits, lo_bits, laststable);
	}
}
