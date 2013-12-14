#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import *
from sets import *
import sys
import re
from collections import *

if __name__ == "__main__":
    attempts = [re.findall(r"[\w]",lines) for lines in sys.stdin]
    code = reduce(lambda s, a: s.union(set(a)), attempts, set())
    child = defaultdict(set)
    for attempt in attempts:
    	for i, v in enumerate(attempt):
    		if i!= 0:
    			child[attempt[i-1]].add(attempt[i])
    # Topological sort
    # http://en.wikipedia.org/wiki/Topological_sorting
    noIncomingNode = code.difference(reduce(set.union, child.itervalues()))
    passcode = ""
    while len(noIncomingNode) != 0:
    	n = noIncomingNode.pop()
    	passcode += n

    	setm = set(child[n])
    	child[n].clear()
    	# for each node m with an edge e from n to m do
    	for m in setm:
    		# if m has no other incoming edges
    		if m not in reduce(set.union, child.itervalues()):
    			noIncomingNode.add(m)

    if len(reduce(set.union, child.itervalues())) != 0 :
    	raise Exception("graph has at least one cycle!")
    else:
    	print passcode