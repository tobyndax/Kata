#!/usr/bin/python
import hashlib
import math

testfile = open("test.txt","r")
wordfile = open("wordlist.txt","r")
modValue = 1000000

for line in testfile.readlines():
    data = line.split()
    for line in data:
        hash = hashlib.md5(line.encode('utf-8')).digest()
        h1 = int(hash[0:3].encode("hex"),16)%modValue
        if(line == "Sherlock"):
            print"The length of %s in the testfile is %s and has H1 = %s"%(line,len(line),h1)
for line in wordfile.readlines():
    data = line.split()
    for line in data:
        hash = hashlib.md5(line.encode('utf-8')).digest()
        h1 = int(hash[0:3].encode("hex"),16)%modValue
        if(line == "Sherlock"):
            print"The length of %s in the wordfile is %s and has H1 = %s"%(line,len(line),h1)
    
