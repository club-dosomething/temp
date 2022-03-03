#!/bin/bash

imgs="*.png"
for f in $imgs
do
	echo "[$f]"
	if [[ $f =~ ([0-9a-zA-Z_]+)_([0-9]+)_([0-9]+).png ]]
	then
		name="${BASH_REMATCH[1]}"
		sub="${BASH_REMATCH[2]}"
		ind="${BASH_REMATCH[3]}"

		echo $name
		echo $sub
		echo $ind
	fi
done


