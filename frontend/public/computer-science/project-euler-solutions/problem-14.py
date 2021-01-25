import numpy as np

def collatz(n):
	i = 1
	while n!=1:
		if n%2==0:
			n = n/2
		else:
			n = 3*n + 1
		i += 1
	return i
	
#print collatz(100)

print np.argmax([collatz(i) for i in range(1, 1000001)]) + 1 
	