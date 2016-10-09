# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:58:17 2016

@author: kuangyiyun
"""

#Exercise 8.1
item = ['a', 'b', 'c', 'd', 'e']

def chop(item):
    del item[0]
    del item[len(item)-1]

chop(item)
print (item)

def middle(item):
    del item[0]
    del item[len(item)-1]
    return item
    
item = ['a', 'b', 'c', 'd', 'e']
print (middle(item))