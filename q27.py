#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
from sets import Set

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
    maxPrime = 0
    multi = 0
    primes = Set(get_primes_erat(1000000))
    for a,b in itertools.product(range(-999,1000),range(-999,1000)):
        count = len(list(itertools.takewhile( lambda n: abs(n*n+a*n+b) in primes, itertools.count() )))
        if count > maxPrime:
            maxPrime = count
            multi = a * b
    print multi

