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

sol = []

for prime in primes:
    is_truncatable = True
    for p in [int(str(prime)[n:]) for n in range(len(str(prime)))] + [int(str(prime)[:n]) for n in range(1, len(str(prime)))]:
        if p not in primes:
            is_truncatable = False
            break;
    if is_truncatable:
        sol.append(prime)
        
print sum(sol[4:])
         