def sol(coin_types, to_make):
	sol_list = [0]*(to_make+1)
	for type in coin_types:
		sol_list[type] += 1
		for i in range(type, len(sol_list)):
			sol_list[i] += sol_list[i-type]
	return sol_list[-1]
	
#coin_types = [1,2,5]
coin_types = [1, 2, 5, 10, 20, 50, 100, 200]
print sol(coin_types, 200)#+1