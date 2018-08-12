for i in $(ls -d ../chap*)
do
	(
	fname=`echo $i | cut -c 4-`
	cp -v ../$fname/matrix.pdf ./$fname.pdf
	cp -v ../$fname/so_matrix.pdf ./so_$fname.pdf
	)
done
