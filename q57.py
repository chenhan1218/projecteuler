#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
from fractions import Fraction

if __name__ == "__main__":
    f = Fraction(1,1)
    count = 0
    for i in xrange(1000):
    	f = 1+1/(1+f)
    	if len(str(f.numerator))-len(str(f.denominator))>0:
    		count += 1
    print count
