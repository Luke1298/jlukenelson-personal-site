from __future__ import division
import numpy as np
from itertools import permutations, product


formats = ["(d_1 o_1 d_2) o_2 (d_3 o_3 d_4)",
           "(d_1 o_1 d_2 o_2 d_3) o_3 d_4",
           "(d_1 o_1 (d_2 o_2 d_3)) o_3 d_4",
           "(d_1 o_1 d_2) o_2 d_3 o_3 d_4",
           "d_1 o_1 (d_2 o_2 d_3) o_3 d_4"]



def getArithmeticPossibilites(numList):
    possibilities = set()

    for f in formats:
        for operator_list in product('+-/*', repeat=3):
            ev = f
            for e, o in enumerate(operator_list):
                ev = ev.replace("o_{}".format(e+1), o)
            for dorder in permutations(numList, 4):
                ready_ev = ev
                for e, d in enumerate(dorder):
                    ready_ev = ready_ev.replace("d_{}".format(e+1), str(d))
                try:
                    possibilities.add(eval(ready_ev))
                except:
                    pass
    return possibilities

def countConsecutive(mySet):
    print mySet
    i = 0
    while i+1 in mySet:
        i+=1
    return i

sol = []

for a in range(1, 7):
    for b in range(a+1,8):
        for c in range(b+1,9):
            for d in range(c+1,10):
                ans = countConsecutive(getArithmeticPossibilites([a,b,c,d]))
                sol.append(([a,b,c,d], ans))
                print [a,b,c,d], ans

print max(sol, key=lambda x:x[1])
