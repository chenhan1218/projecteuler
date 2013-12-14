#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
from sets import Set
from collections import *
from itertools import *

def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

if __name__ == "__main__":
    MAXI = 140000
    primeNum = [0] * (MAXI+1)
    consecutive = 4
    for p in takewhile(lambda p: p<= MAXI, erat2()):
        for i in xrange(p,MAXI-MAXI%p+1,p):
            primeNum[i] += 1
    idx = [i for i,v in enumerate(primeNum) if v == 4]
    for i in xrange(0,len(idx)-consecutive+1):
        if idx[i+consecutive-1]-idx[i]==consecutive-1:
            print idx[i]
            break