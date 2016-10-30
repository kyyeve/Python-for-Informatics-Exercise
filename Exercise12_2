#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:34:07 2016

@author: kuangyiyun
"""

import socket

#url = raw_input("Enter url: ")
url = 'http://www.py4inf.com/code/romeo.txt'
try:
    host_name = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    mysock.send('GET ' + url + ' HTTP/1.0\n\n')
    count = 0
    while True:
        data = mysock.recv(512)
        count += len(data)
        if (len(data) < 1) or count >= 3000:
            break
        print data
    mysock.close()
    print count

except:
    print "Wrong URL"



