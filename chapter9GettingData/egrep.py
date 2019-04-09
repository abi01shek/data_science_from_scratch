# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:09:33 2019

@author: abi01
"""

import sys, re

# regex is the first argument 
regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex,line):
        sys.stdout.write(line)
