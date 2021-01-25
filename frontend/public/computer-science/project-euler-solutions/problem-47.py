from collections import Counter

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
    
    
primes = sieve_of_eratosthenes(1000000)

def _primeFactorize(n):
    if n in primes:
        return [n]
    else:
        for p in primes:
            if n%p==0:
                return [p] + _primeFactorize(n/p)
                
def primeFactorize(n):
    factorization = []
    for key, item in Counter(_primeFactorize(n)).items():
        factorization.append((key, item))
    return factorization
    
currNumConcecutive = 0
desiredNumConcecutive = 4
num_identical = 4
n = 2

while currNumConcecutive!=desiredNumConcecutive:
    if len(primeFactorize(n)) == num_identical:
        print n, currNumConcecutive
        currNumConcecutive+=1
    else:
        currNumConcecutive = 0
    n+=1
print n - desiredNumConcecutive