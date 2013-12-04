#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools
from math import *
from sets import Set
import string
import re

print sum([16*n*n+4*n+4 for n in range(1,501)])+1