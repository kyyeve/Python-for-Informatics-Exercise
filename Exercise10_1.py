# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:30:39 2016

@author: kuangyiyun
"""

#Exercise 10.1
fname = 'mbox-short.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    line = line.rstrip('\n')
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        dic[words[1]] = dic.get(words[1], 0) + 1

ls = []
for key, val in dic.items():
    ls.append((val, key))
    
ls.sort(reverse = True)
print (ls[0][1], ls[0][0])