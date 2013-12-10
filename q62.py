#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
from collections import *

if __name__ == "__main__":
    d = defaultdict(list)
    l=[]
    maxx=0
    for a in count(1):
    	s = ''.join(sorted(str(a**3)))
    	d[s].append(a)
    	maxx=max(maxx,len(d[s]))
    	if len(d[s]) == 5:
    		l=d[s]
    		break
    print l[0]**3