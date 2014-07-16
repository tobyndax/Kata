import json
import time
import hashlib

start = time.clock()

modValue = 1000000

with open('data.txt', 'r') as infile:
	hashTable = json.load(infile)

infile.close()	
end = time.clock()

print(end-start)

testfile = open("test.txt","r")

test = "knew"

item = test
hash = hashlib.md5(item.encode('utf-8')).digest()
h1 = int.from_bytes(hash[0:3],byteorder='big')%modValue
h2 = int.from_bytes(hash[4:7],byteorder='big')%modValue
h3 = int.from_bytes(hash[8:11],byteorder='big')%modValue
print("%s %s %s"%(hashTable[h1], hashTable[h2], hashTable[h3]))
if(hashTable[h1] and hashTable[h2] and hashTable[h3]):
	print("Yay, maybe nay")
else:
	print("okay...")

# for line in testfile.readlines():
	# data = line.split()
	# for item in data:
		# hash = hashlib.md5(item.encode('utf-8')).digest()
		# h1 = int.from_bytes(hash[0:3],byteorder='big')%modValue
		# h2 = int.from_bytes(hash[4:7],byteorder='big')%modValue
		# h3 = int.from_bytes(hash[8:11],byteorder='big')%modValue
		# if(hashTable[h1] and hashTable[h2] and hashTable[h3]):
			# print()
			#print("The word %s is correct" %item)
		# else: 
			# print("The word %s is incorrect" %item)