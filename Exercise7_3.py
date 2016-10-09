# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:49:18 2016

@author: kuangyiyun
"""

#Exercise 7.3
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print (fname + "- You have been punk'd!")
    else:
        print ("File cannot be opened: " + fname)
    exit()    #terminate the program
    
count = 0
for line in fhand:
    count += 1
print ("There were " + str(count) + " subject lines in " + fname)