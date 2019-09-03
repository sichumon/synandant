#! /bin/bash

countdown(){
  date1=$((`date +%s` + $1));
  while [ "$date1" -ge `date +%s` ]; do
  echo -ne "\r$(date -u --date @$(($date1 - `date +%s`)) +%H:%M:%S)\r";
  sleep 0.1
  done
printf "\n\nTime for the answer:"
}

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

COUNT=0
CORRECT=0
clear

echo "Enter the Times Table to practise"
read TT

MAX=12
while true
do
clear
echo -e "\n STATUS -- $CORRECT / $COUNT\n\n"
MIX=`echo $((RANDOM % $MAX + 1))`

echo "$MIX X $TT = "
echo
countdown 1
read ans

while [[ $ans = "" ]]
do
echo "$MIX X $TT = "
read ans
done

urans=`echo $ans|sed 's/ //g'`
corans=`echo $MIX "*" $TT|bc`

if [[ $urans -eq $corans ]]
then
echo "Well Done, You have one more point"
CORRECT=`expr $CORRECT + 1`
else
printf "\n Too Bad you fool, You have made a mistake, ${red}THE CORRECT ANSWER is ${green} $corans ${reset}"

fi
COUNT=`expr $COUNT + 1`
read X
ans=""
done
