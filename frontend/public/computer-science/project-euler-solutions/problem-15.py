def lattice_paths_nbyn(n):
	half_sol = [[1]]
	while len(half_sol) < n:
		half_sol_new = [sum(half_sol[-1][:i+1]) for i, _ in enumerate(half_sol[-1])]
		half_sol.append(half_sol_new+[2*sum(half_sol[-1])])
	return 2*sum(half_sol[-1])
	"""if n == 1:
		return [1]
	sol_list = [1, n]
	while len(sol_list) < n:
		sol_list.append(lattice_paths_nbyn(len(sol_list))"""

print lattice_paths_nbyn(20)