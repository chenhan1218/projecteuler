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
    primes = get_primes_erat(10000)
    d = defaultdict(list)
    l = []
    for p in takewhile(lambda p: p<10000, dropwhile(lambda p: p>=1000, erat2())):
        d[''.join(sorted(str(p)))].append(p)
    for key in d:
        if len(d[key]) > 3:
            for t in combinations(d[key], 2):
                if t[0] != 1487 and t[1]*2-t[0] in d[key]:
                    l = [t[0], t[1], t[1]*2-t[0]]
    print ''.join(map(str,l))