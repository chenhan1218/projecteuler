#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
from fractions import Fraction

def e_genertator():
	yield 2
	for k in count(1):
		yield 1
		yield 2*k
		yield 1

if __name__ == "__main__":
	d = [n for n in islice(e_genertator(), 100)]
	f = Fraction(d.pop(), 1)
	for i in reversed(d):
		f = i + 1/f
	print sum(map(int,str(f.numerator)))
