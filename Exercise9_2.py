# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:14:33 2016

@author: kuangyiyun
"""

#Exercise 9.2
fname = 'mbox-short.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    line = line.rstrip('\n')
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        day = words[2]
        """if day in dic:
            dic[day] += 1
        else:
            dic[day] = 1"""
        dic[words[2]] = dic.get(words[2], 0) + 1
            
print (dic)