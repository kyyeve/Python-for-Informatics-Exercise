#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:20:42 2016

@author: kuangyiyun
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = raw_input('Enter the website: ')

try:
    host_name = url.split("/")[2]
    mysock.connect((host_name,80))
    mysock.send('GET ' + url + ' HTTP/1.0\n\n')
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print data
    mysock.close()
    
except:
    print 'wrong website!'