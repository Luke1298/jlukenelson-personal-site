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

CAP = 1000000

primes = sieve_of_eratosthenes(CAP//1000)

sol = 1

p=0
while sol*primes[p] < CAP:
	sol *= primes[p]
	p += 1

print(sol)
