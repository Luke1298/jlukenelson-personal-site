
def product(l):
    if l==[]:
        return 1
    sol = 1
    for t in l:
        sol *= t
    return sol
    
    
def C(n, r):
    return product(range((n-r)+1, n+1))/product(range(1, r+1))
    

print sum([C(n, r)  > 1000000 for n in range(1, 101) for r in range(n+1)])
