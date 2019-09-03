#!/bin/bash

COUNT="0"
CORRECT="0"

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
#echo "${red}red text ${green}green text${reset}"

cleanup(){ 
if [ ! -z $PERC ]
 then 
	#printf ${green}"\n\n So far your score is: $CORRECT / $COUNT\n "
	printf ${green}"\n\n  The Percentage of correct answers was $PERC"
 fi 
}
trap 'cleanup' EXIT

countdown(){
  date1=$((`date +%s` + $1));
  while [ "$date1" -ge `date +%s` ]; do
  echo -ne "\r$(date -u --date @$(($date1 - `date +%s`)) +%H:%M:%S)\r";
  sleep 0.1
  done
printf "\n\nTime for the answer:"
}


clear

MAX=999
LIST=99
while true
do
clear
echo -e "\n STATUS -- $CORRECT / $COUNT\n\n"
NO1=`echo $((RANDOM % $MAX + 1))`
NO2=`echo $((RANDOM % $LIST + 1))`

while [[ $ans = "" ]]
do
clear
	printf ${green}"\n\n So far your score is: $CORRECT / $COUNT "
echo
echo
echo
echo
echo " $NO1 *"
echo "  $NO2"
echo
echo "----------- "
echo
read -p "ANSWER:" ans;echo
#test ! -z "ans" && { break ; }
#read -r -s -t 1  -p "ANSWER:" -s holder && ans="$holder"
#countdown 3
# Check for Space
    if [[ ${ans} =~ \ + ]]; then
       echo "space found"
       echo "$ans"
    # Check if input is NULL
    elif [[ -z "$ans" ]]; then
       { break ; }
    fi
done

urans=`echo $ans|sed 's/ //g'`
corans=`echo "$NO1 * $NO2"|bc`

if [[ $urans -eq $corans ]]
then
echo "Well Done, You have one more point"
CORRECT=`expr $CORRECT + 1`
    elif [[ -z "$urans" ]]; then
       printf "\n INPUT was NULL, Sleeping on the wheel ???? \n" 
else
#printf "\n Too Bad you fool, You have made a mistake, ${red}THE CORRECT ANSWER is ${green} $corans ${reset}"
printf "\n WRONG ANSWERRRRRR ${urans}, ${red}THE CORRECT ANSWER was ${green} $corans ${reset}\n "
fi
CORRECT=${CORRECT}
COUNT=`expr $COUNT + 1`
ans=""
#PERC="$(( (${CORRECT}/${COUNT}) * 100))"
#PERC=`expr \($CORRECT / $COUNT \) \* 199`
echo $PERC
read X
done

