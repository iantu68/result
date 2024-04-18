#!/bin/bash

read -p "input file number:" num

if ! [[ $num =~ ^[0-9]+$ ]]; then
	echo "Fail!"
	exit 1
fi

for ((i=1; i<=$num; i ++))
do
	mkdir "Layer_$i"
done
echo "Folder Create Successfully!"
