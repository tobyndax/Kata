#!/usr/bin/python

import itertools

def anagrams(word):
    words = [w.rstrip() for w in open('wordlist.txt')]
    
    words = set([w for w in words if len(w) == len(word)])

    comb = set([ ''.join(w) for w in itertools.permutations(word,len(word))])

    return comb.intersection(words)
    
s = anagrams('wordeewwr')
if(len(s) != 0):
    print s