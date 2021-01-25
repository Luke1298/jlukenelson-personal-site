from math import floor, log
import operator

def product(iterable):
    return reduce(operator.mul, iterable, 1)

def power_eval(prime_fac):
	return product([p**e for (p,e) in prime_fac])

def combos(primes_av, ov_max, min):
	def log_eval(l):
		return sum([log(i) for i in l])
	def sub_combos(sub_list, sub_max, base=[], so_far=[]):
		if len(sub_list) == 1:
			#import pdb; pdb.set_trace()
			#print base
			min_p = int(max(base[-1][1], floor(log(min - power_eval(base))/log(sub_list[-1])))) if (min - power_eval(base)) > 0 else max(base[-1][1], 0)
			max_p = int(floor(log(sub_max)/log(sub_list[-1])))+1
			so_far += [(base + [(sub_list[-1], p)]) for p in range(min_p, max_p)]
			return
		else:
			max_p = int(floor(log(sub_max)/log_eval(sub_list)))
			#print base
			min_p = base[-1][1] if len(base) else 0
			#print sub_list[-1], min_p, max_p
			for p in range(min_p, max_p+1):
				base_copy = base[:]
				base_copy.append((sub_list[-1], p))
				sub_combos(sub_list[:-1], int(sub_max/(sub_list[-1]**p)), base_copy, so_far)
		return so_far
	return sub_combos(primes_av, ov_max)

def num_factors(l):
	return product([(i[-1]*2)+1 for i in l])

total_list = []
N = 50
Upper_range = 10000000000000000
Lower_ragne = 0
#Lower_ragne = 4000000
prime_list = list(reduce( (lambda r,x: r-set(range(x**2,N,x)) if (x in r) else r), range(2,N), set(range(2,N))))
prime_list.sort()
print prime_list
#print combos(list(reduce( (lambda r,x: r-set(range(x**2,N,x)) if (x in r) else r), range(2,N), set(range(2,N)))), Upper_range, Lower_ragne)
#print len(combos(list(reduce( (lambda r,x: r-set(range(x**2,N,x)) if (x in r) else r), range(2,N), set(range(2,N)))), Upper_range, Lower_ragne))

winner = 0
winning_set = []
for l in combos(prime_list, Upper_range, Lower_ragne):
	nf = num_factors(l)
	if nf > winner:
		winner = nf
		winning_set = l
	print l, nf, nf > 4000000
	if nf > 8000000: #THE NUMBER IS A PERFECT SQUARE EXACTLY HALF OF IT'S FACTORS WILL BE LESS THAN IT'S SQUARE ROOTS
		num = power_eval(l)
		print num


print "THE WINNER"
print winning_set, winner, winner>4000000

#[(31, 1), (29, 1), (23, 1), (19, 1), (17, 1), (13, 1), (11, 1), (7, 2), (5, 2), (3, 2), (2, 5)] 3007125 False
