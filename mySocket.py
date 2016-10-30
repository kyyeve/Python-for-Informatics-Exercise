# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 18:34:24 2016

@author: kuangyiyun
"""
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com', 80))
mysocket.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print (data.decode("utf-8"))
#utf-8 there is ht format of string
mysocket.close()

"""import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data);

mysock.close()"""