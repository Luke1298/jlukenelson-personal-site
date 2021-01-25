import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def G(m, n):
    return sum([ncr(n-l*(m-1), l) for l in range(1, n//m+1)])

def rgb(n):
    return sum([G(m, n) for m in range(2,5)])

if __name__ == '__main__':
    #Verify
    print(rgb(5))
    print(rgb(50))
