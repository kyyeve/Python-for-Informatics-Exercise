# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:00:04 2016

@author: kuangyiyun
"""

#Exercise 10.3
fname = 'mbox-short.txt'
fhand = open(fname)
dic = {}
for line in fhand:
    line = line.rstrip('\n')
    for words in line.split():
        for word in words:
            for letter in word.lower():
                if letter.isalpha():
                    dic[letter] = dic.get(letter,0)+1
#print (dic)
      
ls = []
for key, val in dic.items():
    ls.append((val, key))
ls.sort(reverse = True)
for each in ls:
    print (each[1], each[0])