#!/usr/bin/python

#This pythonscript prints out all existing words of a specific size that
#can be created by concatinating two different words of smaller size
#you call makeWordsOfN(size), where size is your specified stringlength.

#In the description below the string length 6 is assumed
#This script uses the very speedy implementation of dictionaries.
#Firstly all the proper words of length 6 are added to a dict.
#Then the presubstrings, i.e, in the word proper, p, pr, pro, prop, porpe are added
# to the preDict. and the same is done for the sufDict but from the back of the string.
#The next step is extracting all proper words of size, for instance, 3 and see if they 
# are a match for the preDict. For every match in the preDict, find all words 
# that are a match for the sufDict. Lastsly return the concatination of the two if
# it can be found in the fullDict.

from collections import defaultdict

l = 6

fullDict = defaultdict(set)
preDict = defaultdict(set)
sufDict = defaultdict(set)
newWords = defaultdict(set)

def wordsOfLength(n):
    words = [w.strip().lower() for w in open('wordlist.txt') if len(w)-1 == n if "'" not in w]
    return words

def makeDictN(n):
    global fullDict,preDict,sufDict
    fullDict.clear()
    preDict.clear()
    sufDict.clear()
    for word in wordsOfLength(n):
        key = word
        fullDict[key].add(key)
        for p in range(1,n):
        
            preKey = word[0:p]
            sufKey = word[p:n]
        
            preDict[preKey].add(preKey)
            sufDict[sufKey].add(sufKey)

def makeWords(n,k):
    words1 = wordsOfLength(n)
    words2 = wordsOfLength(k)
    makeDictN(n+k)
    for w in words1:
        if w in preDict:
            word= [w+w2 for w2 in words2 if w2 in sufDict if w+w2 in fullDict]
            for p in word:
                if not p in newWords:
                    newWords[p] = p
                  
def makeWordsOfN(n):  
    for l in range(1,n):
        makeWords(l,n-l)
    
makeWordsOfN(6)
print(' '.join(newWords))
