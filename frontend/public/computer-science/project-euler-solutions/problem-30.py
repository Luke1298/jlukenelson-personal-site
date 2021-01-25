from progressbar import ProgressBar
pbar = ProgressBar()

def dig_pow_sum(n, p):
	return sum([int(i)**p for i in str(n)])
	
solList = []
for n in pbar(range(10, 1000000)):
	if n == dig_pow_sum(n, 5):
		solList.append(n)

print solList		
print sum(solList)