#!/bin/sh

#for i in {001..084}

#do
#     CMD=`/usr/local/bin/rtl_433 -a -r gfile"$i".data &> result"$i".txt`
#    echo "File gfile+$i processed"
#    $i++
#done


i=1
for file in gfile???.data

do
  echo " "
  echo "###################################################################"
  echo "-------------------------"$file"-----------------------------"
  echo "###################################################################"
  echo " "
  echo "/usr/local/bin/rtl_433 -a -r "$file""
  echo " "
  `/usr/local/bin/rtl_433 -a -r "$file"`
  echo " "
  echo "###################################################################"
  echo " "
  echo "/usr/local/bin/rtl_433 -A -r "$file""
  echo " "
  `/usr/local/bin/rtl_433 -A -r "$file"`
 
done
