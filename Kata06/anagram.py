#!/usr/bin/python
from collections import Counter
import json

def isAnagram2(str1,str2):
    if(str1 == str2):
        return False
    count1 = Counter(str1)
    count2 = Counter(str2)
    if (count1 == count2):
        return True
    else:
        return False
        
wordList = []

f = open("wordlistsorted.txt","r")

for line in f.readlines():
    line = line.strip()
    wordList.append(line)
f.close
f = open("lengths.txt","r")
lengths = json.load(f)

#---------------------------------------------------
# Preloaded parameters done.

def checkAnagram(str1):
    for item in wordList[lengths[len(str1)-1]:lengths[len(str1)]]:
        if(isAnagram2(str1.lower(),item.strip())):
            print item
        
checkAnagram("Arrest")