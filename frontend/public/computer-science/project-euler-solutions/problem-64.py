from math import sqrt

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
#3 and 2 are broken on the one above...


numberOfOdd = 1
#sqrtPeriod(9876, laList=[], path=[])

for x in range(4, 10001):
    if x not in [i**2 for i in range(1, 101)]:
        repList = sqrtPeriod(x, laList=[], path=[])
        if len(repList) % 2 == 1:
            numberOfOdd += 1

print(numberOfOdd)
"""for x in range(3, 10000):
    if x not in [i**2 for i in range(1, 101)]:
        try:
            sqrtPeriod(x, laList=[], path=[])
        except RecursionError:
            print(x)"""
