for i in $(ls -d ../page*)
do
	(
  fname=`echo $i | cut -c 4-`
	echo $fname
	cp -v ../$fname/matrix.pdf ./$fname.pdf
	)
done
