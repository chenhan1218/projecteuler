#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys

def isPalindrome(s):
	return s == s[::-1]

def isLychrel(n):
	for i in xrange(50):
		n += int(str(n)[::-1])
		if isPalindrome(str(n)):
			return False
	return True

if __name__ == "__main__":
    print map(isLychrel, range(10000)).count(True)
