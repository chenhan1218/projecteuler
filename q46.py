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
    primes = Set(get_primes_erat(1000000))
    for n in itertools.count(3, 2):
        if n not in primes:
            if any(map(lambda x: x in primes, [n-2*s*s for s in itertools.takewhile(lambda x:2*x*x<n, itertools.count(1))])) == False:
                print n
                break

