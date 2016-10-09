# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:42:07 2016

@author: kuangyiyun
"""

#Exercise 10.2
fname = 'mbox-short.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    line = line.rstrip('\n')
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        dic[words[5].split(':')[0]] = dic.get(words[5].split(':')[0], 0) + 1
        
ls = []
for key, val in dic.items():
    ls.append((key, val))
ls.sort()
for each in ls:
    print (each[0], each[1])