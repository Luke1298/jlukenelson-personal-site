import itertools
import re
import copy
import sys


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
            primes.append(str(i))
    return primes

primes = sieve_of_eratosthenes(10000000)   

primeGroupedByDigits = [[prime for prime in primes if len(prime) == i] for i in range(1, 8)]

#print primeGroupedByDigits

def maxFromDash(s, digits):
    primes = primeGroupedByDigits[len(s)-1]
    for i in digits:
        s[s.index("-")] = i
    s = "".join(s)
    family = [s.format(t) for t in range(10) if s.format(t) in primes]
    return family
    #print s.format("1")
    


for group in primeGroupedByDigits:
    for n in range(1, len(str(group[0]))+1):
        for combination in list(itertools.combinations(range(len(str(group[0]))), n)):
            formatString = ["-"]*len(str(group[0]))
            for c in combination:
                formatString[c] = "{0}"
            #formatString = "".join(formatString)
            #print formatString
            for i in range(1, 10**formatString.count("-")):
                if len(str(i)) < formatString.count("-"):
                    i = "0" * (formatString.count("-")-len(str(i))) + str(i)
                i = str(i)
                family = maxFromDash(copy.copy(formatString), i)
                if len(family) == 7:
                    print family    
                if len(family) == 8:
                    print family 
                    sys.exit()
                