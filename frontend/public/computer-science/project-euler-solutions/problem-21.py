from math import sqrt
def get_proper_factors(n):
	step = 2 if n%2 else 1
	sol = list(set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0))))
	sol.remove(n)
	return sol
					
	
print sum([i for i in range(2, 10000) if (i == sum(get_proper_factors(sum(get_proper_factors(i)))) and sum(get_proper_factors(i)) != i)])
