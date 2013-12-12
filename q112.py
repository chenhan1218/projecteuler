#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys

def isBouncy(n):
	s = str(n)
	ss = ''.join(sorted(s))
	return s != ss and s != ss[::-1]

if __name__ == "__main__":
    notBounty = 0
    ans = 0
    for n in count(1):
    	if not isBouncy(n):
    		notBounty+=1
    	if n==notBounty*100:
    		ans = n
    		break
    print ans