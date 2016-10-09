# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:28:30 2016

@author: kuangyiyun
"""

#Exercise 9.5
fname = 'mbox-short.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    line = line.rstrip('\n')
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        add = words[1].split('@')[1]
        #print (add)
        dic[add] = dic.get(add, 0) + 1
            
print (dic)