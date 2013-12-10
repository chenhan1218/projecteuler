#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
import string

if __name__ == "__main__":
    encrypted = [map(int,lines.split(',')) for lines in sys.stdin][0]
    s=False

    l = 3
    count = 0
    ans=""
    for secret in product(string.lowercase, repeat=3):
    	count+=1
    	it = cycle(secret)
    	message = ''.join(map(lambda i: chr(ord(it.next())^i), encrypted))
    	if "the" in message and "to" in message and "and" in message and "of" in message and "in" in message:
    		ans = message
    		break
    print ans
    print sum(map(ord,ans))
    