# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:10:56 2016

@author: kuangyiyun
"""

import urllib.request
#import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
try:
    request = urllib.request(url)
    response = urllib.request.urlopen(request)
    print (response.read())
except urllib.errer, e:
    if hasattr(e,"code"):
        print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)