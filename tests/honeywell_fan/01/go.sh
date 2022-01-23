FILES=`ls *.cu8`

for file in $FILES
do
	echo $file
	~/rtl_433_dev/rtl_433/build/src/rtl_433 -F json -r $file > `basename $file .cu8`.json
done
