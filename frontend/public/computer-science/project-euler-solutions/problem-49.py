
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

    
primes = [p for p in sieve_of_eratosthenes(10000) if p > 1000]

difference = 1000

def useSameDigits(i1, i2):
    s1 = str(i1)
    s2 = str(i2)
    if len(s1)==len(s2) and set(s1) == set(s2):
        return True
    return False
        

while difference < 9999:
    for prime in primes:
        p1, p2, p3 = prime, prime + difference, prime + 2*difference
        if useSameDigits(p1, p2) and useSameDigits(p1, p3) and p2 in primes and p3 in primes:
            print p1, p2, p3
    difference += 1  
        