#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
from math import *
from sets import Set
import string
import re

count=0
s = Set()
for digits in xrange(1,9):
	for x in itertools.combinations_with_replacement("0123456789", digits):
		total = sum(map(factorial,map(int,x)))
		if str(total).__len__() == x.__len__() and sorted(str(total))==map(str,x):
			s.add(total)

print sum(s.difference(Set([1,2])))