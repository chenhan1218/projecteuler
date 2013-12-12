#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
import itertools
from sets import *
import sys
from fractions import Fraction

if __name__ == "__main__":
	l = []
	for denominator in xrange(1, 1000001):
		if (3*denominator) % 7 != 0:
			l.append(Fraction(3*denominator/7, denominator))
	print max(l).numerator
