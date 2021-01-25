a_list = [i for i in range(3, 333)]

for a in a_list:
	for b in range(a, 666-a):
		c = 1000 - (a + b)
		if a**2 + b**2 == c**2:
			print a*b*c