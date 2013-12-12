#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
import sys
def erat2( ):
    D = {  }
    yield 2
    for q in islice(count(3), 0, None, 2):
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
  return list(takewhile(lambda p: p<n, erat2()))

if __name__ == "__main__":
    # Be aware, this program runs about 40 minutes
    # But to ensure there is no other sets sum up in 27000, I think it is nessesary.
    SUM_UPPERBOUND = 27000
    n = 5

    def isPrimeAfterConcatenate(a,b):
        c = int(str(a)+str(b))
        for p in takewhile(lambda p:p*p<=c, erat2()):
            if c % p == 0:
                return False
        c = int(str(b)+str(a))
        for p in takewhile(lambda p:p*p<=c, erat2()):
            if c % p == 0:
                return False
        return True
    
    d = [[p] for p in get_primes_erat(SUM_UPPERBOUND)]
    for k in xrange(2,n+1):
        b = []
        for i in xrange(len(d)):
            for j in xrange(i+1, len(d)):
                if d[i][0:-1] == d[j][0:-1] and sum(d[i]+[d[j][-1]])<=SUM_UPPERBOUND:
                    if isPrimeAfterConcatenate(d[i][-1], d[j][-1]):
                        b.append(d[i]+[d[j][-1]])
                else:
                    break
        d = b
    print sum(d[0])
