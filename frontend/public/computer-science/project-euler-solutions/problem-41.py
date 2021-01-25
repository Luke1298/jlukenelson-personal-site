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

def is_N_pandigital(num):
    num = str(num)
    N = len(num)
    return set([int(i) for i in num]) == set(range(1, N+1))
    

sieve2 = filter(is_N_pandigital, primes)

print max(seive2)