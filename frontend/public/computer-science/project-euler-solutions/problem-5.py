#from Utils.primes import sieve_of_eratosthenes
import math
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

primes = sieve_of_eratosthenes(20)

def prime_factorize(i):
	sol = []
	while i!=1:
		probable_primes = [p for p in primes if p<=i]
		for p in probable_primes:
			if i%p == 0:
				sol.append(p)
				i /= p
	return Counter(sol)

prime_factors = [prime_factorize(j) for j in range(2, 21)]

sol_dict = {p:1 for p in primes}

for num in prime_factors:
	for key, val in num.items():
		if sol_dict[key] < val:
			sol_dict[key] = val
sol = 1

for p, e in sol_dict.items():
	sol *= p**e
	
print sol