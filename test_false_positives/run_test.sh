#!/bin/bash


#    Copyright (C) 2021 Peter Shipley
#
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.


# script to :
#
#  generate test data (if needed)
#
#  run rtl_433 with test data
#
#  sort/unique/print  results
#
# jq command needed for post processing result

# (requires `jq`  command)

default_values=("00" "FF" "55")

test_values=("${@:-${default_values[@]}}")

# build_dir=${HOME}/Projects/rtl_433/build/src/
def_build_dir=../../build/src/

build_dir=${BUILD_DIR:-$def_build_dir}

# test ! -d ${build_dir}/ && echo "${build_dir} does not exist" && exit 1

test ! -f ${build_dir}/rtl_433 && echo rtl_433 not found &&  exit 


# ls -l ${build_dir}/rtl_433
# ${build_dir}/rtl_433 -V

for x in "${test_values[@]}"
do
    dat_value=${x#0x}
    base_name="0x${dat_value}"
    json_outfile="${base_name}_out.json"
    stderr_outfile="${base_name}_out.stderr"
    data_file="${base_name}_data.txt"

    # echo json_outfile ${json_outfile}

    test -f ${json_outfile} &&   mv ${json_outfile} ${json_outfile}-old
    test -f ${stderr_outfile} && mv ${stderr_outfile} ${stderr_outfile}-old
    
    # create test input data if needed
    test -f ${data_file} || python3 gen_data.py ${x} > ${data_file}

    # -vv 
    # -K test_pat="0x${x}" 

    ${build_dir}/rtl_433 -y @${data_file} \
        -M protocol \
        -F "json:${json_outfile}"  2> ${stderr_outfile}

    if [ -s "${json_outfile}" ] ; then
	    echo "Potential False Positives with pattern 0x${x}"
	    echo "     Protocol	Model"
	    jq -r < ${json_outfile} '["", .protocol, .model, .msg] | @tsv' | sort -u -n 
	    echo "see file ${json_outfile} for details"
    else
	    echo "No False Positives with pattern 0x${x}"
    fi

done
