from math import sqrt
def get_proper_factors(n):
	step = 2 if n%2 else 1
	sol = list(set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0))))
	sol.remove(n)
	return sol
	
lower_bound = 12
upper_bound = 28123

abundant_numbers = [i for i in range(lower_bound, upper_bound-lower_bound) if sum(get_proper_factors(i)) > i]

#print abundant_numbers

def can_be_sum(n, av_list):
	av_list = list(filter(lambda x: x < n, av_list))
	for k in av_list:
		if (n-k) in av_list:
			return True
	return False
	
sol = [i for i in range(lower_bound*2)]

for k in range(lower_bound*2+1, upper_bound+1):
	if not can_be_sum(k, abundant_numbers):
		sol.append(k)
		
print sum(sol)