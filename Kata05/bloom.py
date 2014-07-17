#!/usr/bin/python

# Bitstring, size and speed efficient arrays for bools and bits
# https://pythonhosted.org/bitstring/index.html
# This python script takes the 3.5MB large wordlist.txt file and
# creates a bloomfilter of size 125kB for lookup. 

import hashlib
import time
import math
from bitstring import Bits, BitArray, BitStream

# Start for measuring time. (time more accurate on OS X, clock on windows.)
start = time.time()
file = open("wordlist.txt","r")

#Create the container for the hashbools
hashTable = BitArray(1000000)
modValue = 1000000


#read each line, split to remove extra chars.
for line in file.readlines():
    data = line.split()
    for line in data:
        #hash with the md5 hashfunction.
        hash = hashlib.md5(line.lower().encode('utf-8')).digest()
        #extract parts of the hash and convert to integer inside array index span 
        h1 = int(hash[0:3].encode("hex"),16)%modValue
        h2 = int(hash[4:7].encode("hex"),16)%modValue
        h3 = int(hash[8:11].encode("hex"),16)%modValue
        h4 = int(hash[12:15].encode("hex"),16)%modValue
        #set the bits in the array. use the set function for speed.
        hashTable.set(True,h1)
        hashTable.set(True,h2)
        hashTable.set(True,h3)
        hashTable.set(True,h4)

file.close()	

#open file as binary file and write to it.
with open('data', 'wb') as outfile:
    hashTable.tofile(outfile)

#print execution time. ~20 seconds on my system
end = time.time()
print(end-start)

