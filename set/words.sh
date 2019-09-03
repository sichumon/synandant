#/bin/bash


while true
do 
word=$(cat wordlist |shuf -n 1)
echo $word 
sleep 5 
/usr/local/bin/def $word
sleep 30
echo $word >> practised_words
clear 

prword=$(cat practised_words |shuf -n 1)
echo $prword 
sleep 5 
/usr/local/bin/def $prword
sleep 15
clear 

done 
