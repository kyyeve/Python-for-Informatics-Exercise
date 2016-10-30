# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 17:02:18 2016

@author: kuangyiyun
"""

import urllib.request

img = urllib.request.urlopen('http://www.py4inf.com/cover.jpg').read()
fhand = open('cover.jpg', 'w')
fhand.write(str(img))
fhand.close()