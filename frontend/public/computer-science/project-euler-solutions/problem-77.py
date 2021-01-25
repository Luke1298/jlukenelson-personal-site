def sol(coin_types, to_make):
	sol_list = [0]*(to_make+1)
	for type in coin_types:
		sol_list[type] += 1
		for i in range(type, len(sol_list)):
			sol_list[i] += sol_list[i-type]
	return sol_list

CAP = 100

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

primes = sieve_of_eratosthenes(CAP)


#coin_types = [1, 2, 5, 10, 20, 50, 100, 200]
print sorted(filter(lambda x: x[1]>5000, map(lambda x:(x[0], x[1]), enumerate(sol(primes, CAP)))))[0]#+1
