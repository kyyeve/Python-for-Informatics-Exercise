#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:55:50 2016

@author: kuangyiyun
"""

from BeautifulSoup import *
import urllib

#url = input('Enter URL : ')
#url = 'http://www.dr-chuck.com/page1.htm'
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('p')
c = 0
for tag in tags:
    c += 1
    if len(tag.contents) > 0:
        print tag.contents[0]
    
print c
