#!/bin/bash

LINE=$(df -k | grep "/sd" | awk '{ print $1, $4, $3 }' | wc -l)
LIMIT=$[$LINE+1]
I=1
STRING='{'

while [ $I -lt $LIMIT ]
        do
        VOLn=$(df -k | grep "/sd" | awk 'FNR=='$I' { print $1 }')
        VOLt=$(df -k | grep "/sd" | awk 'FNR=='$I' { print $4 }')
        VOLu=$(df -k | grep "/sd" | awk 'FNR=='$I' { print $3 }')
        STRING+="$STRINT '"$VOLn"_t': '$VOLt', '"$VOLn"_u': '$VOLu',"
        I=$((I+1))
        done

echo $STRING"}"
