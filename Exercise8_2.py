# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:33:06 2016

@author: kuangyiyun
"""

#Exercise 8.2
"""  Example in the book
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) ==0: continue
    if words[0] != 'From': continue
    print (words[2])
"""

fhand = open('mbox-short-2.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) ==0: continue
    if words[0] != 'From': continue
    if len(words) < 3: continue   #if after from there is no text
    print (words[2])
