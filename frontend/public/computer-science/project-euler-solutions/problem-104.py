from functools import wraps
from collections import Counter


oneToNineSet = set(map(str, range(1,10)))

def leftPandigital(num):
    return (set(Counter(num[:9]).keys()) == oneToNineSet)

def rightPandigital(num):
    return (set(Counter(num[-9:]).keys()) == oneToNineSet)


def checkDoubleSidePandigital(num):
    num = str(num)
    return leftPandigital(num) and rightPandigital(num)

"""fibList = [[1, 1], 2]
def fib(n):
    while fibList[1] < n:
        fibList[0].append(fibList[0][-1] + fibList[0][-2])
        fibList[0].pop(0)
        fibList[1] += 1
    return fibList[0][-1]"""

fibList = [1,1]

def nextFib():
    fibList.append(fibList[-1] + fibList[-2])
    return fibList[-1]

for k in range(329464):
    nextFib()

while not checkDoubleSidePandigital(fibList[k]):
    print k
    nextFib()
    k+=1

print k
