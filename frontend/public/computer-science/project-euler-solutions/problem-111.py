import numpy as np

import math

from itertools import permutations, combinations_with_replacement

def get_all_n_length_d_repeated(n, d, i=1):
    ret_list = set()
    poschar = [b for b in combinations_with_replacement([j for j in range(10)], i)]
    sub_list = [str(d)]*(n-i)
    if sub_list.count("0") == n - 1:
        return []
    for char_set in poschar:
        curr_sub_list = sub_list + list(map(str, char_set))
        if curr_sub_list.count("0") < n - 1:
            for k in permutations(curr_sub_list):
                if int(''.join(k)) > pow(10, n-1)-1:
                    ret_list.add(int(''.join(k)))
    return ret_list


def S(n, d): #n is number of n-digit prime d is repeated digit
    def is_prime(i):
        if i == 1:
            return False
        for k in range(2, int(math.ceil(math.sqrt(i)))+1):
            if i % k == 0:
                return False
        return True
    N = [p for p in get_all_n_length_d_repeated(n, d) if is_prime(p)]
    i = 1
    while not N:
        N = [p for p in get_all_n_length_d_repeated(n, d, i) if is_prime(p)]
        i +=1
    print(d, N)
    return N



if __name__ == '__main__':
    #VERIFY:
    #ten_digit_primes = filter(lambda x: x>10**10, sieve_of_eratosthenes(10**11))
    #The tricky thing about this problem is that numbers that have 8 or 7 or 9 1s 2s (etc) are really sparse --
    #So while it may seem that generating primes is the answer
    #generating these sparse numbers then checking primality is actually far superior, by a factor of a few million if I had to guess
    print(sum([sum(S(10, i)) for i in range(10)]))
