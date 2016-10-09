# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 23:26:09 2016

@author: kuangyiyun
"""

#Exercise 7.1
fname = 'mbox-short.txt'
fhand = open(fname)
for line in fhand:
    print (line.strip('\n').upper())