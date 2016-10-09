# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:41:46 2016

@author: kuangyiyun
"""

#Exercise 8.4
fname = 'remeo.txt'
fhand = open(fname)
ls = []
for line in fhand:
    for words in line.split():
        if words not in ls:
            ls.append(words)

ls.sort()
print (ls)
