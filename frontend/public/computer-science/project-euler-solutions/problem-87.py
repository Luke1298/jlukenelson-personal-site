#The best approach here is to get limits for the primes and just do combinations
#Not trying to calculate the pair that makes the sum given some number x

#x**2 + y**3 + z**4; x, y, z will represent those numbers to those powers
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



limit = 50000000

max4th = int(math.ceil((limit-(2**2+2**3))**(1./4)))
max3rd = int(math.ceil((limit-(2**2+2**3))**(1./3)))
max2nd = int(math.ceil((limit-(2**3+2**4))**(1./2)))

primes = sieve_of_eratosthenes(max2nd)


sol = set()

for z in filter(lambda t: t<max4th, primes):
    for y in filter(lambda t: t<max3rd, primes):
        for x in filter(lambda t: t<math.ceil(math.sqrt(max(limit - (z**4 + y**3), 0))), primes):
            if z**4+y**3+x**2 < limit:
                sol.add(z**4+y**3+x**2)

print len(sol)
