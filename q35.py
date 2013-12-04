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

def all_rotation(str):
    return [str[i:]+str[0:i] for i in range(len(str))]

if __name__ == "__main__":
    primes = Set(get_primes_erat(1000000))
    circular=[]
    
    for value in primes:
        if reduce(lambda condition, value: condition and value in primes ,map(int,all_rotation(str(value))), True):
            circular.append(value)

    print circular.__len__()