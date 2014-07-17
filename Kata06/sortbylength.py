#/usr/bin/python

import json

f = open("wordlist.txt", "r")
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort(key=len)

o = open("wordlistsorted.txt","w")
for item in lines:
    o.write(item.lower())

length = 1
pos = 0

lengtharr = [0]

for item in lines:
    pos+=1
    if(len(item)-1 > length):
        lengtharr.append(pos)
        length +=1
    
print lengtharr
with open("lengths.txt","w") as outfile:
    json.dump(lengtharr,outfile)