#!/usr/bin/python

import json
import time
import hashlib
from bitstring import Bits, BitArray, BitStream

start = time.clock()

modValue = 1000000
with open('data', 'r') as infile:
	hashTable = Bits(infile)

infile.close()	

wordcount = 0
errors = 0

testfile = open("test.txt","r")

for line in testfile.readlines():
    data = line.split()
    for line in data:
        hash = hashlib.md5(line.lower().encode('utf-8')).digest()
        h1 = int(hash[0:3].encode("hex"),16)%modValue
        h2 = int(hash[4:7].encode("hex"),16)%modValue
        h3 = int(hash[8:11].encode("hex"),16)%modValue
        h4 = int(hash[12:15].encode("hex"),16)%modValue
        if(hashTable[h1] and hashTable[h2] and hashTable[h3] and hashTable[h4]):
            wordcount +=1
        else:
            wordcount +=1
            errors += 1
            print "%s was spelled incorrectly"%line

end = time.clock()
print(end-start)
print("There were %s number of incorrect words reported"%errors)
print("that means atleast %s false positive"%(16-errors))
print("There were a total of %s words checked"%wordcount)