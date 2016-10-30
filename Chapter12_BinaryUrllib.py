#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:21:14 2016

@author: kuangyiyun
"""

#Reading Binary Files using urllib

import urllib
img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
fhand = open('cover.jpg', 'w')

#Only works for small file
#fhand.write(img)

#retrieve data by blocks
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1 : break
    size = size + len(info)
    fhand.write(info)

print size, 'charaters copied.'
fhand.close()

