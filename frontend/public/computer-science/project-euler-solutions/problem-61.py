import math
import random


def boundryFinder(f, min=1000, cap=9999):
    start = 1
    answer = []
    while f(start) < min:
        start+=1
    print(f(start))
    while f(start) <= cap:
        answer.append(int(f(start)))
        start+=1
    return answer

T, S, P, Hx = lambda n: (n*(n+1)/2), lambda n: n**2, lambda n: (n*(3*n-1)/2), lambda n:n*(2*n-1)
Hp, O = lambda n: (n*(5*n-3)/2), lambda n: (n*(3*n-2))


polygon_numbers = list(map(boundryFinder, [T, S, P, Hx, Hp, O]))
#polygon_numbers = sorted(list(set(polygon_numbers)))

symetric_classes = [] #Note... We won't fill this with inheriently equivalence classes at first... Just symetries

print("----  Calculating Edges  -----")
for k in range(len(polygon_numbers)):
    for q in range(len(polygon_numbers)):
        for i in range(len(polygon_numbers[k])):
            for j in range(len(polygon_numbers[q])):
                right = str(polygon_numbers[k][i])[2:]
                left = str(polygon_numbers[q][j])[:2]
                if right == left:
                    symetric_classes.append(((k, polygon_numbers[k][i]),(q, polygon_numbers[q][j])))


#print(symetric_classes)
#print(symetric_classes)

answer = None

class Graph(object):
    def __init__(self, polygon_numbers):
        self.Graph = {}
        for e, num in enumerate(polygon_numbers):
            for n in num:
                self.Graph[(e, n)] = []
        self.visited = []
        self.visitedPtype = []
        self.currentPath = []
    def resetVisited(self):
        self.visited = []
        self.visitedPtype = []
        self.currentPath = []
    def populateFromList(self, symetric_classes):
        for s in symetric_classes:
            self.Graph[s[0]] += [j[1] for j in symetric_classes if j[0] == s[0]]
    def dfsSolver(self, cur, cycleSearch=True):
        self.visited.append(cur)
        self.currentPath.append(cur)
        self.visitedPtype.append(cur[0])
        if self.startNode in self.Graph[cur] and len(self.currentPath) == 6:
            self.answer = self.currentPath.copy()
        for node in self.Graph[cur]:
            if node not in self.visited and node[0] not in self.visitedPtype:
                self.dfsSolver(node)
                self.currentPath.pop()
                self.visitedPtype.pop()
    def searchForCycles(self, startNode):
        self.startNode = startNode
        self.dfsSolver(startNode)
        self.resetVisited()

print("----  Calculating Graph  -----")

polyGraph = Graph(polygon_numbers)
polyGraph.populateFromList(symetric_classes)

print("----  Finding Cycles  -----")
for key in polyGraph.Graph.keys():
    polyGraph.searchForCycles(key)
print(polyGraph.answer)

print("---- Answer -----")
print(sum(map(lambda x: x[1], polyGraph.answer)))
