# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:00:07 2016

@author: kuangyiyun
"""

#Exercise 5.2
maximum = None
minimum = None
while True:
    i = input('Enter a number: ')
    if i == 'done':
        break
    else:
        try:
            i = int(i)
            if maximum == None and minimum == None:
                maximum = i
                minimum = i
            elif maximum < i:
                maximum = i
            elif minimum > i:
                minimum = i
        except:
            print ("Invalid input")

print (maximum, minimum)
    