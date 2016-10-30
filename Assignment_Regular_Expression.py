# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 11:52:13 2016

@author: kuangyiyun
"""

"""Assignment: Regular Expression"""
docu = open("regex_sum_262392.txt")
docu = open("regex_sum_42.txt")
result = []
i = 1
for line in docu:
    line = line.strip()
    #print (line)
    numbers = re.findall('[0-9]+', line)
    for item in numbers:
        result.append(item)
    #print (numbers)
    #print (result)
    #i = i + 1
    #if i > 20:
        #break
num_sum = 0
for i in result:
    num_sum = num_sum + int(i)
print (num_sum)
    