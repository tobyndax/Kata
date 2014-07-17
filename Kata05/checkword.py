#!/usr/bin/python
# Bitstring, size and speed efficient arrays for bools and bits
# https://pythonhosted.org/bitstring/index.html
# This python script takes the 125 kB large BloomFilter created by bloom.py
# and uses it for lookup of words.
# Assuming the test.txt included is used the program also reports how many 
# errors and how many falsepositives that was generated during runtime.
 
import time
import hashlib
from bitstring import Bits, BitArray, BitStream

#Measuring execution time.
start = time.time()

#Modvalue, same as used when creating the hashtable in bloom.py
modValue = 1000000

#Read in the binary datafile
with open('data', 'r') as infile:
	hashTable = Bits(infile)
infile.close()	


wordcount = 0
errors = 0

#Testfile, extract from Sherlock Holmes if using the included test.txt
testfile = open("test.txt","r")


for line in testfile.readlines():
    data = line.split()
    for line in data:
        
        #Calculate the hashes. Same as in bloom.py.
        hash = hashlib.md5(line.lower().encode('utf-8')).digest()
        h1 = int(hash[0:3].encode("hex"),16)%modValue
        h2 = int(hash[4:7].encode("hex"),16)%modValue
        h3 = int(hash[8:11].encode("hex"),16)%modValue
        h4 = int(hash[12:15].encode("hex"),16)%modValue
        
        #If all the hashes result in a hit, the word is deemed to be correct.
        #This has a chance of being incorrect. 
        #http://en.wikipedia.org/wiki/Bloom_filter has a decent explanation of 
        #the mechanics in progress.
        if(hashTable[h1] and hashTable[h2] and hashTable[h3] and hashTable[h4]):
            wordcount +=1
        else:
            wordcount +=1
            errors += 1
            print "%s was spelled incorrectly"%line

#Print execution time.
end = time.time()
print(end-start)

#Print stats about the words
print("There were %s number of incorrect words reported"%errors)
print("that means atleast %s false positive"%(16-errors))
print("There were a total of %s words checked"%wordcount)