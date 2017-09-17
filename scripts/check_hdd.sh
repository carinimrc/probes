#!/bin/bash

LINE=$(df -k | grep "/sd" | awk '{ print $1, $4, $3 }' | wc -l)
LIMIT=$[$LINE+1]
I=1
STRING='{'

while [ $I -lt $LIMIT ]
        do
        VOLn=$(df -k | grep "/sd" | awk 'FNR=='$I' { print $1 }')
        VOLu=$(df -k | grep "/sd" | awk 'FNR=='$I' { print $5 }' | cut -d"%" -f1)
        STRING+="$STRINT '$VOLn': '$VOLu',"
        I=$((I+1))
        done

echo $STRING" }"
