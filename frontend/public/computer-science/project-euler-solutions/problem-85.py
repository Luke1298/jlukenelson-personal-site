import os
import sys
import math

#Some quick maths by hand has brought me to the solution that for a MxN rectangle there are ((m**2 + m) * (n**2 + n))/4
#'sub rectangles' Thus we see than N<=2000

closest = 1

for n in range(1, 2001):
    for m in range(1, int(math.ceil(math.sqrt(8000000/(n**2+n))))):
        if abs(2000000 - ((m**2 + m)*(n**2 + n))/4) < abs(2000000 - closest):
            closest = ((m**2 + m)*(n**2 + n))/4
            bestm = m
            bestn = n

print(bestm*bestn)
