#!/bin/bash

array=($(ls *[s].jpg))
for i in "${array[@]}"
do
    convert $i -crop 330x330+0+45 $i
done

