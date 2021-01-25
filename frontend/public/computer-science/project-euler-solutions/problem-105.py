import numpy as np
import math
from collections import Counter
import itertools
import os
import sys
import re

import itertools

scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p105_sets.txt")

file = open(src_filename, "r")

src = file.read()



allLines = [k for k in src.split("\n")]
allInputs = map(lambda l: map(int, l.split(",")), allLines)

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

validInputs = filter(isValid, allInputs)

print sum(map(sum, validInputs))
