#!/usr/bin/python
# -*- coding: utf-8 -*-
from sets import Set
import itertools
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


MAX_NUM=28123

sum_factors = [0] * (MAX_NUM+1)
for factor in xrange(1,MAX_NUM+1):
	multi = factor*2
	while multi <= MAX_NUM:
		sum_factors[multi] += factor
		multi += factor

abundant = [index for index, x in enumerate(sum_factors) if x>index and index!=0]
sum_abundant = reduce(lambda s, x: s.union(Set([x+y for y in abundant])), abundant, Set())

answer = [x for x in xrange(1,MAX_NUM+1) if x not in sum_abundant]
print sum(answer)
