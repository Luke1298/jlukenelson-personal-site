from itertools import chain, cycle, count
from functools import wraps, reduce
import operator
from collections import Counter
import math
import random

def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes

CAP = 12000

CAP*=2

primes = sieve_of_eratosthenes(CAP)

def memoize(func):
    memo = {}

    @wraps(func)
    def memoizer(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return memoizer


@memoize
def getIntegersThatProduct(n):
    if n in primes:
        return set([ (n, ) ])
    else:
        toReturn = set()
        oldReturn = set()
        for j in range(2, int(math.sqrt(n))+1):
            if n%j == 0:
                toReturn.add((j, n//j))
        while toReturn != oldReturn:
            oldReturn = toReturn.copy()
            for el in toReturn.copy():
                for k in getIntegersThatProduct(el[-1]):
                    toReturn.add(tuple(sorted(list(el[:-1]) + list(k))))
        return toReturn


sol = {}

for t in range(2, CAP):
    sol[t] = float('inf')

solKeys = set(sol.keys())

for c in range(2, CAP+1):
    for pair in getIntegersThatProduct(c):
        index = len(pair) + (c-sum(pair))
        if index in solKeys and sol[index]>c:
            sol[index] = c

ans = {k: v for k, v in sol.items() if k<=(CAP//2)}

print(sum(set(ans.values())))
