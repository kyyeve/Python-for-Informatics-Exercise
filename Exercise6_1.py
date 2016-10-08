# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:21:21 2016

@author: kuangyiyun
"""

#Exercise 6.1
usrstring = "abcde"

def backwards(usrstring):
    index = len(usrstring)
    while index > 0:
        letter = usrstring[index - 1]
        print (letter)
        index = index - 1

backwards(usrstring)