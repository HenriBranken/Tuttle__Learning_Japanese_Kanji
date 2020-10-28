#!/bin/bash

array=($(ls *.jpg))
for i in "${array[@]}"
do
    convert $i -crop 330x330+0+45 $i
done

