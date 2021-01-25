import math

def decimal2binary(dec):
    """TODO: This could be cleaner"""
    if dec < 2:
        return [dec]
    binary_powers = [1]
    while dec >= binary_powers[-1]:
        binary_powers.append(binary_powers[-1]*2)
    bin_list = [0] * (len(binary_powers) - 1)
    bin_list[(len(binary_powers) - 2)] = 1
    dec -= 2**(len(binary_powers) - 2)
    while dec != 0:
        binary_powers = filter(lambda x: x <= dec, binary_powers)
        bin_list[(len(binary_powers) - 1)] = 1
        dec -= 2**(len(binary_powers) - 1)
    return bin_list [::-1]

def ispalindrome(n):
    return n[:len(n)/2] == n[(len(n)+1)/2:][::-1]
    
sol_list = []

for x in range(1000000):
    if ispalindrome(decimal2binary(x)) and ispalindrome(str(x)):
        sol_list.append(x)
        
print sum(sol_list)