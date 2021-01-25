fib = [1, 1]

while fib[-1] < 4000000:
	fib.append(fib[-1] + fib[-2])

print fib[2::3]
print sum(fib[2::3])