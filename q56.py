#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys

if __name__ == "__main__":
    n=100
    print reduce(max,map(lambda s: sum(int(c) for c in s), map(str,[a**b for a, b in product(xrange(n),xrange(n))])))