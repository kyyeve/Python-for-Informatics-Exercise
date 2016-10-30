# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:23:38 2016

@author: kuangyiyun
"""

#dic = dict(zip(keys,values))
import pandas as pd
from pandas import Series

aSer = Series([1,2.0,'a'])
bSer = Series(['apple','banana','orange'],index = [1,2,3])

data = {'a':1, "b":2, "c":3}
sindex = ['a','b','c','d']
cSer = Series(data, index = sindex)

data = 