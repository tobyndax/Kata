#!/usr/bin/python

from collections import defaultdict


wordlist = open('wordlist.txt', 'r')
d = defaultdict(set)

for word in wordlist:
    word = word.strip().lower()
    if "'" not in word:
        key = tuple(sorted(word))
        d[key].add(word)

sortedSets = [sorted(x) for x in d.values() if len(x) > 2]
for wordset in sorted(sortedSets):
    print(' '.join(wordset))