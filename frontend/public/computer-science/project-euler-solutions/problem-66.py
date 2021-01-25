from math import sqrt

"""def solveDiophantine(D, bound=10):
    DisEven = (D%2 == 0)
    skipx = 1
    startx = int(sqrt(D))
    if startx%2==0:
        startx -= 1
    if DisEven:
        skipx = 2
    for x in range(startx, bound, skipx):
        xisEven = (x%2 == 0)
        skipy = 1
        starty=1
        if xisEven:
            skipy = 2
        if not xisEven and not DisEven:
            skipy = 2
            starty = 2
        for y in range(starty, (x//int(sqrt(D)))+1, skipy):
            if x**2 - D*y**2 == 1:
                return x"""

squareList = [1]

def isPerfectSquare(n):
    while squareList[-1] < n:
        squareList.append((len(squareList) + 1)**2)
    return (n in squareList)

def sqrtPeriod(n, a=None, b=None, laList=[], path=[]):
    # b % new_b == 0
    #import pdb; pdb.set_trace()
    if a is None or b is None:
        a = int(sqrt(n))
        b = int(n - a**2)
        toAppend = a
        if len(laList) != 0:
            for e in laList:
                aHolder = a - e*b
                b_new = n - aHolder**2
                a_new = -1 * aHolder
                b_new = b_new // b
                a = a_new
                b = b_new
                if (a, b) in path:
                    return laList[:-1]
                path.append((a, b))
    toAppend = ((a//b)+1)
    aHolder = a - toAppend*b #the smallest value to make it negative
    b_new = n - aHolder**2
    if b_new < 0:
        laList[-1] += 1
        return sqrtPeriod(n, None, None, laList, [])
    else:
        a_new = -1 * aHolder
    b_new = b_new // b
    if b == 1:
        a_new = b_new
        b_new *= 2
    if (a_new, b_new) not in path:
        laList.append(toAppend)
        path.append((a_new, b_new))
        return sqrtPeriod(n, a_new, b_new, laList, path)
    else:
        return laList

def periodApproximation(period, a_init, bound=10000):
    U = [a_init, (a_init*period[0])+1]
    L = [1, period[0]]
    i = 1
    while len(U) < bound:
        if len(period) == 1:
            L.append(period[0]*L[-1] + L[-2])
            U.append(period[0]*U[-1] + U[-2])
        else:
            j = i % len(period)
            L.append(period[j]*L[-1] + L[-2])
            U.append(period[j]*U[-1] + U[-2])
        i+=1

    return U, L




def solveDiophantine(D):
    period = sqrtPeriod(D,laList=[],path=[])
    U, L = periodApproximation(period, int(sqrt(D)))
    for i in range(len(U)):
        if U[i]**2 - D*L[i]**2 == 1:
            return U[i]

#for D in [2,3,5,6,7]:
#    print(solveDiophantine(D))

sqaures = [j**2 for j in range(32)]
xSolutions = []

#print(solveDiophantine(52))
for D in range(4, 1000):
    if D not in sqaures:
        print(D, end = ' ')
        sol = solveDiophantine(D)
        xSolutions.append((D, sol))
        print(sol)

print(max(xSolutions, key=lambda x: x[1]))
