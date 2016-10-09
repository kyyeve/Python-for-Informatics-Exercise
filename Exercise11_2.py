# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:27:54 2016

@author: kuangyiyun
"""

#Exercise 11.2
import re

fname = 'mbox.txt'
fhand = open(fname)
count = 0
total = 0

for line in fhand:
    x= re.findall('New Revision: (\d+)', line)
    if len(x) != 0:
        count += 1
        total += float(x[0])
        
print (total/float(count))