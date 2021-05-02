#!/bin/bash

read -p "What is yout=r file's name? " file_name

echo -e  "start searching:\n"
flag=true
for file in $(ls|sort);do

	if [ $file_name ==  $file  ]
	then
		flag=false
		echo -e  "name match:\n"
		if [ -f $file ]
		then
			echo -e "last 10 line, start:\n********\n\n"
			tail -n 10 $file
			echo -e "\n\n********\nlast 10 line, finish\n"
		fi
		if [ -d $file ] 
		then
			echo "It isn't a file, it's directory"
		fi
		echo
	fi
done
if $flag
then
	echo -e "File dose not exist\n"
fi

