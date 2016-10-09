# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:56:56 2016

@author: kuangyiyun
"""

#Exercise 8.6
number = input('Enter a number: ')
ls = []
while number != 'done':
    try:
        number = float(number)
        ls.append(number)
    except:
        print ('Please input correct number!')
    number = input('Enter a number: ')

print ('Maximum: ' + str(max(ls)))
print ('Minimum: ' + str(min(ls)))