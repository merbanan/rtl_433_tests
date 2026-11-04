# rtl_433 test for Simple False Positives #

rtl_433_tests/test_false_positives contains the tests for rtl_433 to check for false positives from simple data
containing repeating data patterns of `0x00`, `0xFF` and `0x55`


## Installation instructions ##

report script requires the [jq](https://github.com/stedolan/jq/) to run

## Running ##

Enter `make`
: The output will tell if the tests failed or not.


enter `make clean`
: To delete test results

enter `make real_clean`
: To delete test results and test data
