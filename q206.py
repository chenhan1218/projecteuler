#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
import math

if __name__ == "__main__":
    MINI = 1020304050607080900
    MAXI = 1929394959697989990
    ans = 0
    # n^2 == 1_2_3_4_5_6_7_8_9_0
    # n must be 1XXXXXXX30 or 1XXXXXXX70
    for i in count(int(math.floor(math.sqrt(MINI)/10))):
    	if (i*10)**2 > MAXI:
    		break
    	if str(((i+3)*10)**2)[0::2]=="1234567890":
    		ans = (i+3)*10
    		break
    	if str(((i+7)*10)**2)[0::2]=="1234567890":
    		ans = (i+7)*10
    		break
    print ans