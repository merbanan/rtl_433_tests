#!/bin/bash

## Your git project directory
PRJDIR=~/projects

## Test command
CMD="$PRJDIR/rtl_433/build/src/rtl_433 -r"

## Find all data files (sort for consistency between runs)
DATAFILES=$(find $PRJDIR/rtl_433_tests -iname "*.data" | sort)

## Run though all test data
for FILE in $DATAFILES
do
	$CMD $FILE
done

