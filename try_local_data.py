# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:03:57 2016

@author: kuangyiyun
"""
import os

#write a file companies.txt
file = open(os.path.expanduser("~/Desktop/RawData/companies.txt"),'w');
file.write("Apple" "\n" "Bond" "\n" "Cienma" "\n" "Double");
file.close();

file = open(os.path.expanduser("~/Desktop/RawData/companies.txt"),'r');
file.read();
#file.close();

#add numbers to each row and save as scompanies.txt
f1 = open(os.path.expanduser("~/Desktop/RawData/companies.txt"));
cNames = f1.readlines();
for i in range(0,len(cNames)):
    cNames[i] = str(i+1) + " " + cNames[i];
f1.close();
f2 = open(os.path.expanduser("~/Desktop/RawData/scompanies.txt"), 'w');
f2.writelines(cNames);
f2.close();

f = open(os.path.expanduser("~/Desktop/RawData/scompanies.txt"), 'a+');
f.read();
f.seek(0,0);
cNames  = f.readlines();
print (cNames);
f.close();