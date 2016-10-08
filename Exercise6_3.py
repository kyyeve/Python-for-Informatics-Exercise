# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:41:10 2016

@author: kuangyiyun
"""

#Exercise 6.3
word = "banana"
match = 'b'

def counter(word, match):
    count = 0
    for letter in word:
        if letter == match:
            count += 1
    print (count)

counter(word, match)