
import math

n_tuples = [tuple([i for i in range(1, k+1)]) for k in range(2, 7)]

upper_bound = [int(math.ceil((10**math.ceil((9./len(n))))/n[-1])) for n in n_tuples]

def ispandigital(k):
    if len(k) == 9:
        if set(k) == set([str(i) for i in range(1,10)]):
            return True
    return False
    
def strSum(l):
    to_return = ""
    for i in l:
        to_return += i
    return to_return
    
pos_solution = []    
for n_tupple, u in zip(n_tuples, upper_bound):
    for k in range(u):
        if ispandigital(strSum([str(k*n) for n in n_tupple])):
            pos_solution.append(int(strSum([str(k*n) for n in n_tupple])))
            
print max(pos_solution)

