import math

def sol(num):
	table = [i * num for i in range(10)]
	sol = []
	n_p_ten = int(10**(math.floor(math.log(num, 10))+1))
	diveden = max([i for i, k in enumerate(table) if k <= n_p_ten])
	sol.append((diveden, n_p_ten - diveden*num))
	while sol.count(sol[-1]) == 1:
		remainder = sol[-1][-1]
		if remainder < 0:
			return 0
		diveden = max([i for i, k in enumerate(table) if k <= 10*remainder])
		sol.append((diveden, 10*remainder - diveden*num))
	if (0, 0) in sol:
		return 0
	return len(sol)
	
print max([sol(i) for i in range(1, 1000)])
