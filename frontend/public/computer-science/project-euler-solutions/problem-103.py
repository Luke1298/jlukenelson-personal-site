import numpy as np
import math
from collections import Counter
import itertools
import os
import sys
import re

import itertools

def powerSet(arr):
    """returns a list of all subsets of a list"""

    combs = []
    for i in xrange(0, len(arr)+1):
        listing = [list(x) for x in itertools.combinations(arr, i)]
        combs.extend(listing)
    return combs

def isValid(l):
    allSubsets = powerSet(l)
    subsetSumsSet = set(map(sum, allSubsets))
    if len(allSubsets) != len(subsetSumsSet):
        return False
    else:
        allSubsetsByLen = {i : filter(lambda x: len(x)==i, allSubsets) for i in range(len(l)+1)}
        for k in range(len(l)):
            if max(map(sum, allSubsetsByLen[k]) + [0]) > min(map(sum, allSubsetsByLen[k+1])):
                return False
    return True

possibilities = []

for a_1 in range(31, 45):
    lToTryBase = [20, a_1]
    for comb in itertools.combinations(range(a_1, 55), 5):
        lToTry = lToTryBase + list(comb)
        if isValid(lToTry):
            print lToTry
            possibilities.append(lToTry)
print "".join(map(str, min(possibilities, key=sum)))
print isValid([20,31,38,39,40,42,45])
