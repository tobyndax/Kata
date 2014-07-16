import hashlib
import time
import math
import json

start = time.clock()
file = open("wordlist.txt","r")

hashTable = [0]*1000001
modValue = 1000000

linenumb = 0

for line in file.readlines():
	hash = hashlib.md5(line.encode('utf-8')).digest()
	h1 = int.from_bytes(hash[0:3],byteorder='big')%modValue
	h2 = int.from_bytes(hash[4:7],byteorder='big')%modValue
	h3 = int.from_bytes(hash[8:11],byteorder='big')%modValue
	hashTable[h1] = 1;
	hashTable[h2] = 1;
	hashTable[h3] = 1; 
	linenumb += 1
	if(linenumb == 189300):
		print(line),
		print(" has the hashnumbers")
		print("%s %s %s"%(h1,h2,h3))
	
file.close()	

with open('data.txt', 'w') as outfile:
  json.dump(hashTable, outfile, ensure_ascii=False)
outfile.close()
  
end = time.clock()
print(end-start)



