# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:31:26 2016

@author: kuangyiyun
"""

#Chapter 12 Examples
#Page 144
"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()
"""

"""
#Page 145
import socket
#import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))
mysock.send(b'GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0
picture = "";
while True:
    data = mysock.recv(512)
    data = data.decode(encoding = "utf-8")
    if (len(data) < 1): 
        break
    #time.sleep(0.25)
    count = count + len(data)
    print (data, len(data), count)
    picture = picture + data
    
mysock.close()

#Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n")
#print ('Hearder length', pos)
#print (picture[:pos])

#Skip past the hearder and save the picture data
#picture = picture[pos+4:]
#fhand = open("stuff.jpg","eb")
#fhand.write(picture)
#fhand.close()
"""

#Page 148
"""
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print line.strip()

counts = dict()
fhand = urllib.urlopen('http://www.py4inf.com/code/remeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print counts
"""

#Page149
import urllib
import re

#url = raw_input('Enter - ')
url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"',html)
for link in links:
    print link