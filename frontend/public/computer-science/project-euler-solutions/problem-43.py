import itertools

#possibilities = list(itertools.permutations(range(0,10), 10)) WAY TO MANY

"""

This problem really starts off as a logic puzzle. Because the last 3 conditions are bigger than 10 (and because
in order for something to be divisable by 5 it must end with 0 or 5; we can easily narrow down our search
space from 10! to the following 3 endings: (See the Scanned problem-43.pdf for futher work on this)

"??????53901"
"??????57289"
"??????52867"

This is nice; as now we have taken this problem from very complicated conditions that we would have to reverse
engineer to 3. These three conditions will further narrow the search space to basically nothing

You'll notice this code runs in basically no time
"""

def getPossible(used):
    d3d4d5Possibilities = []
    totalGroupPossibilities = []
    
    for d4 in set(2*i for i in range(5)) - used:
        avialable = set(range(10)) - used
        avialable -= set([d4])
        for d3 in avialable:
            for d5 in avialable - set([d3]):
                if (d3+d4+d5) % 3 == 0:
                    d3d4d5Possibilities.append((d3, d4, d5))

    for pair in d3d4d5Possibilities:
        avialable = set(range(10)) - used
        avialable -= set(pair)
        for d1 in avialable:
            for d2 in avialable - set([d1]):
                totalGroupPossibilities.append((d1, d2, pair[0], pair[1], pair[2]))
                
    return totalGroupPossibilities

readyForCondition7 = []    
    
for x in [[5, 2, 8, 6, 7], [5, 3, 9, 0, 1], [5, 7, 2, 8, 9]]:
    for l in getPossible(set(x)):
        readyForCondition7.append(list(l) + x )

isCondition7 = lambda x: (x[4]*100 + x[5]*10 + x[6])%7==0     

print sum(int("".join(map(str, l))) for l in filter(isCondition7, readyForCondition7))


