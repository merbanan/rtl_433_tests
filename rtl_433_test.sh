#!/bin/bash

## Your git project directory
PRJDIR=~/Projects

## Test command
CMD="$PRJDIR/rtl_433/build/src/rtl_433 -r"

## Find all data files (sort for consistency between runs)
DATAFILES=$(find $PRJDIR/rtl_433_tests -iname "*.data" | grep xc | sort)

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
	$CMD $FILE $LEVEL
done

