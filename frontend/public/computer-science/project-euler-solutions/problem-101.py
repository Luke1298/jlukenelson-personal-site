import math
import numpy as np
from scipy import linalg

U_n = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

print U_n(1)
print U_n(2)
print U_n(3)
print U_n(4)

FIT = [1]
RIT = [1]

for k in range(2, 11):
    a = np.array([[t**i for t in range(1, k+1)] for i in range(k)], dtype=np.float128).T
    b = np.array([U_n(i) for i in range(1, k+1)]).astype(np.float128)
    x = linalg.solve(a, b)
    print x

    RIT.append(sum([c*k**e for e, c in enumerate(x)]))
    FIT.append(sum([c*(k+1)**e for e, c in enumerate(x)]))

print RIT
print FIT

print int(sum(FIT))
print [U_n(i) for i in range(1, 13)]
