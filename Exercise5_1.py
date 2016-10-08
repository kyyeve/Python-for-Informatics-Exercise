# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:30:09 2016

@author: kuangyiyun
"""
#Exercise 5.1
total = 0
count = 0

while True:
    i =input("Enter a number: ")
    if i == "done":
        break
    else:
        try:
            total += int(i)
            count += 1
        except:
            print ("Invalid input")
print (total, count, float(total)/count)