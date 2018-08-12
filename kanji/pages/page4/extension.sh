for i in $(ls *.jpg)
do
	(
	naampie=${i%.*}
	sips -s format pdf $i --out $naampie.pdf
	)
done