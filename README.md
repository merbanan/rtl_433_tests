# rtl_433 test samples

rtl_433_tests contains the test suite for rtl_433

This repository contains lots of signal recordings that are supported by rtl_433.

The regtest system is not developed yet, but accepting signal recordings.

## Installation instructions

Clone this repository to the root of rtl_433

## Running

Enter the directory and run `make test`. The output will tell if the tests failed or not.

## Contributing

Run rtl_433 with `rtl_433 -S unknown` and wait for you signal to be detected. When it is detected
note what gfile name it has. This file can now be run through rtl_433 offline:

    $ rtl_433 -r g001.cu8

Look at the `-A` analyze mode output and include a timing description if you like.
You can also include a flex decoder (`-X ...`), don't include raw analyzer output.

## Organization

Add signals by creating directories and then add the sample files.
We need to watch the repo size, add only about 5 interesting sample files.
If you have more interesting samples (e.g. to recover a checksum), include the bitbuffer codes in the `README.md`.

You can rename the sample files to add information, e.g. replace `g001` with `low_battery`. Do not remove the frequency and sample rate information.

Also add a `README.md` and perhaps pictures of the hardware. E.g. `front.jpg`, `back.jpg`, `inside.jpg`.
Limit the picture size to about 50k by cropping and compression.

Samples are contained in directories with the scheme: `tests/GROUP/DEVICE/SET`
- `GROUP` is optional and usually the manufacturer or common protocol, e.g. `lacrosse`
- `DEVICE` is the device name, e.g. `tx141w`
- `SET` is optional and used for different actual devices, not functions. E.g. `01`
- Each level should have a `README.md` describing that level.

Browse the [Decoder and Sample Explorer](https://triq.org/explorer/) to see how we extract metadata from rtl_433_tests.

To discuss the device and decoding open an issue on [rtl_433](https://github.com/merbanan/rtl_433/issues).
Issues in rtl_433_tests are used for the acutal building and testing only.
PRs on rtl_433_tests should only discuss the merging and not the device.
