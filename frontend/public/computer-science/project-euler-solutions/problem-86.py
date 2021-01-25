import math
from collections import Counter
import itertools


LIMIT = 1800
#CAP = 100
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def iscoPrime(a, b):
    return gcd(a, b) == 1

def myround(x, base):
    return int(base * math.floor(float(x)/base))


class solver():
    def __init__(self, i):
        self.triags = []
        self.solutions = set()
        self.i = 0
        self.generateTriples(i)
        self.triagKeys(i)
        self.i = i

    def iterate(self, k=1):
        for _ in range(k):
            self.generateTriples(self.i+1)
            self.triagKeys(self.i+1)
            self.i += 1

    def generateTriples(self, N):
        # (m**2-n**2)**2 + (2mn)**2 = (m**2 + n **2)**2
        # => 2m**2 + 2mn <= N
        # => m**2 <= N//2
        # => m <= sqrt(N//2)
        for m in range(self.i, N):
            for n in range(1, m):
                if (m%2 == 1) and (n%2==1):
                    pass
                elif iscoPrime(m, n):
                    an = sorted(((m**2 - n**2), (2*m*n)))
                    #toReturn.append(tuple(sorted(((m**2 - n**2), (2*m*n), (m**2 + n**2)))))
                    if an[0] <= N:
                        self.triags.append(an)
        return self.triags


    def triagKeys(self, cap):
        for t in self.triags:
            a = t[0]
            for x in range(max(a, myround(self.i, a)), cap+1, a):
                usefulRangey = []
                y = t[1] * (x//a)
                if y>2*cap:
                    pass
                elif y>cap:
                    usefulRangey = range(y-cap, cap+1)
                else:
                    usefulRangey = range(1, (y//2)+1)
                self.solutions.update(filter(lambda t: t[0] >= t[1][-1], [(x, tuple(sorted((y-i, i)))) for i in usefulRangey]))
            b = t[1]
            for y in range(max(b, myround(self.i, b)), cap+1, b):
                usefulRangeX = []
                x = t[0] * (y//b)
                if x>cap:
                    pass
                else:
                    usefulRangeX = range(1, (x//2)+1)
                #self.solutions.update(filter(lambda t: ((t[1][1]/gcd(t[1][1], t[0]+t[1][0]), (t[0]+t[1][1])/gcd(t[0], t[1][0]+t[1][1])) in self.triags), filter(lambda t: t[0] <= t[1][-1], [(x, tuple(sorted((y-i, i)))) for i in usefulRangey])))
                self.solutions.update(filter(lambda t: t[0] >= t[1][-1], [(y, tuple(sorted((x-i, i)))) for i in usefulRangeX]))

val1 = solver(1818)
print(val1.i, len(val1.solutions))

val = solver(1800)
#print(sorted(val))
print(val.i, len(val.solutions))
val.iterate(18) #FOR SOME REASON THIS DOESN'T WORK EXACTLY.... BUT IT GIVES A REALLY GOOD APPROXIMATION
                #-- This iterate function gave that 1820 was the answer -- when it wasn't I just tried
                #recalcuation from the begging with 1819...1818...(which where bigger than 1 milllion) 1817... 
                #at 1817 it was less than a million
print(val.i, len(val.solutions))

diff = val1.solutions.difference(val.solutions)
import pdb; pdb.set_trace()
