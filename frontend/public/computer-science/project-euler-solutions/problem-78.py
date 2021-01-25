def sol(coin_types, to_make):
	sol_list = [0]*(to_make+1)
	for type in coin_types:
		sol_list[type] += 1
		for i in range(type, len(sol_list)):
			sol_list[i] += sol_list[i-type]
	return sol_list

CAP = 60000

coin_types = range(1, CAP+1)
print sorted(filter(lambda x: (x[1]% 1000000 == 0), map(lambda x:(x[0], x[1]), enumerate(sol(coin_types, CAP)))))#+1
