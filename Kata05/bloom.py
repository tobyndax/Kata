#!/usr/bin/python

import hashlib
import time
import math
from bitstring import Bits, BitArray, BitStream


start = time.clock()
file = open("wordlist.txt","r")

hashTable = BitArray(1000000)
modValue = 1000000
linenumb = 0

for line in file.readlines():
    data = line.split()
    linenumb += 1
    for line in data:
        hash = hashlib.md5(line.lower().encode('utf-8')).digest()
        h1 = int(hash[0:3].encode("hex"),16)%modValue
        h2 = int(hash[4:7].encode("hex"),16)%modValue
        h3 = int(hash[8:11].encode("hex"),16)%modValue
        h4 = int(hash[12:15].encode("hex"),16)%modValue
        hashTable.set(True,h1)
        hashTable.set(True,h2)
        hashTable.set(True,h3)
        hashTable.set(True,h4)
        #hashTable.set(True,h5)
        #hashTable.set(True,h6)

file.close()	

with open('data', 'wb') as outfile:
    hashTable.tofile(outfile)
  

  
end = time.clock()
print(end-start)

