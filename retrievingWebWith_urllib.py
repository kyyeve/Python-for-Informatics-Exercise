# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:32:36 2016

@author: kuangyiyun
"""

import urllib.request
from bs4 import BeautifulSoup

#url = input('Enter - ')
#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://python-data.dr-chuck.net/known_by_Lorcan.html'
fhand = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(fhand)
tags = soup('a')


position = int(input('Position -'))
count = input('Count - ')
print (url)

i = 1
while i <= int(count):
    print (tags[position-1].get('href', None))
    url = tags[position-1].get('href', None)
    fhand = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(fhand)
    tags = soup('a')
    i += 1

"""
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
"""