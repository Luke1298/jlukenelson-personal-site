import numpy as np

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
	
def is_prime(n):
	if n < 0:
		n = -1 * n
	if n == 2:
		return True
	for i in range(2, int(np.sqrt(n) +1)):
		if (n % i) == 0:
			return False
	return True
	
#print is_prime(11)
#primes = sieve_of_eratosthenes(10000000)

b_list = sieve_of_eratosthenes(1000)

a_list = [i for i in range(-1000, 1001)]

f = lambda a: lambda b: lambda n: n**2 + a*n + b

sol_dict = {}

for b in b_list:
	for a in a_list:
		i = 0
		f_n = f(a)(b)
		while is_prime(f_n(i)):
			i+=1
		sol_dict[i] = (a,b)
		
sol_tup = sol_dict[max(sol_dict.keys())]

print sol_tup[0] * sol_tup[1]