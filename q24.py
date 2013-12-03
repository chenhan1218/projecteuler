#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *

def permute(str, n):
    if(len(str)<=1):
        return str
    else:
        n %= factorial(len(str))
        index = n/factorial(len(str)-1)
        return str[index]+permute(str[0:index]+str[index+1:],n%factorial(len(str)-1))

print permute('0123456789', 999999)