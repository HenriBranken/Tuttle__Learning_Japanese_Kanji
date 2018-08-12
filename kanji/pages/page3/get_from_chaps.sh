folders=(chap6 chap7 chap8 chap9)
echo ${folders[@]}
for i in $(echo ${folders[@]})
do
  for j in $(ls ../../$i/*.pdf)
  do
    arr+=(`basename $j`)
  done
done
arr=(${arr[@]//so_*/})
arr=(${arr[@]//tb_*/})
arr=(${arr[@]//matrix/})
echo ${arr[@]}
for l in $(echo ${arr[@]})
do
  cp -v ../../*/$l ./
done
