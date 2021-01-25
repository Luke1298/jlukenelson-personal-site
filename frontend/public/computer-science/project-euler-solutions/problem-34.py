
def factorial(k):
    s = 1
    for i in range(1, k+1):
        s *= i
    return s
    
to_try = range(10, 10**7)

sol_list = []

def is_sum_factorial(t):
    if sum([factorial(int(i)) for i in str(t)]) == t:
        return True
    return False
    
    
for t in to_try:
    if is_sum_factorial(t):
        sol_list.append(t)
        
print sol_list
print sum(sol_list)