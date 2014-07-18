#!/usr/bin/python

import itertools
import json

thresh = 8
words = [w.rstrip() for w in open('wordlistsorted.txt')]

def anagramLow(word):
    global words
    
    words = set([w for w in words if len(w) == len(word)])

    comb = set([ ''.join(w) for w in itertools.permutations(word,len(word))])

    return comb.intersection(words)
    
def anagramHigh(word):
    global words
    sword = sorted(word)
    return [w for w in words if w != word if sorted(w) == sword ]
    
    
    
def anagram(word):
    global thresh
    if(len(word) > thresh):
        return anagramHigh(word)
    else:
        return anagramLow(word)
     
        
f = open("lengths.txt")
length = json.load(f)
print length
f.close()

for w in words[length[17]:length[18]]:
    s = anagram(w)
    if(len(s) > 0):
        print "%s is anagram for %s "%(s,w)
        