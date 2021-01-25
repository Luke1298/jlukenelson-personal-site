sol_list = [[1]]

while len(sol_list) < 501:
	sol_list.append([sol_list[-1][-1] + i*len(sol_list)*2 for i in range(1, 5)])


print sum([sum(sub_list) for sub_list in sol_list])