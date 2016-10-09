# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:08:33 2016

@author: kuangyiyun
"""

#Exercise 9.1
fname = 'words.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    for word in line.strip('\n').split():
        if word != '':
            dic[word] = None

usrsearch = input('enter a word to check: ')
print (usrsearch in dic)