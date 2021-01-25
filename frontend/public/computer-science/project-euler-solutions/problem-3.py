#from Utils.primes import sieve_of_eratosthenes
import math


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
	
prime_factors = []
	
for x in sieve_of_eratosthenes(int(math.sqrt(600851475143))):
	if 600851475143%x ==0:
		prime_factors.append(x)

print max(prime_factors)