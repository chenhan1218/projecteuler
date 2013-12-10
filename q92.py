#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
import string

def op(n):
    return sum(int(c)**2 for c in str(n))

def factorial(n):
    ans = 1
    while n > 0:
        ans *= n
        n-=1
    return ans

def possible(s):
    s=sorted(s)
    ans = factorial(len(s));
    repeat=0
    for i,c in enumerate(s):
        if i!=0 and c!=s[i-1]:
            ans /= factorial(repeat)
            repeat=1
        else:
            repeat+=1
    ans /= factorial(repeat)
    return ans

if __name__ == "__main__":
    c = 0
    for digit in xrange(0,7):
        for leading in "123456789":
            for s in combinations_with_replacement(string.digits, digit):
                b = ''.join(s)+leading
                n = int(b)
                while n != 1 and n!= 89:
                    n=op(n)
                if n == 89:
                    c += possible(s)
    print c