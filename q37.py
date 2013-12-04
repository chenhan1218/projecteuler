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
    s=[];
    toRightPrime=Set([2,3,5,7])
    toLeftPrime=Set([2,3,5,7])
    primes = get_primes_erat(1000000)

    digit = 10
    for p in primes:
        if digit*10<p:
            digit*=10

        if p/10 in toLeftPrime:
            toLeftPrime.add(p)
        if p%digit in toRightPrime:
            toRightPrime.add(p)
        if p >=10 and p in toLeftPrime and p in toRightPrime:
            s.append(p)
    print sum(s)
