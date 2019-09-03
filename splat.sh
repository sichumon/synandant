#!/bin/bash

INFILE=$1

#echo "llist=[$(cat ${INFILE} |while read line; do one=$(echo $line|awk '{print $1}'); two=$(echo $line|awk '{print $2}'); echo "[['${one}', '${two}']],"; done|sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g')]"
#echo "nlist=[$(cat ${INFILE} |while read line; do one=$(echo $line|awk '{print $1}'); two=$(echo $line|awk '{print $2}'); echo "['${one}', '${two}'],"; done|sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g')]"


cat $INFILE|while read a b; do echo " ['$a', '$b'],"; done
