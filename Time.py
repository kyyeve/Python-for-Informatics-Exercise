# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 20:13:48 2016

@author: kuangyiyun
"""

# Time 
import time
ticks = time.time()
print (ticks)

localtime = time.localtime(time.time())
print (localtime)

localtime = time.asctime( time.localtime(time.time()) )
print (localtime)

import calendar

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)