# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:18:45 2019

@author: abi01
"""

#line_count.py
import sys

line_count = 0
for line in sys.stdin:
    line_count = line_count+1
    
print(line_count)