# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:24:56 2016

@author: kuangyiyun
"""

#Exercise 9.4
fname = 'mbox-short.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    line = line.rstrip('\n')
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        dic[words[1]] = dic.get(words[1], 0) + 1
            
max_add = ''
max_count = 0

for key in dic:
    if max_count < dic[key]:
        max_add = key
        max_count = dic[key]
        
print (max_add + ' ' + str(max_count))