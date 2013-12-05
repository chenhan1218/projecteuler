#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

if __name__ == "__main__":
    longest = 0
    d = 0
    for i in xrange(2,1000):
    	remainder=[]
    	numerator = 1
    	while numerator not in remainder:
    		remainder.append(numerator)
    		numerator = (numerator*10) % i
    	#print i, len(remainder)-remainder.index(numerator)
    	if len(remainder)-remainder.index(numerator) > longest:
	    	longest = len(remainder)-remainder.index(numerator)
	    	d = i
    print d


