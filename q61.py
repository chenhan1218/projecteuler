#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
import sys
from collections import *
from sets import *

if __name__ == "__main__":
    base=100
    formulae=6

    # dictionary
    # map triangle, square, pentagonal, hexagonal, heptagonal, octagonal
    # to d[0]~d[5]
    # 210 is a triangle number
    # so d[0][21] contains 0
    # 1045 is a Octagonal number
    # so d[5][10] contains 45
    d = [defaultdict(Set) for i in xrange(formulae)]
    for f in xrange(formulae):
        for k, v in map(lambda x: (x/base,x%base), filter(lambda x: x>=base*base/10,map(lambda n: n*((f+1)*n-f+1)/2, takewhile(lambda n: n*((f+1)*n-f+1)/2<base*base,count(1))))):
            d[f][k].add(v)
    
    all_possible=[];
    for per_d in permutations(d):
        p = [[i] for i in xrange(base)]
        for f in xrange(formulae):
            newP = []
            for pos in p:
                for num in per_d[f][pos[-1]]:
                    newP.append(pos+[num])
            p=newP
        all_possible += filter(lambda x: x[0]==x[-1], p)

    # collect numbers
    s=[]
    for i in xrange(formulae):
        s.append(all_possible[0][i]*100+all_possible[0][i+1])
    print sum(s)

