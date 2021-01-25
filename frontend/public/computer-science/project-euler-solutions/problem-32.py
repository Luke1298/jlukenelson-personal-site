import itertools

def is_pandigital(in_list):
    in_list = map(int, in_list)
    if len(in_list) == 9 and set(in_list) == set(range(1,10)):
        return True
    return False
    

tens = list(itertools.permutations(range(1,10), 2))
hundreds = list(itertools.permutations(range(1,10), 3))


pandigital_products = []

for t in tens:
    for h in hundreds:
        tval = sum([x * 10**(1-i) for i, x in enumerate(t)])
        hval = sum([x * 10**(2-i) for i, x in enumerate(h)])
        if is_pandigital(str(tval) + str(hval) + str(tval*hval)):
            pandigital_products.append(tval*hval)
     
tens = range(1,10)
hundreds = list(itertools.permutations(range(1,10), 4))
     
for t in tens:
    for h in hundreds:
        tval = t
        hval = sum([x * 10**(3-i) for i, x in enumerate(h)])
        if is_pandigital(str(tval) + str(hval) + str(tval*hval)):
            pandigital_products.append(tval*hval)
                    

print pandigital_products
print sum(set(pandigital_products))