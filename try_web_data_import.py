# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:19:21 2016

@author: kuangyiyun
"""

#import web data 
#import urllib.request as ur

# this is to aviod verfication error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#import urllib
#s = ur.urlopen("http://www.google.com")
#s = ur.urlopen("https://sg.finance.yahoo.com/q?s=EURUSD=X")
#html = s.read()
#print(html)

from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd

today = date.today()
start = (today.year-1, today.month,today.day)
quotes = quotes_historical_yahoo_ochl('CCOJY',start, today)
df = pd.DataFrame(quotes)
print (df)
#output: 日期 开盘 收盘 最高 最低 成交量
