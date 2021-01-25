import os
import sys



scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p067_triangle.txt")

file = open(src_filename, "r")

src = file.read()


sol_list = [[int(i) for i in k.split(" ")] for k in  src.split("\n")[:-1]][::-1]


for i, v in enumerate(sol_list):
	if i+1 < len(sol_list):
		sol_list[i+1] = [max(v[j], v[j+1])+sol_list[i+1][j] for j in range(len(sol_list[i+1]))]

print(sol_list[-1][0])
