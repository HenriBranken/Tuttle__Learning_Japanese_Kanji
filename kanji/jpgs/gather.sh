for i in $(ls -d ../chap*)
do
	(
	fname=`echo $i | cut -c 4-`
	cp -v ../$fname/matrix.pdf ./$fname.pdf
	cp -v ../$fname/so_matrix.pdf ./so_$fname.pdf
	convert -colorspace RGB -interlace none -density 300x300 -quality 100 -background white -alpha remove $fname.pdf $fname.jpg
	convert -colorspace RGB -interlace none -density 300x300 -quality 100 -background white -alpha remove so_$fname.pdf so_$fname.jpg
	)
done

rm -v *.pdf
