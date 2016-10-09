# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 23:35:10 2016

@author: kuangyiyun
"""

#Exercise 7.2
fname = 'mbox-short.txt'
fhand = open(fname)

total = 0
count = 0
for line in fhand:
    line = line.strip('\n')
    if line.startswith('X-DSPAM-Confidence:'):
        total +=float(line[line.find(':')+1:])
        count += 1

print ('Average spam confidence: ' + str(total/float(count)))