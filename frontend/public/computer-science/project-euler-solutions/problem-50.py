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
    
def get_biggest_consecutive_sum(prime):
    starting = 0
    ending = 0
    while sum(primes[starting:ending]) != prime:
        while sum(primes[starting:ending]) <= prime:
            if sum(primes[starting:ending]) == prime:
                return primes[starting:ending]
            ending +=1
        starting += 1
    return primes[starting:ending]
    
current_record = 0
best_prime = 0
smallest_prime = 0
    
for prime in primes[::-1]:
    if prime < smallest_prime:
        break
    consecutive = len(get_biggest_consecutive_sum(prime))
    if current_record < consecutive:
        current_record = consecutive
        best_prime = prime
        smallest_prime = sum(primes[:consecutive])


print best_prime