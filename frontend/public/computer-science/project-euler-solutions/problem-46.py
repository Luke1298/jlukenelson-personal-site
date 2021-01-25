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

#composite_odds = [2*n+1 for n in range(, 1000000/2 - 1) if 2*n+1 not in primes]
squares = [x**2 for x in range(0, 1001)]

i=1

def supportsConjecture(current_odd):
    for s in [s for s in squares if s < current_odd]:
        for p in [p for p in primes if p <= current_odd]:
            if p + 2*s == current_odd:
                return True
    return False

while True:
    i+=1
    current_odd = 2*i+1
    if not supportsConjecture(current_odd):
        break
print current_odd
    