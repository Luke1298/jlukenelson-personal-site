import math
from collections import Counter
import itertools


CAP = 1500000
#CAP = 100



def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def iscoPrime(a, b):
    return gcd(a, b) == 1



def getUniqueUnderN(N):
    # (m**2-n**2)**2 + (2mn)**2 = (m**2 + n **2)**2
    # => 2m**2 + 2mn <= N
    # => m**2 <= N//2
    # => m <= sqrt(N//2)
    toReturn = []
    for m in range(1, int(math.sqrt(N) + 100)):
        for n in range(1, m):
            if (m%2 == 1) and (n%2==1):
                pass
            elif iscoPrime(m, n):
                an = sum(((m**2 - n**2), (2*m*n), (m**2 + n**2)))
                #toReturn.append(tuple(sorted(((m**2 - n**2), (2*m*n), (m**2 + n**2)))))
                if an < CAP:
                    toReturn.append(an)
    return toReturn


a = sorted(getUniqueUnderN(CAP))

sol = {}
keys = set()

for l in sorted(getUniqueUnderN(CAP)):
    for k in range(l, CAP, l):
        if k not in keys:
            keys.add(k)
            sol[k] = 1
        else:
            sol[k] = 0

print(sum(sol.values()))
