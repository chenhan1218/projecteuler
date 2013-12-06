#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
import string

if __name__ == "__main__":
    char=['I','V','X','L','C','D','M']
    value=[1,5,10,50,100,500,1000]
    d = dict(zip(char,value))

    def int2roman(s):
        ans = ""
        for i in reversed(xrange(len(value))):
            # for case like IX
            if i%2==1 and s/value[i-1]==9 and i+1<len(value):
                ans += char[i-1] + char[i+1]
                s %= value[i-1]
            # for case like IV
            elif i%2==0 and s/value[i]==4 and i+1<len(value):
                ans += char[i] + char[i+1]
                s %= value[i]
            else:
                ans += char[i] * (s/value[i])
                s %= value[i]

        return ans
    def roman2int(s):
        ans = 0
        for i in xrange(len(s)):
            ans += d[s[i]]
            if i>0 and d[s[i]]>d[s[i-1]]:
                ans -= d[s[i-1]]*2
        return ans

    #for x in sys.stdin:
    #    print saved(string.rstrip(x)), x
    print sum(map(lambda s:len(s)-len(int2roman(roman2int(s))),map(string.rstrip, sys.stdin)))

