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

primes = sieve_of_eratosthenes(10000000)

def prime_factorize(i):
	sol = []
	while i!=1:
		probable_primes = [p for p in primes if p<=i]
		for p in probable_primes:
			if i%p == 0:
				sol.append(p)
				i /= p
	return Counter(sol)
	
def count_factors(k):
	prime_factors = prime_factorize(k)
	sol = 1
	for val in prime_factors.values():
		sol *= (val+1)
	return sol
	
print count_factors(9)
	
tri_numbers = [1, 3]

def tri_numbers():
	i, num = 1, 1
	while True:
		yield num
		i+=1
		num += i
		
sol_tri_gen = tri_numbers()

sol = sol_tri_gen.next()

while count_factors(sol) < 500:
	print sol, count_factors(sol)
	sol = sol_tri_gen.next()
	
print sol