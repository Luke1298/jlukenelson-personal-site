from itertools import permutations, product
from tqdm import tqdm
import math


CAP = 1000000

amicableDict = {1:1, 2:3}

print "MAKING AMICALBE DICTIONARY"
for n in tqdm(range(2, CAP)):
    factors = set()
    for j in range(1, int(math.sqrt(n))+1):
        if n%j == 0:
            factors.add(j)
            factors.add(n//j)
    amicableDict[n] = sum(factors) - n

cycleDict = {1 : [1]}
amicableDictSet = set(amicableDict.keys())

print "DOING CYCLE DETECTION"
for k in tqdm(range(2, CAP//50)):
    if amicableDict[k] in cycleDict:
        cycleDict[k] = cycleDict[amicableDict[k]]
    else:
        visited = []
        curNode = k
        while curNode not in visited:
            if curNode in cycleDict:
                cycleDict[k] = cycleDict[curNode]
                break
            else:
                visited.append(curNode)
                if curNode in amicableDictSet:
                    curNode = amicableDict[curNode]
                else:
                    curNode = None
                    visited.append(curNode)
        if k not in cycleDict.keys():
            cIndex = visited.index(curNode)
            for t in visited:
                cycleDict[t] = visited[cIndex:]

import pdb; pdb.set_trace()
print min(max(cycleDict.iteritems(), key=lambda x:len(x[1]))[1])
