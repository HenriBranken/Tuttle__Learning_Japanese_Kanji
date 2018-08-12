for i in $(ls *.png)
do
	(
	naampie=${i%.*}
	sips -s format pdf $i --out $naampie.pdf
	)
done

rm -v *.png