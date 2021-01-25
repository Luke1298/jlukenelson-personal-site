def rotate(string, k):
    k = k % len(string)
    return string[k:] + string[:k]

def get_rotation_group(prime):
    return list(set([int(rotate(str(prime), k)) for k in range(len(str(prime)))]))

def sol_sieve(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
            rotation_group = get_rotation_group(start)
            all_prime = True
            for num in rotation_group:
                if not sieve[num]:
                    all_prime = False
                    break;
            if not all_prime: 
                for num in rotation_group:
                    sieve[num] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes

   
print sol_sieve(100)
sol = set(sol_sieve(1000000) + sol_sieve(100000) + sol_sieve(10000) + sol_sieve(1000) + sol_sieve(100))
print sol
print len(sol)