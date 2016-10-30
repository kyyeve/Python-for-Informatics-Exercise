#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:56:49 2016

@author: kuangyiyun
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
file = ""
while True:
    data = mysock.recv(512)
    if (len(data))<1: break 
    file = file + data
    
mysock.close()
pos = file.find("\r\n\r\n")
file = file[pos+4:]
print file