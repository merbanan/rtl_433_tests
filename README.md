rtl_433_tests
=============

rtl_433_tests contains the test suite for rtl_433

This repository contains lots of signal recordings that are supported by rtl_433.

The regtest system is not developed yet, but accepting signal recordings.


Installation instructions:
--------------------------

Clone this reposity for the root of rtl_433

Running:
--------

Enter the directory and run `make test`. The output will tell if the tests failed or not.

Contributing:
-------------

Run rtl_433 with `rtl_433 -a -t` and wait for you signal to be detected. When it is detected 
note what gfile name it has. This file can now be run through rtl_433 offline:

    $ rtl_433 -r gfile001.data

You can also add `-a` or `-A` to see what it looks like in analyze mode.

Add signals by creating a directory with the protocol name and then add the gfiles under a
directory with 2 number directory name. Also add a `readme.md` and a picture of the hardware.

Eg tests/prologue/01

