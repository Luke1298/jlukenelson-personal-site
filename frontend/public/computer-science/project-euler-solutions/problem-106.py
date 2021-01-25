import numpy as np
import math
from collections import Counter
import itertools
import os
import sys
import re

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

#Because of the increaseing property of the list we can gaurntee that the following is not allowed
def isGreaterThan(s, x):
    s = sorted(s)
    x = sorted(x)
    return all([s[t] < x[t] for t in range(len(s))])

def countEmptyOverlap(s, l):
    toReturn = filter(lambda x: (len(s.intersection(x))==0 and len(s) == len(x) and len(s)>1), l)
    return len(filter(lambda x: not(isGreaterThan(s, x)), toReturn))

def calcCombos(arr):
    c = 0
    pSet = powerSet(arr)[1:]
    pSetCopy = pSet[:]
    for e, s in enumerate(pSet):
        c += countEmptyOverlap(set(s), map(set, pSet[e:]))
    return c


for t in range(3, 13):
    print t, calcCombos(range(t))
