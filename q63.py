#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys

if __name__ == "__main__":
    s = 0
    for base in xrange(1,10):
    	s += len([p for p in takewhile(lambda p: len(str(base**p))==p, count(1))])
    print s