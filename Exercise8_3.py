# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:39:58 2016

@author: kuangyiyun
"""

#Exercise 8.3
fhand = open('mbox-short-2.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) >= 3 and words[0] == 'From':
        print (words[2])