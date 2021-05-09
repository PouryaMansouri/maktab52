#!/bin/bash
# Play random mp3

# Variables
SONG=$(cat last_song.txt)
MOCP_STATUS=$(pgrep mocp)

#fuction to play music
randomsong () {
# Check if mocp is running. If not running, start mocp
if [ -z "$MOCP_STATUS" ] && [ "$1" != "stop" ];
then
SONG=$(ls *.mp3 | shuf -n1)
echo "Playing ${SONG}"
mocp -S
echo "$SONG" > last_song.txt

# If argument "stop" is given, stop mocp 
elif [ -n "$MOCP_STATUS" ] && [ "$1" = "stop" ];
then mocp -x

#get score just when stop the music
# flag=true
while [[ true ]]; do
	#statements
	read -p "get score to music(1-10): " score
	if [ $score -le 10 ] && [ $score -ge 1 ];
	then
		echo "$SONG = $score" >> score.txt
		# cat score.txt 
		list=$(cat score.txt | grep "$SONG")
		# echo $list
		break
	else
		echo "enter between 1 and 10"
		echo
	fi 
done
cat score.txt | grep "$SONG" > tak_score.txt
scores=$(cat tak_score.txt | grep -o -P '= \d+' |grep -o -P '\d+')
n=$(echo "$scores" | wc -l)
sum=0

for score in $scores
do
	# echo $score
	sum=$[ $sum + $score ]
done
echo "sum score is $sum"
echo  "times played is $n"
ave=$[ $sum/$n]
# echo $ave
# echo "$SONG played $n times and average score is $ave" >> ave.txt
echo "$SONG played $n times and average score is $ave" 
elif [ -n "$MOCP_STATUS" ] && [ "$1" != "stop" ]; then
	#statements
	echo "player was started before"
	echo "if you want to stop, run bash with stop argument"
else
	echo "player was stoped before"
fi

# Append random song to mocp playlist and start playing playlist
# echo "start"
# mocp -c -a -p "$SONGPATH" 2> ./file.txt; }
}

randomsong "$*"
