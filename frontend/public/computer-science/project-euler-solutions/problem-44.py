
CAP = 3000
DISTANCECAP = CAP/10

pentagonalNumbers = [i*(3*i-1)/2 for i in range(0,CAP*2)]


#j,k pairs

JKPairs = [(n, i, i*(6*n+3*i-1)/2) for n in range(1, CAP) for i in range(1, DISTANCECAP) if i*(6*n+3*i-1)/2 in pentagonalNumbers]

for pair in JKPairs:
    n = pair[0]
    i = pair[1]
    pj = pair[2]
    if abs(pentagonalNumbers[n] - pj) in pentagonalNumbers[1:]:
        print abs(pentagonalNumbers[n] - pj)
        print "P({}) = {}".format(n, pentagonalNumbers[n])
        print "P({}) = {}".format(n+i, pentagonalNumbers[n+i])
        print "P({}) = {}".format(pentagonalNumbers.index(pj), pj)
        print (n, i)