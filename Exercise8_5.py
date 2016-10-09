# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:51:53 2016

@author: kuangyiyun
"""

#Exercise 8.5
fname = 'mbox-short.txt'
fhand = open(fname)
count = 0
for line in fhand:
    words = line.split()
    if len(words) >1 and words[0] == 'From':
        count += 1
        print (words[1])

print ('There were ' + str(count) + ' lines in the file with From as the first word')
        