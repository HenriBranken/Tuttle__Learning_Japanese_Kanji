for i in $(ls *.png)
do
	(
	naampie=${i%.*}
	convert $i -threshold 99.9% $naampie.pdf
	)
done

#rm -v *.png
