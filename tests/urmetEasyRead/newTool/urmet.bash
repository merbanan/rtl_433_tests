
FILES=/media/fraschi/W7/rpiRadio/buoni/freqNew/*.data
for f in $FILES
do
  python newdemod.py $f
  python newdecode.py /home/fraschi/testOutput.data e $f
done
FILES2=/media/fraschi/W7/rpiRadio/buoni/freqNew-2M/*.data
for g in $FILES2
do
  python demod.py $g
  python newdecode.py /home/fraschi/gfskQuadDemod.data e $g
done

