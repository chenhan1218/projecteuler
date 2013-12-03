#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import re

def value(name):
	return sum(map(lambda x: ord(x)-ord('A')+1, list(name)))

name = re.findall(r"[\w]+", raw_input())
name.sort()
print sum([(i+1) * value(x) for i,x in enumerate(name)])
