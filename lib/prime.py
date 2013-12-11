#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
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
