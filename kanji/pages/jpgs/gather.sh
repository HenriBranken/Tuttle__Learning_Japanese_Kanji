for i in $(ls -d ../page*)
do
	(
	fname=`echo $i | cut -c 4-`
	cp -v ../$fname/matrix.pdf ./$fname.pdf
	convert -colorspace RGB -interlace none -density 300x300 -quality 100 -background white -alpha remove $fname.pdf $fname.jpg
	)
done

rm -v *.pdf
