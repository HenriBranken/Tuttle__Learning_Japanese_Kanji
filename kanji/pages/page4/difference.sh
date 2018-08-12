folders=(chap9 chap10 chap11)
#echo ${#folders[@]}
for i in $(echo ${folders[@]})
do
  for j in $(ls ../../$i/*.pdf)
  do
    arr+=(`basename $j`)
  done
done
#echo ${arr[@]}
for h in $(ls ./*.pdf)
do
  page_arr+=(`basename $h`)
done
#echo ${page_arr[@]}
for k in $(echo ${arr[@]} ${page_arr[@]} | tr ' ' '\n' | sort | uniq -u)
do
  diff_arr+=($k)
done
#echo ${diff_arr[@]}
for l in $(echo ${diff_arr[@]})
do
  cp -v ../../*/$l ./
done
