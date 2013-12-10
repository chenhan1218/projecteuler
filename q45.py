#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys

def tri(n):
	return n*(n+1)/2
def penta(n):
	return n*(3*n-1)/2
def hexagon(n):
	return n*(2*n-1)

if __name__ == "__main__":
    MAXINT = 1600000000
    triangle = Set(map(tri,takewhile(lambda n:tri(n)<MAXINT, count(1))))
    pentagonal = Set(map(penta,takewhile(lambda n:penta(n)<MAXINT, count(1))))
    hexagonal = Set(map(hexagon,takewhile(lambda n:hexagon(n)<MAXINT, count(1))))

    l = list(triangle.intersection(pentagonal).intersection(hexagonal))
    print l[2]
