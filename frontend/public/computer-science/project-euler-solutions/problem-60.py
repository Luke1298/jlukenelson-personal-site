import math

def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def isPrime(n):
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0 :
            return False
    return True


symetric_classes = [] #Note... We won't fill this with inheriently equivalence classes at first... Just symetries

primesUnder10000 = sieve_of_eratosthenes(10000)

print("----  Calculating Symetries  -----")
for i in range(len(primesUnder10000)):
    for j in range(i, len(primesUnder10000)):
        small = primesUnder10000[i]
        big = primesUnder10000[j]
        leftJoinPrimality = str(small) + str(big)
        rightJoinPrimlity = str(big) + str(small)
        if isPrime(int(leftJoinPrimality)) and isPrime(int(rightJoinPrimlity)):
            symetric_classes.append((small,big))
            symetric_classes.append((big,small))

#print(symetric_classes)

def searchForEquivalence(symetric_classes):
    relations = {}
    for s in symetric_classes:
        relations[s[0]] = [j[1] for j in symetric_classes if j[0] == s[0]]
    return relations

print("----  Calculating Equivalences  -----")

equiv_class = searchForEquivalence(symetric_classes)

print("----  Calculating Interest  -----")


list_of_interest = set()


class DepthSearch:
    def __init__(self, relations):
        self.relations = relations
        self.visited = []
        self.currentPath = []
        self.list_of_interest = []

    def dfs(self, node, NTS, step=1):
        self.visited.append(node)
        self.currentPath.append(node)
        if step >= 4:
            list_of_interest.add(frozenset(self.currentPath.copy()))
        for node in NTS:
            if node not in self.visited:
                self.dfs(node, NTS.intersection(set(self.relations[node])), step+1)
                self.currentPath.pop()

for k in equiv_class.keys():
    search = DepthSearch(equiv_class)
    search.dfs(k, set(equiv_class[k]))


#dfs(673, set(equiv_class[673]))

print("---- Answer -----")

for i in list_of_interest:
    if len(i) == 5:
        print(sum(i))
