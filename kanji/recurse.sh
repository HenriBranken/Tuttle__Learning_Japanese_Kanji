xebuild() {
i="$1"
naam=${i%.*}
xelatex -synctex=1 -interaction=nonstopmode $naam.tex
okular $naam.pdf
}

for i in $(ls -d chap*/)
do
	(
	fol_name=`echo $i | rev | cut -c 2- | rev`
	cd ./$fol_name/
	xebuild matrix.tex
	)
done
