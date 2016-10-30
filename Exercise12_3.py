#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:38:55 2016

@author: kuangyiyun
"""

import urllib

url = 'http://www.py4inf.com/code/romeo.txt'
fhand = urllib.urlopen(url)
counts = 0
data = fhand.read()
print data[:3000]

for i in data:
        counts += 1
    
print counts