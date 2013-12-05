#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
from itertools import *

def pentagonal(n):
    return n*(3*n - 1) / 2

if __name__ == "__main__":
    module = 1000000
    p=[1,1];

    for n in count(2):
        p.append(0)

        # http://en.wikipedia.org/wiki/Partition_%28number_theory%29#Exact_formula
        # Exact formula of partition function
        # the summation is over all nonzero integers k (positive and negative) and p(m) is taken to be 0 if m < 0.
        for k in count(1):
            # positive k
            sign = -1 if k%2==0 else 1
            penta = pentagonal(k)
            if penta > n:
                break
            p[n] += sign * p[n - penta]

            # negative k
            sign = -1 if k%2==0 else 1
            penta = pentagonal(-k)
            if penta > n:
                break
            p[n] += sign * p[n - penta]

        p[n] %= module
        #print n, p[n]
        if p[n] == 0:
            break
    n = len(p)-1
    print n

# import itertools
# import copy

# if __name__ == "__main__":
#     module = 1000000
#     MAX_N = 56000

#     #Leonhard Euler's pentagonal number theorem
#     ways=[1L]*(MAX_N+1)
#     for coin in xrange(2,MAX_N+1):
#         for n in xrange(MAX_N+1):
#             if coin <= n:
#                 ways[n] = (ways[n]+ways[n-coin])%module
#         print coin, ways[coin]
#         if ways[coin] == 0:
#             break

