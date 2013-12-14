#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
import re
import math

def comp(a):
	return math.log(float(a[0]))*float(a[1])

if __name__ == "__main__":
    l = [tuple(re.findall(r"[\d]+",line)) for line in sys.stdin]
    print l.index(max(l, key=comp))+1