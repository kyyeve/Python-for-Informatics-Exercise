# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:23:14 2016

@author: kuangyiyun
"""

#Exercise 9.3
fname = 'mbox-short.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    line = line.rstrip('\n')
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        #day = words[1]
        """if day in dic:
            dic[day] += 1
        else:
            dic[day] = 1"""
        dic[words[1]] = dic.get(words[1], 0) + 1
            
print (dic)