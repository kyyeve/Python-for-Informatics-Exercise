# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:58:59 2016

@author: kuangyiyun
"""

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = 'http://www.dr-chuck.com/page1.htm'
#url = 'http://www.py4inf.com/book.htm'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

"""tags = soup('a')
for tag in tags:
    print tag.get('href', None)"""
    
# Retrieve all of the anchor tags
total = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    print ('TAG:',tag)
    print ('URL:',tag.get('href', None))
    print ('Contents:',tag.contents[0])
    print ('Attrs:',tag.attrs)
    try:
        total += float(tag.contents[0])
        count += 1
    except:
        continue
    
print count, total  