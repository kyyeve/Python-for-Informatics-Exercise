# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:51:24 2016

@author: kuangyiyun
"""

#Exercise 6.5
info = "X-DSPAM-Confidence: 0.8475"
start = info.find(':')
print (float(info[start+1:]))