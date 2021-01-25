import itertools
sol_list = sorted([int("".join(map(str, k))) for k in list(itertools.permutations([i for i in range(10)]))])
print sol_list[999999]

