#!/bin/bash

## Your git project directory
PRJDIR=~/Projects

## Test command
CMD="$PRJDIR/rtl_433/build/src/rtl_433 -q -r"

## Find all data files (sort for consistency between runs)
DATAFILES=$(find $PRJDIR/rtl_433_tests -iname "*.data" | sort)

## Run though all test data
for FILE in $DATAFILES
do
    # in case of very bad samples, check if they require specific level to pass
    # use only in emergency
    LEVEL_FILE="$(dirname "$FILE")/level"
    if [[ -r "$LEVEL_FILE" ]] ; then
        LEVEL="-l $(cat "$LEVEL_FILE")"
    else
        LEVEL=
    fi

    # Add a "samplerate" file in case of non-standard samplerate
    SAMPLERATE_FILE="$(dirname "$FILE")/samplerate"
    if [[ -r "$SAMPLERATE_FILE" ]] ; then
        SAMPLERATE="-s $(cat "$SAMPLERATE_FILE")"
    else
        SAMPLERATE=
    fi

#	$CMD $FILE $SAMPLERATE -l 0   # Auto level
	$CMD $FILE $SAMPLERATE $LEVEL
done

