from collections import Counter

bound = 5 #This was 3 in the problem

#(counter, [list-of-occurence])
permutations = {0:[0]}

i=1
while max([len(v) for v in permutations.values()]) < bound:
    c = frozenset(Counter(str(i**3)).items())
    permutations.setdefault(c,[]).append(i**3)
    i+=1

for perm in permutations.items():
    if len(perm[1]) == bound:
        print(min(perm[1]))
