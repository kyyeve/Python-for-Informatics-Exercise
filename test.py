# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 23:45:53 2016

@author: kuangyiyun
"""
#Reglar Expression
import re

#re.search()
#re.findall()
#method 1: Use String
"""hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    if line.find('From:') >= 0:
        print (line)
#method 2: Use Regular Expression
for line in hand:
    line = line.strip()
    if re.search('From:', line):
        print (line)"""
     
#method 1: Use String
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    if line.startswith('From:'):
        print (line)
#method 2: Use Regular Expression
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    if re.search('^From:', line):
        print (line)