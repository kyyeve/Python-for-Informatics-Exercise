# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:16:31 2016

@author: kuangyiyun
"""

#Exercise 11.1
import re

fname = 'mbox.txt'
fhand = open(fname)
count = 0
requirement = input("Enter a regular expression: ")
for line in fhand:
    if re.search(requirement, line):
        count += 1
        
print (fname + " had " + str(count) + " lines that matched " + requirement)