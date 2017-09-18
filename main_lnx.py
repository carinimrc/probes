#!/usr/bin/env python

import subprocess
import os
import json

sys = subprocess.check_output("scripts/check_sys.sh")
sys = sys.replace('\'', '\"')
sys = eval(sys)

hdd = subprocess.check_output("scripts/check_hdd.sh")
hdd = hdd.replace('\'', '\"')
hdd = eval(hdd)

RAM_t = float(sys["RAM_t"])
RAM_u = float(sys["RAM_u"])
RAM_p = RAM_u/RAM_t*100
RAM_p = round(RAM_p, 1)
SWAP_t = float(sys["SWAP_t"])
if SWAP_t == 0:
	SWAP_t = 1
SWAP_u = float(sys["SWAP_u"])
SWAP_p = SWAP_u/SWAP_t*100
SWAP_p = round(SWAP_p, 1)

print("##### DEBUG ##########################")
print("The CPU load is " + sys["CPU"] + "%")
print("Tha RAM load is " + str(RAM_p) + "%")
print("Tha SWAP load is " + str(SWAP_p) + "%")
for key in hdd:
        print("The VOL " + key + " is full at " + hdd[key] + "%")
print("######################################")
