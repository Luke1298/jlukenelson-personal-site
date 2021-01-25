import os
import sys
import numpy as np
from collections import Counter
from itertools import combinations



numchoices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def twoDigitCombos(l, r):
    toReturn = []
    for nl in l:
        for nr in r:
            #15^6 == 9 and 15^9 == 6
            if (nl==6 or nl==9):
                toReturn.append(int(str(15^nl) + str(nr)))
                toReturn.append(int(str(nr) + str(15^nl)))
            if (nr==6 or nr==9):
                toReturn.append(int(str(nl) + str(15^nr)))
                toReturn.append(int(str(15^nr) + str(nl)))
            toReturn.append(int(str(nl) + str(nr)))
            toReturn.append(int(str(nr) + str(nl)))
    return set(toReturn)

def canDisplaySquares(l, r):
    return all([sq in twoDigitCombos(l, r) for sq in [1, 4, 9, 16, 25, 36, 49, 64, 81]])

print canDisplaySquares((0, 5, 6, 7, 8, 9), (1, 2, 3, 4, 8, 9))

print twoDigitCombos((0, 5, 6, 7, 8, 9), (1, 2, 3, 4, 8, 9))

i = 0
allSolutions = set()

for l in list(combinations(numchoices, 6)):
    for r in list(combinations(numchoices, 6)):
        if canDisplaySquares(l, r):
            allSolutions.add(frozenset((frozenset(l), frozenset(r))))
print len(allSolutions)
