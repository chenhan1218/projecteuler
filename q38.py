#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import Set

if __name__ == "__main__":
    largest=0
    for x in xrange(1,10000):
        string=""
        for n in count(1):
            string += str(x*n)
            if len(string) >= 9:
                break
        if len(string)==9 and len(Set(string)-Set(['0']))==9:
            largest = max(largest, int(string))

    print largest
            


