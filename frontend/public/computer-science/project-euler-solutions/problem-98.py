import numpy as np
import math
from collections import Counter
import os
import sys
import re

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p098_words.txt")

file = open(src_filename, "r")

src = file.read()



allWords = [k for k in src.split("\",\"")]
allWords[0] = allWords[0][1:]
allWords[-1] = allWords[-1][:-1]


counterMap = [Counter(word) for word in allWords]

anagrams = []

for k in range(len(counterMap)):
    for j in range(k):
        if counterMap[k] == counterMap[j]:
            anagrams.append((allWords[k], allWords[j]))

print anagrams

maxDigitLen = len(max(anagrams, key=lambda x: len(x[1]))[0])
sqrs = [x**2 for x in range(1, int(10**(maxDigitLen/2.))+1)]
sqrsByLen = {i : filter(lambda x: len(str(x)) == i, sqrs) for i in range(1, maxDigitLen+1)}
print sqrsByLen

print maxDigitLen

def getPostior(word1, word2, num):
    strNum = str(num)
    theMap = {word1[k] : strNum[k] for k in range(len(word1))}
    return int("".join([theMap[c] for c in word2]))

ans = []

for j in range(len(anagrams)):
    word1 = anagrams[j][0]
    word2 = anagrams[j][1]
    for sqr in sqrsByLen[len(word1)]:
        if getPostior(word1, word2, sqr) in sqrsByLen[len(word1)]:
            ans.append(sqr)
            ans.append(getPostior(word1, word2, sqr))
            print word1, word2, sqr, getPostior(word1, word2, sqr)

print max(filter(lambda x: max(Counter(str(x)).values())<=1, ans))
