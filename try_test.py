# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:54:00 2016

@author: kuangyiyun
"""

#random numbers
"""import random
for i in range(10):
    x = random.random()
    print (x)
t = [1,2,3]
print (random.choice(t))"""

#math function
"""import math
print (math)"""

#function
"""def print_lyrics():
    print ("I'm a lumberjack, and I am okay.")
    print ("I sleep all night and I work all day.")

print_lyrics()"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data.decode("utf-8"));

mysock.close()

