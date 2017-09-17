#!/bin/bash

CPU=$(top -b -n1 | grep Cpu | awk '{ print $2 }' | cut -d"%" -f1);
RAMt=$(free -m | grep Mem | awk '{ print $2 }' );
RAMu=$(free -m | grep Mem | awk '{ print $3 }' );
SWAPt=$(free -m | grep Swap | awk '{ print $2 }' );
SWAPu=$(free -m | grep Swap | awk '{ print $3 }' );

echo "{ 'CPU': '$CPU', 'RAM_t': '$RAMt', 'RAM_u': '$RAMu', 'SWAP_t': '$SWAPt', 'SWAP_u': '$SWAPu' }"
