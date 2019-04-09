# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:22:37 2019

@author: abi01
"""

import sys
from collections import Counter 



try:
    num_words = int(sys.argv[1])
except:
    print("Usage",(sys.argv[0]),"  num_words" )
    sys.exit(1)
    
counter = Counter (word.lower()
for line in sys.stdin
for word in line.strip().split()
if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
