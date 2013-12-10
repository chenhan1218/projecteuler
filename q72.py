#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
import itertools
from sets import *
import sys

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

def primeCombination(n, MAXMUL, init, mul, depth):
	if depth == n:
		yield mul
	else:
		for p in dropwhile(lambda x: x<init, erat2()):
			if mul*(p**(n-depth)) <= MAXMUL:
				for m in primeCombination(n, MAXMUL, p+1, mul*p, depth+1):
					yield m
			else:
				break

if __name__ == "__main__":
	MAXD = 1000000
	ans = 0
	for i in count():
	    l = []
	    for n in primeCombination(i,MAXD,1,1,0):
	    	l.append(n)
	    	if i%2==0:
	    		ans += (MAXD/n)*(MAXD/n-1)/2
	    	else:
	    		ans -= (MAXD/n)*(MAXD/n-1)/2
	    if len(l) == 0:
	    	break
	print ans
