from itertools import permutations, product
import math


CAP = 1000000000/3

almostEquilateralTriangle = []

for y in range(2, CAP+1):
    h = (3*y**2 - 2*y - 1)
    t = h + 4*y
    if int(math.sqrt(h) + 0.5)**2  == h:
        if int(math.sqrt(h) + 0.5)*(y+1) % 4 == 0:
            almostEquilateralTriangle.append((y, y, y+1))
            print almostEquilateralTriangle[-1]
    if int(math.sqrt(t) + 0.5)**2  == t:
        if int(math.sqrt(t) + 0.5)*(y-1) % 4 == 0:
            almostEquilateralTriangle.append((y, y, y-1))
            print almostEquilateralTriangle[-1]


print sum([sum(t) for t in almostEquilateralTriangle])
