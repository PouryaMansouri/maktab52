#!/bin/bash

read -p "What is yout=r file's name? " file_name

echo "start searching"
for file in $(ls|sort);do

	if [ $file_name ==  $file  ]
	then
		echo -e  "name match:\n"
		if [ -f $file ]
		then
			echo -e "last 10 line, start:\n********\n\n"
			tail -n 10 $file
			echo -e "\n\n********\nlast 10 line, finish\n"
		fi
		if [ -d $file ] 
		then
			echo "It isn't a file"
		fi
	fi
	echo
done

