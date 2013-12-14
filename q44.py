#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
import math

def pentagon(n):
    return n*(3*n-1)/2

def isPentagon(n):
    return ((1+math.sqrt(1+24*n))/6).is_integer()

def isPentagon2(n):
    begin=1
    end=n+1
    while end-begin>=2:
        mid = (begin+end)/2
        p = pentagon(mid)
        if p == n:
            return True
        elif p > n:
            end=mid
        else:
            begin=mid
    return pentagon(begin)==n

if __name__ == "__main__":
    penta_list = map(pentagon, takewhile(lambda n:pentagon(n)<100000000,count(1)))
    penta = Set(penta_list)

    # D = P2167 − P1020 = 7042750 - 1560090 = 5482660 = P1912
    d = False
    for i in count(1):
        a = pentagon(i)
        for j in count(1):
            b = pentagon(j)
            if pentagon(j+1)-pentagon(j) > a:
                break
            if isPentagon(a+b) and isPentagon(b+a+b):
                d=a
                #print "a,b", a,b
                break
        if d:
            break
    print d
