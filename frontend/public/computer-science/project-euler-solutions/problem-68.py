import os
import sys
from itertools import permutations
import numpy as np

def perm(choices, num):
	result = 1
	for x in range(num):
		result *= (choices - x)
	return result

#Lets try m == 6
outer = range(6,11)


def solve(outer):
	inner = list(set(range(1,11)) - set(outer))
	couldWork = (sum(outer) + 2*sum(inner)) % 5

	if couldWork == 0:
		n = (sum(outer) + 2*sum(inner))//5
	else:
		return None

	a1 = min(outer)
	outer.remove(a1)
	X = np.array([[0,1,1,0,0],[0,0,1,1,0], [0,0,0,1,1], [1,0,0,0,1], [1,1,0,0,0]])
	for order in permutations(outer):
		order = list(order)
		order.insert(0, a1)
		y = n  - np.array(order)
		sol = np.linalg.solve(X, y)
		print(set(sol)==set(inner), order, sol)
		if set(sol)==set(inner):
			num_sol = ""
			for j in range(5):
				a = "".join(map(str, [order[j], int(sol[(j+1)%5]), int(sol[(j+2)%5])]))
				num_sol += a
			print(num_sol)

solve([6,7,8,9,10])
